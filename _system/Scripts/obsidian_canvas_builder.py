#!/usr/bin/env python3
"""
Obsidian Canvas Builder (Grouped + Timeline + Colors + Result Transclusion)
---------------------------------------------------------------------------
- Groups notes by frontmatter `categories`
- Places notes left→right by frontmatter `started` date
- Colors groups (and optionally nodes) by category
- Builds edges from [[Wiki Links]] and [text](path/to.md)
- Filters categories; can hide notes with no categories AND no links
- NEW: If a note has a heading '# Result' or '# Results', its node becomes
       type='text' with text='![[<NoteTitle>#Result(s)]]' to show that section directly.
"""

from __future__ import annotations
from pathlib import Path
import argparse, json, re
from dataclasses import dataclass, field
from typing import Dict, List, Set, Tuple, Optional
from datetime import datetime

# ---------- Regex helpers ----------
FRONTMATTER_BLOCK_RE = re.compile(r'^---\s*\n(.*?)\n---\s*', re.DOTALL)
KV_RE = re.compile(r'^([A-Za-z0-9_\-]+)\s*:\s*(.*)$')
LIST_ITEM_RE = re.compile(r'^\s*-\s*(.+)$')
WIKILINK_RE = re.compile(r'\[\[([^\]|#]+)')
MDLINK_RE   = re.compile(r'\[[^\]]*?\]\(([^)]+?\.md)\)')
RESULT_HDR_RE = re.compile(r'(?mi)^[ \t]{0,3}#{1,6}[ \t]*(Result|Results)\b')

# ---------- Data models ----------
@dataclass
class Settings:
    vault: Path
    root: Optional[Path] = None
    include_subfolders: bool = True
    node_w: int = 380
    node_h: int = 260
    preserve_positions: bool = True
    canvas_path: Path = Path("_graphs/Knowledge.canvas")
    horiz_gap: int = 80
    vert_gap: int = 80
    group_padding: int = 60
    group_vertical_gap: int = 160
    multi_category: str = "first"       # 'first' or 'copy'
    bidirectional_only: bool = False
    include_categories: Set[str] = field(default_factory=set)
    exclude_categories: Set[str] = field(default_factory=set)
    hide_uncategorized_unlinked: bool = False
    color_nodes: bool = False           # also color file/text nodes with group color

@dataclass
class NoteInfo:
    path: Path
    rel: str                 # vault-relative posix path
    title: str               # file stem
    categories: List[str]    # may be []
    started: Optional[datetime]
    content: str
    result_section: Optional[str]       # "Result" or "Results" if header exists

@dataclass
class CanvasNode:
    id: str
    type: str                # "file" | "text" | "group"
    x: float
    y: float
    width: float
    height: float
    file: Optional[str] = None
    text: Optional[str] = None
    label: Optional[str] = None
    color: Optional[str] = None

@dataclass
class CanvasEdge:
    id: str
    fromNode: str
    toNode: str
    fromSide: str = "right"
    toSide: str = "left"
    label: Optional[str] = None
    color: Optional[str] = None

# ---------- Utils ----------
def uid(prefix="id") -> str:
    import random, time
    return f"{prefix}-{int(time.time()*1000)%100000000:08d}-{random.randint(1000,9999)}"

def read_text(p: Path) -> str:
    try: return p.read_text(encoding="utf-8")
    except: return ""

def parse_frontmatter(text: str) -> Dict[str, object]:
    m = FRONTMATTER_BLOCK_RE.match(text)
    if not m: return {}
    block = m.group(1).splitlines()
    data: Dict[str, object] = {}
    i=0
    while i < len(block):
        line = block[i].rstrip()
        kv = KV_RE.match(line)
        if kv:
            key,val=kv.group(1).strip(),kv.group(2).strip()
            if val=="":
                lst=[]; j=i+1
                while j<len(block) and LIST_ITEM_RE.match(block[j]):
                    lst.append(LIST_ITEM_RE.match(block[j]).group(1).strip()); j+=1
                data[key]=lst; i=j-1
            else:
                if val.startswith("[") and val.endswith("]"):
                    inner = val[1:-1]
                    data[key] = [x.strip().strip('"\'') for x in inner.split(",") if x.strip()]
                else:
                    data[key]=val.strip('"\'')
        i+=1
    return data

def parse_started(value: str) -> Optional[datetime]:
    if not value: return None
    for fmt in ("%Y-%m-%d","%Y/%m/%d","%d-%m-%Y"):
        try: return datetime.strptime(value, fmt)
        except: pass
    return None

def find_notes(settings: Settings) -> List[NoteInfo]:
    base=settings.vault.resolve()
    scan_root = (base / settings.root).resolve() if settings.root else base
    it = base.rglob("*.md") if settings.include_subfolders else scan_root.glob("*.md")
    notes=[]
    for p in it:
        if settings.root and not str(p.resolve()).startswith(str(scan_root)):
            continue
        text=read_text(p)
        fm=parse_frontmatter(text)
        raw = fm.get("categories", [])
        cats = ([raw] if isinstance(raw, str) and raw else list(raw)) if raw else []
        started = parse_started(str(fm.get("started","")).strip())
        # detect Result/Results section
        m_res = RESULT_HDR_RE.search(text)
        result_section = m_res.group(1) if m_res else None
        rel=str(p.resolve().relative_to(base).as_posix())
        notes.append(NoteInfo(
            path=p.resolve(),
            rel=rel,
            title=p.stem,
            categories=cats,
            started=started,
            content=text,
            result_section=result_section
        ))
    return notes

def build_title_index(notes: List[NoteInfo]) -> Dict[str, List[NoteInfo]]:
    idx: Dict[str, List[NoteInfo]] = {}
    for n in notes:
        idx.setdefault(n.path.stem, []).append(n)
    return idx

def extract_links(note: NoteInfo, title_index: Dict[str, List[NoteInfo]], vault: Path) -> Set[str]:
    links: Set[str] = set()
    for m in WIKILINK_RE.finditer(note.content):
        tgt = m.group(1).strip()
        if tgt in title_index:
            links.add(title_index[tgt][0].rel)
        else:
            tail = Path(tgt).name
            if tail in title_index:
                links.add(title_index[tail][0].rel)
    for m in MDLINK_RE.finditer(note.content):
        relp = (note.path.parent / m.group(1).strip()).resolve()
        if relp.suffix.lower()==".md" and relp.exists():
            links.add(str(relp.relative_to(vault).as_posix()))
    links.discard(note.rel)
    return links

def load_existing_positions(canvas_file: Path) -> Dict[str, Tuple[float,float,float,float,str]]:
    pos = {}
    if canvas_file.exists():
        try:
            data = json.loads(canvas_file.read_text(encoding="utf-8"))
            # We can only recover positions for previous 'file' nodes (Canvas doesn't store rel for 'text')
            for n in data.get("nodes", []):
                if n.get("type")=="file" and n.get("file"):
                    pos[n["file"]] = (n.get("x",0), n.get("y",0), n.get("width",380), n.get("height",260), n.get("id",""))
        except: pass
    return pos

# ---------- Color palette ----------
PALETTE = [
    "#A5B4FC", "#FCA5A5", "#86EFAC", "#FCD34D", "#93C5FD",
    "#F9A8D4", "#FCA5E1", "#FDBA74", "#67E8F9", "#C7D2FE",
    "#FDE68A", "#34D399", "#F87171", "#60A5FA", "#A78BFA"
]
def color_for(category: str) -> str:
    h = 0
    for ch in category:
        h = (h*33 + ord(ch)) & 0xFFFFFFFF
    return PALETTE[h % len(PALETTE)]

# ---------- Layout (grouped, left->right by started; text nodes for Result/Results) ----------
def layout_grouped(
    notes: List[NoteInfo],
    settings: Settings,
    existing_pos: Dict[str, Tuple[float,float,float,float,str]],
    category_colors: Dict[str, str]
) -> Tuple[List[CanvasNode], Dict[str,str], Dict[str,str]]:
    """
    Returns (nodes, id_map, note_category_map)
    note_category_map maps note.rel -> the category it was placed under
    """
    groups: Dict[str, List[NoteInfo]] = {}
    ungrouped: List[NoteInfo] = []

    for n in notes:
        cats = n.categories if settings.multi_category == "copy" else (n.categories[:1] if n.categories else [])
        if cats:
            for c in cats:
                groups.setdefault(c, []).append(n)
        else:
            ungrouped.append(n)

    # sort groups
    for c in groups:
        groups[c].sort(key=lambda n: (n.started or datetime.max, n.rel))

    nodes: List[CanvasNode] = []
    id_map: Dict[str,str] = {}
    note_category_map: Dict[str,str] = {}

    y = 0.0
    group_idx = 0
    for cat, items in groups.items():
        if group_idx > 0: y += settings.group_vertical_gap
        group_idx += 1

        cursor_x = settings.group_padding
        cursor_y = y + settings.group_padding

        placed_rels = set()
        for n in items:
            rel = n.rel
            color = category_colors.get(cat)

            # Prefer preserving old positions only if that node was previously a 'file' node
            use_existing = settings.preserve_positions and rel in existing_pos

            if use_existing:
                ex, ey, ew, eh, prev_id = existing_pos[rel]
                # Keep as 'file' node to preserve positions reliably
                node = CanvasNode(
                    id=prev_id or uid("node"),
                    type="file",
                    file=rel,
                    x=ex, y=ey, width=ew, height=eh,
                    color=(color if settings.color_nodes else None)
                )
            else:
                # If note has a Result/Results heading → make a 'text' node with transclusion
                if n.result_section:
                    transclusion = f"# [[{n.title}]]\n\n![[{n.title}#{n.result_section}]]"
                    node = CanvasNode(
                        id=uid("node"),
                        type="text",
                        text=transclusion,
                        x=cursor_x, y=cursor_y,
                        width=settings.node_w, height=settings.node_h,
                        color=(color if settings.color_nodes else None)
                    )
                else:
                    node = CanvasNode(
                        id=uid("node"),
                        type="file",
                        file=rel,
                        x=cursor_x, y=cursor_y,
                        width=settings.node_w, height=settings.node_h,
                        color=(color if settings.color_nodes else None)
                    )

                cursor_x += settings.node_w + settings.horiz_gap

            nodes.append(node)
            id_map[rel] = node.id
            note_category_map[rel] = cat
            placed_rels.add(rel)

        # group bounds
        if placed_rels:
            rightmost = max([nd.x + nd.width for nd in nodes if ((nd.file in placed_rels) or (nd.type=="text" and id_map.get(next((r for r in placed_rels if id_map[r]==nd.id), ""), None)==nd.id))])
            bottom   = max([nd.y + nd.height for nd in nodes if ((getattr(nd,"file",None) in placed_rels) or (nd.type=="text" and nd.id in {id_map[r] for r in placed_rels}))])
            gx = 0
            gy = y
            gw = rightmost + settings.group_padding
            gh = (bottom - y) + settings.group_padding
        else:
            gx, gy, gw, gh = 0, y, 600, settings.node_h + settings.group_padding*2

        group_node = CanvasNode(
            id=uid("group"),
            type="group",
            x=gx, y=gy, width=gw, height=gh,
            label=cat, color=category_colors.get(cat)
        )
        nodes.append(group_node)
        y = gy + gh

    # We postpone handling of truly ungrouped notes; filtering may drop them.
    return nodes, id_map, note_category_map

# ---------- Build edges + filtering ----------
def build_edges_and_filter(
    notes: List[NoteInfo],
    id_map: Dict[str,str],
    title_index: Dict[str, List[NoteInfo]],
    vault: Path,
    settings: Settings,
    note_category_map: Dict[str,str]
) -> Tuple[List[CanvasEdge], Set[str]]:
    known = {n.rel for n in notes}
    forward: Dict[str, Set[str]] = {}
    for n in notes:
        outs = extract_links(n, title_index, vault)
        outs = {q for q in outs if q in known}
        if outs:
            forward.setdefault(n.rel, set()).update(outs)

    if settings.bidirectional_only:
        for src in list(forward.keys()):
            to_remove = set()
            for tgt in forward[src]:
                if tgt not in forward or src not in forward[tgt]:
                    to_remove.add(tgt)
            if to_remove:
                forward[src] -= to_remove
            if not forward[src]:
                del forward[src]

    edges: List[CanvasEdge] = []
    for src, tgts in forward.items():
        sid = id_map.get(src)
        if not sid: continue
        for tgt in tgts:
            tid = id_map.get(tgt)
            if not tid: continue
            edges.append(CanvasEdge(id=uid("edge"), fromNode=sid, toNode=tid))

    # base keep set: everything
    keep: Set[str] = {n.rel for n in notes}

    # hide uncategorized & unlinked
    #if settings.hide_uncategorized_unlinked:
    #    degrees: Dict[str,int] = {n.rel:0 for n in notes}
    #    for s,tgts in forward.items():
    #        degrees[s] += len(tgts)
    #        for t in tgts:
    #            degrees[t] += 1
    #    new_keep=set()
    #    for n in notes:
    #        has_cat = n.rel in note_category_map
    #        if has_cat or degrees.get(n.rel,0) > 0:
    #            new_keep.add(n.rel)
    #    keep = new_keep

    # include/exclude categories
    #if settings.include_categories or settings.exclude_categories:
    #    final_keep = set()
    #    for rel in keep:
    #        cat = note_category_map.get(rel, None)
    #        if cat is None:
    #            if settings.include_categories:
    #                continue
    #            final_keep.add(rel)
    #        else:
    #            if settings.include_categories and cat not in settings.include_categories:
    #                continue
    #            if settings.exclude_categories and cat in settings.exclude_categories:
    #                continue
    #            final_keep.add(rel)
    #    keep = final_keep

    return edges, keep

# ---------- Main ----------
def main():
    ap=argparse.ArgumentParser(description="Generate/update an Obsidian Canvas grouped by categories and ordered by started date, with Result transclusion.")
    ap.add_argument("--vault", required=True, help="Path to Obsidian vault root")
    ap.add_argument("--canvas", default="_graphs/Knowledge.canvas", help="Output .canvas path relative to vault")
    ap.add_argument("--root", default="", help="Subfolder to scan (relative to vault). Blank = whole vault")
    ap.add_argument("--include-subfolders", action="store_true", help="Include subfolders when --root is set")

    ap.add_argument("--preserve-positions", action="store_true")
    ap.add_argument("--bidirectional-only", action="store_true")
    ap.add_argument("--multi-category", choices=["first","copy"], default="first")
    ap.add_argument("--color-nodes", action="store_true", help="Color file/text nodes with their group color")

    ap.add_argument("--include-categories", default="", help="Comma-separated list; include only these categories")
    ap.add_argument("--exclude-categories", default="", help="Comma-separated list; exclude these categories")
    ap.add_argument("--hide-uncategorized-unlinked", action="store_true",
                    help="Hide notes that have no categories AND no links (degree 0)")

    ap.add_argument("--node-size", nargs=2, type=int, default=[540,940], metavar=("WIDTH","HEIGHT"))
    args=ap.parse_args()

    settings = Settings(
        vault=Path(args.vault).expanduser(),
        canvas_path=Path(args.canvas),
        root=Path(args.root) if args.root else None,
        include_subfolders=args.include_subfolders or (not args.root),
        preserve_positions=args.preserve_positions,
        bidirectional_only=args.bidirectional_only,
        multi_category=args.multi_category,
        color_nodes=args.color_nodes,
        include_categories=set([s.strip() for s in args.include_categories.split(",") if s.strip()]),
        exclude_categories=set([s.strip() for s in args.exclude_categories.split(",") if s.strip()]),
        node_w=args.node_size[0],
        node_h=args.node_size[1],
    )

    vault = settings.vault.resolve()
    if not vault.exists():
        raise SystemExit(f"Vault path not found: {vault}")

    # Read notes
    notes = find_notes(settings)
    if not notes:
        print("No eligible notes found.")
        return

    # Colors per category
    categories = sorted({c for n in notes for c in n.categories})
    category_colors = {c: color_for(c) for c in categories}

    # Existing positions (for preserve; works for previous 'file' nodes)
    canvas_abs = (vault / settings.canvas_path).resolve()
    existing_pos = load_existing_positions(canvas_abs) if settings.preserve_positions else {}

    # Layout
    nodes, id_map, note_category_map = layout_grouped(notes, settings, existing_pos, category_colors)

    # Edges + filtering
    title_index = build_title_index(notes)
    edges, keep = build_edges_and_filter(notes, id_map, title_index, vault, settings, note_category_map)

    # Keep only nodes for notes in 'keep'; keep group nodes that still have children
    kept_node_ids = set()
    filtered_nodes: List[CanvasNode] = []
    kept_note_ids = {id_map[rel] for rel in keep if rel in id_map}

    for n in nodes:
        if n.type in ("file","text"):
            # Determine associated rel from id_map (reverse map)
            if n.id in kept_note_ids:
                filtered_nodes.append(n)
                kept_node_ids.add(n.id)
        else:  # group
            # keep group if any child note belongs to that category
            if n.label and any(note_category_map.get(rel)==n.label for rel in keep):
                filtered_nodes.append(n)
                kept_node_ids.add(n.id)

    edges = [e for e in edges if e.fromNode in kept_node_ids and e.toNode in kept_node_ids]

    canvas = {
        "nodes": [n.__dict__ for n in filtered_nodes],
        "edges": [e.__dict__ for e in edges],
        "version": 1
    }

    canvas_abs.parent.mkdir(parents=True, exist_ok=True)
    canvas_abs.write_text(json.dumps(canvas, indent=2), encoding="utf-8")
    print(f"Wrote canvas to: {canvas_abs}")
    print(f"Nodes: {len(canvas['nodes'])} | Edges: {len(canvas['edges'])}")

if __name__ == "__main__":
    main()
