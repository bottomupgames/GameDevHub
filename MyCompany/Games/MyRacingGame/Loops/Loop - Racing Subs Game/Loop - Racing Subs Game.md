---
tags:
  - loop
game: "[[MyCompany/Games/MyRacingGame/My Racing Game.md]]"
started: 2025-03-23
ended: 2025-06-30
due: 2025-05-30
cover:
---
# Problem Statement

> [!QUOTE]+ ## ***Design a “racing sub ” game, where subs can fly.***
> - Not sure what “racing subs ” look like. We need to define the look of both subs and racetracks.
> - Need to find a way to balance the game, so that subs spend the right amount of time in and out of the water.
> - Need to figure how to support networked multiplay.
> 

# Risks 

- If the racing subs look “too cartoony ” they might turn off older players. If they look too realistic, they might just seem silly with this kind of gameplay.
- Until we know how much time we are spending in and out of the water, it is impossible to design levels, or to do the artwork for the landscapes.
- The team has never done networked multiplay for a racing game. We aren’t completely sure we can do it.

# Desciption

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

- Artists will sketch different kinds of subs, in a number of different styles: cartoony, realistic, hyper-realistic, subs that are living creatures. The team will vote on them, and we will also informally survey members of our target audience. 
- Programmers and designers will work together on a very crude prototype that lets them experiment with how much time should be spent in and out of the water, and different mechanics for managing that. 
- Programmers will build a rough framework for networked multiplay that should handle all the kinds of messages this kind of game will need.




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


# Results

- Everyone loves the “ dino-sub ”designs. There is strong agreement between team members and potential audience members that “swimming dinosaurs ” are the right look and feel for this game. 
- After several experiments, it becomes clear that for most levels, 60% of time should be spent underwater, 20% in the air, and 20% near the surface, where players who grab the right powerups can fly above the water for a speed advantage. 
- The early networked experiments show that mostly the racing is not a problem for multiplay, but if we can avoid using rapid-fire machine guns, multiplay will be a lot easier.

# Backlogs of this Loop

- [ ] 

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

