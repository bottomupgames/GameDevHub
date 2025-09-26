

# Bases

```base
filters:
  and:
    - authors == ["OlivierTN"]
formulas:
  Categories: link(loop).asFile().toString().split("Loop - ")[-1].split(".")[0]
properties:
  formula.Categories:
    displayName: Loop
views:
  - type: table
    name: My Tasks
    order:
      - categories
      - formula.Categories
      - file.name
    sort:
      - property: categories
        direction: ASC
      - property: formula.Categories
        direction: ASC
      - property: started
        direction: ASC
    columnSize:
      note.categories: 185
      formula.Categories: 148

```




