Liste des boutons à référencer dans les notes.

Exemple de bouton :
````md
```button
name 2+2
type calculate
action 2+2
```
^button-2p2
````
```button
name 2+2
type calculate
action 2+2
```
^button-2p2

Exemple d'héritage :
````md
```button
name 2+2 Child
id 2p2
```
````
```button
name 2+2 Child
id 2p2
```


---
## Games

### Loops

```button
name New Loop
type append template
action Templater - Button Action - newLoop
```
^button-newLoop

### Solutions

```button
name New Concept
type append template
action Templater - Button Action - newConcept
```
^button-newConcept

```button
name New Prototype
type append template
action Templater - Button Action - newProto
```
^button-newProto

```button
name New Task
type append template
action Templater - Button Action - newTask
```
^button-newTask

## Gantt

```button
name Add Gantt Planner
type append template
action Templater - Button Action - addGanttPlanner
remove true
```
^button-addGanttPlanner


## Other 

```button
name Nouveau Arc Distinct
type append template
action Templater - Button Action - newArcDistinct
```
^button-newArcDistinct