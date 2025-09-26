 
# Weekly

```dataviewjs

// This is the Mermaid configuration.
//---displayMode: compact---
const mermaidConf = `mermaid
  gantt
	title Active Loops
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    tickInterval 1month
    todaymarker on
`;

// Critic Arcs
const promptCrit = `
  LIST WITHOUT ID 
  
  file.name + " :" + "crit, " + started + ", " + due
  FROM #loop
  WHERE !ended
  WHERE started
  WHERE due <= date(yesterday)
  SORT started desc
`;

// Active Arcs
const promptActive = `
  LIST WITHOUT ID 
  
  file.name + " :" + "active, " + started + ", " + due
  FROM #loop
  WHERE !ended
  WHERE started
  WHERE due > date(yesterday)
  SORT started desc
`;

// Query data and process output for critic items
const queryResultCrit = await dv.queryMarkdown(promptCrit);
const formattedListCrit = queryResultCrit.value.replace(/^-\s/gm, "");

// Query data and process output for active items
const queryResultActive = await dv.queryMarkdown(promptActive);
const formattedListActive = queryResultActive.value.replace(/^-\s/gm, "");

// Generate and write Mermaid Gantt Chart
const chartMarkup = `
  \`\`\`${mermaidConf}
  ${formattedListCrit}
  ${formattedListActive}
  \`\`\`
`;

dv.paragraph(chartMarkup);
```

```dataviewjs
//yyyy-MM-dd
const currentDate = new Date();
const currentDateString = currentDate.toISOString().split('T')[0];
const currentDateString2 = currentDate.toISOString().split('T')[0];

// This is the Mermaid configuration.
//---displayMode: compact---
const mermaidConf = `mermaid
  gantt
    title Protos & Tasks
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    tickInterval 1week
    todaymarker on
`;

// Critic Solutions
const promptCrit = `
  LIST WITHOUT ID 
  
  file.name + " :" + "crit, " + started + ", " + due
  FROM (#proto or #task or #concept)
  WHERE !ended and loop
  WHERE due and due <= date(yesterday)
  SORT started desc
`;

// Active Solutions
const promptActive = `
  LIST WITHOUT ID 
  
  file.name + " :" + "active, " + started + ", " + due
  FROM (#proto or #task or #concept)
  WHERE !ended and loop
  WHERE due and due > date(yesterday)
  SORT started desc
`;

const promptWaiting = `
  LIST WITHOUT ID 
  
  file.name + " :" + "${currentDateString}$" + ", " + "0d"
  FROM (#proto or #task or #concept)
  WHERE loop
  WHERE !started or !due and !ended
  SORT started desc
`;

// Query data and process output for critic items
const queryResultCrit = await dv.queryMarkdown(promptCrit);
const formattedListCrit = queryResultCrit.value.replace(/^-\s/gm, "");

// Query data and process output for active items
const queryResultActive = await dv.queryMarkdown(promptActive);
const formattedListActive = queryResultActive.value.replace(/^-\s/gm, "");

// Query data and process output for waiting items
const queryResultWaiting = await dv.queryMarkdown(promptWaiting);
const formattedListWaiting = queryResultWaiting.value.replace(/^-\s/gm, "");

// Generate and write Mermaid Gantt Chart
const chartMarkup = `
  \`\`\`${mermaidConf}
  section Active
  ${formattedListCrit}
  ${formattedListActive}

  section Waiting
  ${formattedListWaiting}
  \`\`\`
`;

dv.paragraph(chartMarkup);
```

**Games :**
```base
filters:
  and:
    - file.tags.contains("game")
    - ended.isEmpty()
views:
  - type: table
    name: Table
    order:
      - file.name
    sort:
      - property: started
        direction: ASC

```

**Loops :**
```base
filters:
  and:
    - file.tags.contains("loop")
    - ended.isEmpty()
formulas:
  Game: link(game).asFile()
views:
  - type: table
    name: Table
    order:
      - formula.Game
      - file.name
    sort:
      - property: started
        direction: ASC
    columnSize:
      formula.Game: 140

```


**Solutions :**
```base
filters:
  and:
    - "!loop.isEmpty()"
    - ended.isEmpty()
formulas:
  Game: link(loop).asFile()
  Author: authors
properties:
  formula.Game:
    displayName: Loop
views:
  - type: table
    name: Table
    order:
      - formula.Author
      - file.name
    sort: []
    columnSize:
      formula.Author: 140

```


#### To read & review:
```dataview
TABLE call_to_review
WHERE loop
WHERE call_to_review
SORT ended
```


# Tâches de la semaines

- [ ] 
# Remarques

- 
# Backlogs :

## Actives Loop's Backlogs
```dataviewjs
dv.taskList(dv.pages()
.file
.where(f => f.tags.includes("#loop"))
//.where(f => f.frontmatter.game)
.where(f => !f.frontmatter.ended)
.tasks
.where(t => !t.completed)
.where(t => t.text.trim().length > 1))
```



