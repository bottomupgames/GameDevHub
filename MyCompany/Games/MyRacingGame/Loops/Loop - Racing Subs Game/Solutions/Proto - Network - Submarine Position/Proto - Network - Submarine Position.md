---
tags: proto
loop: "[[MyCompany/Games/MyRacingGame/Loops/Loop - Racing Subs Game/Loop - Racing Subs Game.md]]"
categories:
  - Core Development
authors:
  - OlivierTN
started: 2025-05-27
ended: 2025-06-30
due: 2025-06-17
cover: "[[a026729a0e9_2.jpg]]"
call_to_review: []
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!TODO] Key question
> - [ ] Is it complicated to make a rough networking that synchronizes submarine position updates across clients.

> [!question] Additionnal questions (Additionnal/Secondary/Sub)
> - [ ] Is a free solution exists ?
> - [ ] Position replication is it smooth enough for racing speeds ?

# Description

> [!TIP]- **Reminder :** 
> - Answer a question
> - Forget quality
> - Don't get attached
> - Doesn't have to be digital
> - Doesn't have to be interative

This task focuses on implementing a crude network prototype to test the feasibility of real-time submarine racing. The goal is not polished gameplay but rather confirming that position updates can be transmitted and received accurately across multiple clients.

**Steps:**
1. Create a placeholder submarine pawn with simplified movement logic.
2. Add basic networking code to replicate submarine position, rotation, and velocity.
3. Set up a test environment with at least two clients to observe synchronization.
4. Introduce artificial latency to test desync and correction behavior.
5. Log update frequency and performance under different network conditions.
6. Document results for later refinement of multiplayer architecture.

# Result
![[a026729a0e9_2.jpg]]
> [!success] Succes
> - Submarine position updates replicated reliably between host and clients.
> - Lag compensation worked adequately at moderate speeds.

> [!failure] Failures
> - Flying transitions were harder to sync consistently than underwater movement.

> [!warning] Comments
> - 

>[!note] What's next? 
> - Compare peer to peer solution to client server.
>    

