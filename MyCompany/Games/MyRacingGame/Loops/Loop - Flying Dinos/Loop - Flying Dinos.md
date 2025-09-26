---
tags:
  - loop
game: "[[MyCompany/Games/MyRacingGame/My Racing Game.md]]"
started: 2025-06-06
ended:
due: 2025-09-22
cover:
---
# Problem Statement

> [!QUOTE]+ ## ***Design a “flying dinos ” game where dinosaurs race in and above the water.***
> - We need to figure out if we can schedule all the animation time needed for the dinosaurs.
> - We need to develop the “right” number of levels for this game.
> - We need to figure out all the powerups that will go into this game.
> - We need to determine all the weapons that this game should support (and avoid rapid-fire machine guns because of networking constraints)
> 

# Risks 

- Too childish, we want a target of 12-35 years old.

# Description

> [!TIP]- **Reminder :** The Lens of the Eight Filters
> - Does this game feel right?
> - Will the intended audience like this game enough?
> - Is this a well-designed game?
> - Is this game novel enough?
> - Will this game sell?
> - Is it technically possible to build this game?
> - Does this game meet our social and community goals?
> - Do the playtesters enjoy this game enough?

> [!TIP]- **Reminder :** The Lens of Toy
> - If my game had no goal, would it be fun at all ?
> - When people see my game, do they want to start interacting with it, even
before they know what to do?



# Solutions 

```dataviewjs
// Get all the elements
let pg = dv.current();
let parentFolder = dv.current().file.folder;

//yyyy-MM-dd
const currentDate = new Date();
const currentDateString = currentDate.toISOString().split('T')[0];

// This is the Mermaid configuration.
const mermaidConf = `mermaid
  gantt
    title Vue d'ensemble
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    tickInterval 1month
    todaymarker on
`;

const promptActive = `
  LIST WITHOUT ID 
  
  file.name + " :" + "active, " + started + ", " + due
  FROM "${parentFolder}"
  WHERE loop and contains(loop, this.file.link)
  WHERE started and due and !ended
  SORT started desc
`;

const promptEnded = `
  LIST WITHOUT ID 
  
  file.name + " :" + "done, " + started + ", " + ended
  FROM "${parentFolder}"
  WHERE loop and contains(loop, this.file.link)
  WHERE started and ended
  SORT started desc
`;

const promptWaiting = `
  LIST WITHOUT ID 
  
  file.name + " :" + "${currentDateString}$" + ", " + "0d"
  FROM "${parentFolder}"
  WHERE loop and contains(loop, this.file.link)
  WHERE !ended and (!started or !due)
  SORT started desc
`;


// Query data and process output for waiting items
const queryResultWaiting = await dv.queryMarkdown(promptWaiting);
const formattedListWaiting = queryResultWaiting.value.replace(/^-\s/gm, "");

// Query data and process output for active items
const queryResultActive = await dv.queryMarkdown(promptActive);
const formattedListActive = queryResultActive.value.replace(/^-\s/gm, "");

// Query data and process output for ended items
const queryResultEnded = await dv.queryMarkdown(promptEnded);
const formattedListEnded = queryResultEnded.value.replace(/^-\s/gm, "");


// Generate and write Mermaid Gantt Chart
const chartMarkup = `
  \`\`\`${mermaidConf}
  section Milestone
  DUE : milestone, ${pg.due}, 0d
  
  section Solutions
  ${formattedListActive}
  ${formattedListEnded}

  section Waiting
  ${formattedListWaiting}
  \`\`\`

`;

dv.paragraph(chartMarkup);
```

## Concepts :
```base
filters:
  and:
    - file.hasLink(this.file)
    - file.tags.containsAny("concept")
views:
  - type: table
    name: Concepts Table
    order:
      - file.name
    sort: []
  - type: cards
    name: Concepts Cards
    order:
      - file.name
      - categories
    sort:
      - property: started
        direction: ASC
    image: note.cover
    cardSize: 140
    imageFit: ""
    imageAspectRatio: 1

```
```button
name New Concept
id newConcept
```

## Prototypes :
```base
filters:
  and:
    - file.hasLink(this.file)
    - file.tags.containsAny("proto")
views:
  - type: table
    name: Concepts Table
    order:
      - file.name
    sort: []
  - type: cards
    name: Concepts Cards
    order:
      - file.name
      - categories
    sort:
      - property: started
        direction: ASC
    image: note.cover
    cardSize: 140
    imageFit: ""
    imageAspectRatio: 1

```
```button
name New Prototype
id newProto
```

## Tasks : 
```base
filters:
  and:
    - file.hasLink(this.file)
    - file.tags.containsAny("task")
views:
  - type: table
    name: Concepts Table
    order:
      - file.name
    sort: []
  - type: cards
    name: Concepts Cards
    order:
      - file.name
      - categories
    sort:
      - property: started
        direction: ASC
    image: note.cover
    cardSize: 140
    imageFit: ""
    imageAspectRatio: 1

```
```button
name New Task
id newTask
```



# Result

- 

# Backlogs of this Loop

- [ ] Add weapons
- [ ] Add air/water transition effects
- [x] Implement a basic Network solution
- [ ] Create a flying dino character
	- [x] concept
	- [ ] mod
	- [ ] anim

# Backlogs of Solutions
```dataviewjs
let currentFileName1 = dv.current().file.name + "]"
let currentFileName2 = dv.current().file.name + ".md"
let parentFolder = dv.current().file.folder

dv.taskList(dv.pages()
.file
.where(f => !f.tags.includes("#proto"))
.where(f => f.frontmatter.loop && (f.frontmatter.loop.contains(currentFileName1) || f.frontmatter.loop.contains(currentFileName2)))
.tasks
.where(t => !t.completed)
.where(t => t.text.trim().length > 1))
```

