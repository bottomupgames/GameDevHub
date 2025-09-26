<%*
const os = require('os');
const userName = os.userInfo().username;

const parentFile = tp.config.active_file.path;

if(tp.file.path(true).contains(userName + ".md")){
	const parentFolderPath = tp.file.path(true).split(tp.file.title + ".md")[0] + "Solutions/";
	//Chose the Proto Folder
	var subFolders = this.app.vault.getAllLoadedFiles().filter(i => i.children).filter(i => i.path.startsWith(parentFolderPath)).filter(i => !i.path.contains("/_resources"));
	var subFoldersPath = subFolders.map(folder => folder.path);
	var subFoldersName = subFolders.map(folder => folder.path.split(parentFolderPath)[1]);

	// Add "New Item" to the beginning of the subFolders arrays
	subFoldersPath.unshift(parentFolderPath);
	subFoldersName.unshift("NEW FOLDER");
	// Select an Arc path
	let subFolderPath = await tp.system.suggester(subFoldersName, subFoldersPath, false, "Task's folder : ");
	
	// Select new name
	let fileName = await tp.system.prompt("Name of the task : ", "Task - Task Name");
	
	//Create new folder
	if (subFolderPath === parentFolderPath) {
		subFolderPath = parentFolderPath + "/" + fileName;
		if (!subFoldersPath.contains(subFolderPath)) {
			await this.app.vault.createFolder(subFolderPath + "/");
		}
	}
	// Rename and move File
	await tp.file.rename(fileName);
	await tp.file.move(subFolderPath + "/" + fileName);
}
%>---
tags : task
loop : "[[<% parentFile %>]]"
categories: []
authors: []
started: <% tp.date.now("YYYY-MM-DD") %>
ended:
due:
cover:
call_to_review: []
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!TODO] Main Objective
> - 

> [!question] Secondaries Objectives
> - 

# Description




# Result

> [!warning] Comments
> - 

>[!note] Improvements and ideas
> - [ ] 
> 

