
# Mes notes

## Mes Liens utiles

- [[Lunch and Learn]]
- [[Task - Color - Palette - Underwater]]

---
# Backlogs paramétrable

> [!NOTE] Params
> targetAuthor:: "MorganeD"
> targetLoop:: "Loop - Flying Dinos"
> targetTags:: ["#task", "#concept"]

```dataviewjs
// Proprties
let targetAuthor = dv.current().targetAuthor;
let targetTags = dv.current().targetTags;
let targetLoop = dv.current().targetLoop;

// Retrieve and filter tasks, excluding empty tasks
let tasks = dv.pages()
.where(p => p.authors && p.authors.includes(targetAuthor))
.where(p => p.loop && p.loop.path.includes(targetLoop))
.file
.where(f => f.tags.some(tag => targetTags.includes(tag)))
.tasks
.where(t => !t.completed)
.where(t => t.text.trim().length > 1);

// Display the filtered tasks as a task list
dv.taskList(tasks);

```


# Historique de solutions :
```base
filters:
  and:
    - authors == ["MorganeD"]
views:
  - type: table
    name: Table
    order:
      - file.name
      - categories
    sort:
      - property: started
        direction: ASC
    columnSize:
      file.name: 390

```
