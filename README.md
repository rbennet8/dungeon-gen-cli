# dungeon-gen-cli
Command Line Interface Procedural Dungeon Generator for Dungeon Masters


# ⚔️ Player Rules & Reference

Since the **Dungeon Generator** handles the math for enemies and loot, players must follow these standardized rules to ensure the game balance remains fair (i.e., so you don't get one-shot by a Level 5 Grunt).

---

## 1. Character Creation (Level 1)
Every character begins with a baseline human stat block. You customize your hero by distributing points to fit your desired role (Tank, Mage, Rogue, etc.).

### Step A: Attributes
* **Base Stats:** All characters start with **3** in Strength, Dexterity, and Intelligence.
* **Point Buy:** You have **12 Points** to distribute among the three stats.
    * *Max Limit:* No stat can start higher than 10.
    * *Example Build:* Str 10, Dex 5, Int 3.

### Step B: Vitals (Derived Stats)
Calculate your starting vitals using these formulas:

| Stat | Formula |
| :--- | :--- |
| **Health (HP)** | `25 + (Strength * 2)` |
| **Mana** | `15 + (Intelligence * 2)` |
| **Armor (AC)** | `10 + (Dexterity / 3)` *(Round down)* |

### Step C: Traits
Roll a **1d3** (or a d6 divided by 2).
* The result is the number of **Physical or Psychological Traits** your character has.
* *Examples:* "Missing an eye", "Afraid of fire", "Double-jointed", "Gambling addict".

---

## 2. Leveling Up
When the DM grants a Level Up, apply the following increases to your character sheet:

### Attribute Growth
* **+3 Points** to distribute among Strength, Dexterity, or Intelligence.

### Vital Growth
* **Health:** Increase Max HP by **6**.
* **Mana:** Increase Max Mana by **3**.
* **Armor:** Increase Armor by **1** *only on even levels* (Levels 2, 4, 6, etc.).

---

## 3. Quick Reference Sheet

> **Creation (Level 1):**
> * **Stats:** Base 3/3/3. Add 12 Points.
> * **HP:** `25 + (Str * 2)`
> * **Mana:** `15 + (Int * 2)`
> * **Armor:** `10 + (Dex / 3)`
>
> **Leveling (+1 Level):**
> * **Stats:** +3 Points.
> * **HP:** +6.
> * **Mana:** +3.
> * **Armor:** +1 (Even levels only).


# ⚔️ Item Balancing Guide

Use this chart to determine how much damage items found in chests or dropped by enemies should do.

## Weapon Damage Standards
*Target: A standard enemy (Grunt) should die in 2-3 hits from a Common Weapon.*

| Level | Common Dmg | Rare Dmg | Legendary Dmg |
| :--- | :--- | :--- | :--- |
| **1** | 10 | 15 | 20 |
| **3** | 25 | 35 | 50 |
| **5** | 40 | 60 | 80 |
| **10** | 80 | 120 | 160 |

## Consumable Ideas
* **Health Potion:** Heals `Player Level * 10` HP.
* **Grenade/Bomb:** Deals `Player Level * 15` Damage (AoE).
* **Mana Potion:** Restores `Player Level * 5` Mana.

## Rarity Effects
* **Common:** Standard stats.
* **Rare:** 1.5x Stats OR adds a passive effect (e.g., "Attacks inflict Bleed").
* **Legendary:** 2.0x Stats OR adds a game-breaking ability (e.g., "Revive once per day", "Kill non-bosses instantly on a roll of 20").


# 📂 Project Structure

This repository contains two standalone Python scripts designed to run in a CLI (Command Line Interface).

## 1. `dungeon_gen.py` (The DM Engine)
This is the core tool for the Dungeon Master. It procedurally generates encounters, loot, and environments so you don't have to prep stats beforehand.

* **Campaign Configuration:** At launch, you define the **Player Count**, **Average Level**, and **Game Style** (Survival vs. Power Fantasy).
* **Procedural Biomes:**
    * **The Field:** Generates a "Warzone" or "Horde" battle with a hierarchy of enemies (Grunts → MiniBosses → Bosses).
    * **The Building:** Creates a dungeon crawl with 10-15 rooms, randomized loot containers, and enemy encounters.
    * **The Village:** Generates a network of roads and buildings with potential NPC trade encounters.
* **Math & Scaling:** Automatically scales enemy HP, Damage, and Armor based on the party level and selected difficulty.
* **Loot System:** Generates generic loot drops (e.g., "Rare Weapon", "Legendary Consumable") based on enemy tier.

## 2. `player_gen.py` (Character & NPC Generator)
A utility script to instantly generate stat blocks for players or NPCs. This is useful for spinning up a quick replacement character or populating a town with unique NPCs.

* **Point-Buy Simulation:** It uses the same math as the "Player Rules" below, simulating a player distributing points into Strength, Dexterity, and Intelligence.
* **Level Scaling:** Generates stats appropriate for any target level input.
* **Trait Randomizer:** Rolls a random number (1-3) to determine how many physical or psychological traits the character should possess.


# 🛡️ Combat Rules

## The Combat Round
1. **Initiative:** Roll `d20 + Dex`. Highest goes first.
2. **Action:** Move and Attack/Cast/Item.

## How to Attack
1. **Roll to Hit:** `1d20 + Stat` (Str for Melee, Int for Magic).
2. **Check:** If Result >= Enemy Armor, you hit.
3. **Deal Damage:** `Weapon Damage + Stat`.

## Enemy Logic
* **Enemy Attack:** `d20 + Enemy Strength`. Hits if >= Player Armor.
* **Enemy Damage:** Equals their **Strength** (Physical) or **Intelligence** (Magic).
    * *Crit Rule:* If a Natural 20 is rolled, double the damage.
