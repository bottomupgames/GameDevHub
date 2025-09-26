---
tags: task
loop: "[[MyCompany/Games/MyRacingGame/Loops/Loop - Racing Subs Game/Loop - Racing Subs Game.md]]"
categories:
  - Core Development
authors:
  - OlivierTN
started: 2025-05-01
ended: 2025-05-13
due: 2025-05-10
cover: "[[proto_racing_sub_in_motion_c339b_1.png]]"
call_to_review: []
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!TODO] Main Objective
> - Build a crude prototype that allows basic submarine controls: acceleration, diving, and surfacing.

> [!question] Secondaries Objectives
> - Validate whether acceleration feels distinct from standard racing car physics.
> - Test if vertical movement (dive/surface) integrates smoothly with horizontal racing flow.
> - Identify immediate control frustrations (sluggishness, over-responsiveness).

# Description

This task focuses on developing a quick, unpolished prototype to establish submarine handling fundamentals. By keeping the system simple, the team can rapidly evaluate whether the core movement — moving forward, diving underwater, and surfacing above — feels satisfying and intuitive.

**Steps:**
1. Reuse a base vehicle controller from an existing racing prototype.
2. Add vertical input mapping for diving and surfacing.
3. Implement basic acceleration with slight drag to simulate underwater resistance.
4. Test momentum preservation when transitioning between depths.
5. Run short playtest laps to assess feel and responsiveness.
6. Record initial tester impressions on whether the submarine feels distinct yet manageable.


# Result
![[proto_racing_sub_in_motion_c339b_1.png]]
> [!warning] Comments
> - Controls sometimes felt sluggish compared to expectations for a “racing” vehicle.

>[!note] Improvements and ideas
> - [x] Surface transitions were abrupt and needed smoothing.[[Task - Transition Mechanic between Air and Water]]
> - [ ] Add simple VFX feedback (bubbles, splashes) to emphasize movement.
> 

