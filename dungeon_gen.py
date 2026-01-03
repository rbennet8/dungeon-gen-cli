#!/usr/bin/env python3
"""
Dungeon Generator CLI
Generates procedural dungeons based on user inputs.
"""

import enum
import random

# Enums
class ItemType(enum.Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    CONSUMABLE = "Consumable"

class Rarity(enum.Enum):
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"

class EnemyTier(enum.Enum):
    GRUNT = "Grunt"
    MINIBOSS = "MiniBoss"
    BOSS = "Boss"
    FINALBOSS = "FinalBoss"

class Stats(enum.Enum):
    HEALTH = "Health"
    MANA = "Mana"
    STR = "Strength"
    DEX = "Dexterity"
    INT = "Intelligence"
    ARMOR = "Armor"

# Dungeon generator logic
BASE_STATS = {
    EnemyTier.GRUNT: {Stats.HEALTH: 10, Stats.MANA: 5, Stats.STR: 3, Stats.DEX: 3, Stats.INT: 2, Stats.ARMOR: 1},
    EnemyTier.MINIBOSS: {Stats.HEALTH: 50, Stats.MANA: 25, Stats.STR: 15, Stats.DEX: 10, Stats.INT: 10, Stats.ARMOR: 5},
    EnemyTier.BOSS: {Stats.HEALTH: 150, Stats.MANA: 50, Stats.STR: 30, Stats.DEX: 20, Stats.INT: 20, Stats.ARMOR: 10},
    EnemyTier.FINALBOSS: {Stats.HEALTH: 400, Stats.MANA: 100, Stats.STR: 50, Stats.DEX: 30, Stats.INT: 40, Stats.ARMOR: 20}
}

def generate_enemy_stats(enemy_tier, avg_level, total_mod):
    base_stats = BASE_STATS[enemy_tier]
    return {
        stat: max(1, int(value * avg_level * total_mod)) for stat, value in base_stats.items()
    }

def generate_loot(enemy_tier):
    drop_chance = {
        EnemyTier.GRUNT: 0.2,
        EnemyTier.MINIBOSS: 0.5,
        EnemyTier.BOSS: 0.8,
        EnemyTier.FINALBOSS: 1.0
    }
    if random.random() <= drop_chance[enemy_tier]:
        rarity = random.choices(
            [Rarity.COMMON, Rarity.RARE, Rarity.LEGENDARY],
            weights=[70, 25, 5] if enemy_tier == EnemyTier.GRUNT else
                     [30, 60, 10] if enemy_tier == EnemyTier.MINIBOSS else
                     [10, 40, 50]
        )[0]
        item_type = random.choice(list(ItemType))
        return f"{rarity.value} {item_type.value}"
    return "None"

def generate_biome_field(num_players, avg_level, total_mod):
    base_count = num_players * (4 if total_mod > 1 else 1)
    for i in range(base_count):
        tier = random.choices(
            [EnemyTier.GRUNT, EnemyTier.MINIBOSS, EnemyTier.BOSS],
            weights=[80, 15, 5]
        )[0]
        stats = generate_enemy_stats(tier, avg_level, total_mod)
        loot = generate_loot(tier)
        print(f"Enemy {i + 1} [{tier.value}] - Stats: {stats} | Loot: {loot}")
    # FinalBoss
    stats = generate_enemy_stats(EnemyTier.FINALBOSS, avg_level, total_mod * 2.5)
    loot = generate_loot(EnemyTier.FINALBOSS)
    print(f"FinalBoss - Stats: {stats} | Loot: {loot}")

def main():
    print("Welcome to Dungeon Generator\n")

    # Get inputs
    num_players = int(input("Enter the number of players: "))
    avg_level = int(input("Enter the average level of players: "))
    campaign_style = input("Enter campaign style (Survival/Power Fantasy): ").strip().lower()
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ").strip().lower()

    # Determine modifier
    campaign_mod = 1.5 if campaign_style == "survival" else 0.6
    difficulty_mod = 0.8 if difficulty == "easy" else 1.0 if difficulty == "medium" else 1.2
    total_mod = campaign_mod * difficulty_mod

    generate_biome_field(num_players, avg_level, total_mod)

if __name__ == "__main__":
    main()