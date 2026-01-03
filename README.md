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
