<%*
const os = require('os');
const userName = os.userInfo().username;

let keyProblem = "";
const parentFile = tp.config.active_file.path;

if(tp.file.path(true).contains(userName + ".md")){
	const parentFolderPath = tp.file.path(true).split(tp.file.title + ".md")[0];
	// Type an Arc name
	let fileName = await tp.system.prompt("Nom de l'Arc : ", "Arc - nouvel Arc");
	//Create new main folder
	const arcFolderPath = parentFolderPath + "/Arcs Distincts/" + fileName;
	await this.app.vault.createFolder(arcFolderPath + "/");
	// Create sub-folders
	await this.app.vault.createFolder(arcFolderPath + "/Solutions/");
	
	// Rename and move File
	await tp.file.rename(fileName);
	await tp.file.move(arcFolderPath + "/" + fileName);

} else {
	//tp.vault.delete(tp.file.path);
}
%>---
tags:
  - arcDistinct
game: "[[<% parentFile %>]]"
---
# Description

> [!QUOTE]+ ## ***Description***
> - 
> 

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
    axisFormat  %b %y
    tickInterval 1month
    todaymarker on
`;

const promptActive = `
  LIST WITHOUT ID 
  
  file.name + " :" + "active, " + started + ", " + due
  FROM "${parentFolder}"
  WHERE arc and contains(arc, this.file.link)
  WHERE started and due and !ended
  SORT started desc
`;

const promptEnded = `
  LIST WITHOUT ID 
  
  file.name + " :" + "done, " + started + ", " + ended
  FROM "${parentFolder}"
  WHERE arc and contains(arc, this.file.link)
  WHERE started and ended
  SORT started desc
`;

const promptWaiting = `
  LIST WITHOUT ID 
  
  file.name + " :" + "${currentDateString}$" + ", " + "0d"
  FROM "${parentFolder}"
  WHERE arc and contains(arc, this.file.link)
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
```dataview
TABLE rows.file.link as File
FROM #concept 
WHERE contains(arc, this.file.link)
SORT file.name ASC
GROUP BY categories
```
```button
name Nouveau Concept
id newConcept
```

## Prototypes :
```dataview
TABLE rows.file.link as File
FROM #proto 
WHERE contains(arc, this.file.link)
SORT file.name ASC
GROUP BY categories
```
```button
name Nouveau Prototype
id newProto
```

## Taches : 
```dataview
TABLE rows.file.link as File
FROM #task 
WHERE contains(arc, this.file.link)
SORT file.name ASC
GROUP BY categories
```
```button
name Nouvelle Tâche
id newTask
```

## Arcs
```dataview
TABLE
FROM #arc 
WHERE contains(arc, this.file.link)
SORT started ASC
```
```button
name Nouveau sousArc
id newArcMinor
```


# Backlogs de l'Arc

- [ ] 

# Backlogs des Solutions

```dataviewjs
let currentFileName1 = dv.current().file.name + "]"
let currentFileName2 = dv.current().file.name + ".md"
let parentFolder = dv.current().file.folder

dv.taskList(dv.pages()
.file
.where(f => !f.tags.includes("#proto"))
.where(f => f.frontmatter.arc && (f.frontmatter.arc.contains(currentFileName1) || f.frontmatter.arc.contains(currentFileName2)))
.tasks
.where(t => !t.completed)
.where(t => t.text.trim().length > 1))
```

