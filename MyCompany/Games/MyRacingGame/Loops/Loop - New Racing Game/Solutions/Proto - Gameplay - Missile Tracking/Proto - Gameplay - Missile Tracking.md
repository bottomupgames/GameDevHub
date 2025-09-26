---
tags: proto
loop: "[[MyCompany/Games/MyRacingGame/Loops/Loop - New Racing Game/Loop - New Racing Game.md]]"
categories:
  - Core Development
authors:
  - OlivierTN
started: 2025-03-08
ended: 2025-03-15
due: 2025-03-15
cover:
call_to_review: []
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!important] Key question
> - [x] Is a missile could be done under water ?

> [!question] Additionnal questions (Additionnal/Secondary/Sub)
> - [ ] What target-locking logic creates fair but exciting gameplay ?
> - [x] Can placeholder visuals still communicate the mechanic clearly ?

# Description

> [!TIP]+ **Reminder :** 
> - Answer a question
> - Forget quality
> - Don't get attached
> - Doesn't have to be digital
> - Doesn't have to be interative

This prototype explores how missile-tracking mechanics could enhance the chaos and strategy of an underwater racing game. Instead of polished assets, placeholder car weapons are used to test functionality.

**Steps:**
1. Reuse existing projectile code and add basic homing behavior (nearest target ahead).
2. Adjust missile speed and turn radius to balance pursuit realism with playability.
3. Replace car missile visuals with a simple torpedo-like placeholder mesh.
4. Run playtests to evaluate player reactions to being targeted and dodging missiles.
5. Collect qualitative feedback on whether missiles add fun tension or frustration.

# Results

> [!success] Succes
> - Tracking missiles created instant excitement and unpredictable race moments.
> - Even placeholder visuals were enough for testers to understand the mechanic.

> [!failure] Failures
> - Locking logic sometimes targeted the wrong vehicle.
> - Missiles circling endlessly when they missed their target frustrated players.

> [!warning] Comments
> - 

>[!note] What's next? 
> - Refine targeting system to prioritize nearest forward opponent.
> - ~~Add cooldown mechanics to avoid missile spam. [[Proto - Gameplay - Missile Tracking 001 - Missile Cooldown]]~~
> - Explore counterplay options (flares, evasive maneuvers).
>    

