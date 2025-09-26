---
tags: proto
loop: "[[MyCompany/Games/MyRacingGame/Loops/Loop - New Racing Game/Loop - New Racing Game.md]]"
categories:
  - Core Development
authors:
  - OlivierTN
started: 2025-03-01
ended: 2025-03-07
due: 2025-03-10
cover:
call_to_review: []
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!important] Key question
> - [x] Is it fun to drive with the moving constraints that water does ?

> [!question] Additionnal questions (Additionnal/Secondary/Sub)
> - [x] How does slower acceleration affect race pacing and excitement?
> - [x] Do driftier controls create the sensation of buoyancy without frustrating players?
> - [ ] Which mechanics from car handling can be adapted to simulate submarine physics?

> [!TIP]+ **Reminder :** 
> - Answer a question
> - Forget quality
> - Don't get attached
> - Doesn't have to be digital
> - Doesn't have to be interative

# Description

This task focuses on hacking a baseline racing game to mimic underwater submarine handling. Instead of building a system from scratch, modifications will simulate drag, drift, and slower responsiveness to evaluate how they influence the core racing experience.

**Steps:**
1. Reduce vehicle acceleration curve to create a feeling of underwater drag.
2. Increase steering drift to simulate resistance and buoyancy.
3. Test turning radius and momentum preservation to mimic water flow.
4. Playtest short laps with modified physics against unmodified versions.
5. Collect notes on player perception of “submarine-like” handling.

# Results

> [!success] Succes
> - Driftier handling was immediately perceived as “underwater” by testers.
> - Slower acceleration increased tension in races, creating a distinct feel.

> [!failure] Failures
> - Excessive drift led to frustration in tight corners.
> - Some players described movement as “sluggish” rather than “fluid.

> [!warning] Comments
> - 

>[!note] What's next? 
> - Fine-tune balance between drift and responsiveness.
> - Test handling in tracks with verticality to validate submarine-like gameplay.
> - Share prototype with programming team for shader and VFX integration.

