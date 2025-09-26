```mermaid
gantt
    title Composition Planning
    dateFormat  YYYY-MM-DD
    axisFormat  %d %b
    tickInterval 1day
    excludes    weekends
    todaymarker on
	
	Task 1 : <% tp.frontmatter.started %>, 1d
	Task 2 : <% tp.frontmatter.started %>, 5d
	Task Active : active, <% tp.frontmatter.started %>, 5d
	Task Done :   done,   <% tp.frontmatter.started %>, 5d
	Task Crit :   crit,   <% tp.frontmatter.started %>, 5d
	
	DUE : milestone, <% tp.frontmatter.due && tp.frontmatter.due !== "" ? tp.frontmatter.due : tp.date.now("YYYY-MM-DD") %>, 0d

```