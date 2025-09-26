---
tags: task
loop: "[[MyCompany/Games/MyRacingGame/Loops/Loop - Racing Subs Game/Loop - Racing Subs Game.md]]"
categories:
  - Core Development
authors:
  - OlivierTN
started: 2025-05-19
ended: 2025-05-27
due: 2025-05-26
cover: "[[d3daa46c85e_2.jpg]]"
call_to_review: []
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!TODO] Main Objective
> - Add a temporary mechanic that allows submarines to transition smoothly between underwater, surface, and flying states.

> [!question] Secondaries Objectives
> - Identify if transitions require visual or audio cues for clarity.
> - Ensure transitions don’t create unfair advantages in multiplayer balance.

# Description

This task focuses on creating an early, unpolished system that lets players move in and out of the water seamlessly. Rather than building the final version, this temporary mechanic is intended to test pacing, player perception, and technical feasibility of handling vertical transitions.

**Steps:**
1. Add collision-based triggers where subs enter/exit the water plane.
2. Apply placeholder VFX (splash, bubbles, foam) when crossing the water surface.
3. Smooth speed adjustments when moving between states (drag underwater, acceleration in air).
4. Test vertical momentum preservation during dive/surface transitions.
5. Run short playtests on prototype tracks to evaluate feel and readability.
6. Gather feedback on whether transitions are exciting, confusing, or frustrating.


# Result
![[d3daa46c85e_2.jpg]]
> [!warning] Comments
> - Basic transition mechanic allowed subs to dive and leap out of water smoothly.

>[!note] Improvements and ideas
> - [ ] Add stronger audio and particle cues for clarity.
> 

