---
tags: task
loop: "[[MyCompany/Games/MyRacingGame/Loops/Loop - Flying Dinos/Loop - Flying Dinos.md]]"
categories:
  - Core Development
authors:
  - OlivierTN
started: 2025-07-05
ended: 2025-08-05
due: 2025-08-11
cover: "[[3c43a6c1afe_3.jpg]]"
call_to_review: []
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!TODO] Main Objective
> - Set up a dedicated networking project to test and validate multiplayer features..

> [!question] Secondaries Objectives
> - Ensure the project includes a lightweight framework for position replication, collision handling, and powerup synchronization.
> - Establish a foundation that can later integrate weapons, powerups, and lap tracking.

# Description
**resources :**
- [[Proto - Network - Submarine Position]]


This task involves creating a new project dedicated to networking experiments, separate from the main game prototype. The networking project will allow programmers to test replication, synchronization, and multiplayer stability in a controlled environment before merging solutions into the core game.

**Steps:**
1. Create a blank Unreal Engine project configured for multiplayer testing.
2. Set up base submarine pawn with placeholder movement controls.
3. Implement basic replication of position, rotation, and velocity.
4. Add debugging overlays to monitor latency and update frequency.
5. Test client-server connections with 2–4 simulated players.
6. Document project setup so it can be reused by the entire team.


# Result
![[3c43a6c1afe_3.jpg]]

> [!warning] Comments
> - Provided a safe environment to iterate on multiplayer without affecting main prototype.
> - Some debugging tools required extra setup before being reliable.

>[!note] Improvements and ideas
> - [ ] Prepare a testing environment for simulating latency, packet loss, and desync issues.
> 

