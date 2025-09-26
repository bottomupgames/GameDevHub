---
tags:
  - loop
game: "[[MyCompany/Games/MyRacingGame/My Racing Game.md]]"
started: 2025-03-01
ended: 2025-03-28
due: 2025-03-28
cover:
---
# Problem Statement

> [!QUOTE]+ ## ***Come up with a new kind of racing game***
> - Underwater submarine races (with torpedoes)

# Risks 

- Not sure what underwater racetraks should look like.
- This might not feel innovative enough.
- Technology might not be able to handle all th water effects.

# Description



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
    title Overview
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




# Results

> [!TIP]- **Reminder :** The Lens of the Eight Filters
> - Does this game feel right?
> - Will the intended audience like this game enough?
> - Is this a well-designed game?
> - Is this game novel enough?
> - Will this game sell?
> - Is it technically possible to build this game?
> - Does this game meet our social and community goals?
> - Do the playtesters enjoy this game enough?

- Underwater racetracks look okay if there is a “glowing path ” in the water. Underwater tunnels will be cool! So will flying submarines following tracks that go in and out of the water! 
-  Early prototypes seem fun, provided the submarines are very fast and maneuverable. It will be necessary to make them be “racing subs. ” The mix of flying and swimming feels very novel. Subs should go faster when flying, so we will need to find a way to limit the amount of time they can spend in the air. The little playtesting we have done makes it clear this game must support networked multiplay.
- Some water effects are easier than others. Splashes look good, so do underwater bubbles. Making the whole screen waver takes too much CPU, and is kind of distracting anyway.

# Backlogs of this Loop

- [ ] 
 
# Backlogs of the Solutions
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




