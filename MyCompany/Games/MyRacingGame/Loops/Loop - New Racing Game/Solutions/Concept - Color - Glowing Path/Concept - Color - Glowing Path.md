---
tags: concept
loop: "[[MyCompany/Games/MyRacingGame/Loops/Loop - New Racing Game/Loop - New Racing Game.md]]"
categories:
  - Environment Art
authors:
  - MorganeD
started: 2025-03-09
ended: 2025-03-10
due: 2025-03-10
call_to_review:
  - MorganeD
  - OlivierTN
cover: "[[futuristic_87a9ecj.jpg]]"
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!important] Main Objective
> - Define a readable and visually striking color palette for underwater racetrack paths.

> [!question] Secondaries Objectives
> - Which colors remain the most visible against deep-water backgrounds?
> - How strong should the glow/bloom be without overwhelming the scene?
> - Does the palette remain readable in both single-player and splitscreen?

# Description

The goal is to test multiple glowing color palettes to find the most effective for guiding players along underwater racetracks.

Steps explored:

- Collected photographic references of deep-sea lighting and neon-lit environments.
- Designed quick digital mockups of racetracks with cyan, magenta, yellow, and lime green glows.
- Tested variations of bloom intensity and light diffusion in simulated water shaders.
- Compared readability under different lighting conditions: clear water vs. murky, daylight vs. deep-sea.

```img-gallery
path: MyCompany/Games/MyRacingGame/Loops/Loop - New Racing Game/Solutions/Concept - Color - Glowing Path/_resources/01
type: vertical
gutter: 8
radius: 8
columns: 4
mobile : 2
sortby: name
sort: asc
```
```img-gallery
path: MyCompany/Games/MyRacingGame/Loops/Loop - New Racing Game/Solutions/Concept - Color - Glowing Path/_resources/02
type: vertical
gutter: 8
radius: 8
columns: 4
mobile : 2
sortby: name
sort: asc
```

# Results
![[futuristic_87a9ecj.jpg]]

> [!warning] Comments
> - Lime green and cyan were the most universally readable.
> - Moderate bloom creates a strong guiding line without blinding players.
> - Pure white glow is too aggressive and fatigues the eyes.
> - Magenta looks good in stills but loses clarity during motion.

>[!note] Improvements and ideas
> - [x] Test palette in dynamic race scenarios with moving submarines. [[Task - Color - Palette - Underwater]]
> - [ ] Validate readability in splitscreen mode with reduced resolution.
> 
