---
tags: task
loop: "[[MyCompany/Games/MyRacingGame/Loops/Loop - Flying Dinos/Loop - Flying Dinos.md]]"
categories:
  - Animation
  - Core Development
authors:
  - OlivierTN
started: 2025-09-09
ended:
due: 2025-09-26
cover:
call_to_review:
  - MorganeD
---

```button
name Add Gantt Planner
id addGanttPlanner
```
# Objectives

> [!TODO] Main Objective
> - Create first anim blueprint for the main dino

> [!question] Secondaries Objectives
> - Should works in  network
> - Find a good animation nomencalture

# Description

This is more than just applying animations — I want to explore the technologies around Animation Blueprints. The goal is to answer a few essential questions for this project:

- How to manage the ABPs (Animation Blueprints) of multiple characters without duplicating logic? Hierarchy? Component?
- How to prevent an ABP from becoming increasingly complex with each new Ability added?
- How to name animations and organize them in folders?

# Refs
## 1. Older projects

### 1. Previous Project study (EVA)
```img-gallery
path: MyCompany/Games/MyRacingGame/Loops/Loop - Flying Dinos/Solutions/Task - Dino - Create anim blueprint/_resources/01/EVA/1
type: vertical
gutter: 8
radius: 8
columns: 3
mobile : 2
sortby: name
sort: asc
```
**ABP Logic** (3 steps):
1. The **Base**: Main logic for _locomotion_ / _falling_ / _overlay_
2. **Override Specials**: Either a simple _loop animation_ or a more complex _layer_, activated with BlendPosesByBools.
3. **Slots**: Used by _AnimMontages_ (mostly triggered from Abilities).

![[Drawing 2024-03-22 10.41.16.excalidraw|1000]]

**Naming Convention**:  
`NAME_action_to_action_Direction`  
Examples:
- EVA_bubble_idle_01
- EVA_carrier_combo_wait_idle_01
- EVA_carrier_combo_wait_to_stop
- EVA_attract_hold_to_snap_right
- EVA_attract_hold_to_steer_back
- EVA_attract_hold_to_steer_back_Montage

Problem: All animations are in one folder, making search laborious. It becomes worse when animations are split into steps and reordered alphabetically.

### 2. Advanced Locomotion System V4

```img-gallery
path: MyCompany/Games/MyRacingGame/Loops/Loop - Flying Dinos/Solutions/Task - Dino - Create anim blueprint/_resources/01/ALS/1
type: vertical
gutter: 8
radius: 8
columns: 5
mobile : 2
sortby: name
sort: asc
```

**ABP Logic**:
- Relies heavily on _State Machines_ and _Save Cache Pose_.
- Uses curves inside animations (e.g., `Wait_Gait` to control _Lean_).
- Graph becomes increasingly complex with each new state, requiring deep knowledge of the whole system.

![[Drawing 2024-03-22 12.00.52.excalidraw|1000]]

**Naming Convention**:  
`NAME_STANCE_Action_DIRECTION`
- Organized by folders (Actions, AimOffset, Base, Overlay, etc.).
- But ends up with inconsistencies across animation sets.

### 3. LEGO Fortnite
```img-gallery
path: MyCompany/Games/MyRacingGame/Loops/Loop - Flying Dinos/Solutions/Task - Dino - Create anim blueprint/_resources/01/LEGO
type: vertical
gutter: 8
radius: 8
columns: 5
mobile : 2
sortby: name
sort: asc
```
No details on ABP logic, but they have a custom tool for recording animations.
**Naming Convention**:  
`AnimationType/PawnName_Variant_Name_Suffix`
- AnimationType is restricted to predefined categories (Action, AimOffset, Locomotion, etc.).
- Suffix options include Directions (N, S, E, W, etc.), movement types (Loop, Stop, Pose, Intro, Outro, etc.).
- Despite rules, inconsistencies still appear when animators create custom suffixes.

# Technologies
- Read :
	- [animation-blueprint-linking-in-unreal-engine](https://docs.unrealengine.com/5.0/en-US/animation-blueprint-linking-in-unreal-engine/)
	- [Blend Nodes et Inertialization](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprint-blend-nodes-in-unreal-engine?application_version=5.1)
- Videos :
	- [4 - Animation Layer Interface and Linked Anim Layers - Bow And Arrow - UE5 Blueprints](https://youtu.be/WAkiE6rQutU?si=PQTXpK1FmxESwkI4)
	- [UE5 Character Locomotion Tutorial 6 | Animation layer Interfaces](https://www.youtube.com/watch?v=pcDOpYXCQyU)

### 1. Templates
- **ABPT (Template)**: Can be used as a parent ABP for any Skeleton. Animations can be replaced with the _AssetOverrideEditor_.
- **ABPC (Component)**: Called within other ABPs, acts like a Layer. Accessed with _LinkAnimGraph_. However, animations can’t be overridden via AssetOverrideEditor anymore.

### 2. Interfaces
Allow linking external Animation Layers during runtime via _LinkAnimationGraph_.

# Implementation

Findings:
- A single Blueprint for all characters is possible via a **Template** (`ABPT_PlayerCharacter`).
- Abilities can stay modular thanks to **Interfaces**. Each Ability can manage its own animations independently.

```img-gallery
path: MyCompany/Games/MyRacingGame/Loops/Loop - Flying Dinos/Solutions/Task - Dino - Create anim blueprint/_resources/03
type: vertical
gutter: 8
radius: 8
columns: 1
mobile : 1
sortby: name
sort: asc
```




# Apply on main Dino




[...]






# Result

> [!warning] Comments
> - 

>[!note] Improvements and ideas
> - [ ] 
> 

