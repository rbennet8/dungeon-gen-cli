import random
import time
from enum import Enum
from dataclasses import dataclass

# --- CONFIGURATION & ENUMS ---

class ItemType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    CONSUMABLE = "Consumable"

class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"

class EnemyTier(Enum):
    GRUNT = "Grunt"
    MINIBOSS = "MiniBoss"
    BOSS = "Boss"
    FINALBOSS = "FinalBoss"

class Biome(Enum):
    FIELD = "Field"
    BUILDING = "Building"
    VILLAGE = "Village"

@dataclass
class Stats:
    hp: int
    mana: int
    strength: int
    dexterity: int
    intelligence: int
    armor: int

# Base stats for Level 1 entities
BASE_STATS = {
    EnemyTier.GRUNT: Stats(hp=20, mana=5, strength=4, dexterity=4, intelligence=2, armor=10),
    EnemyTier.MINIBOSS: Stats(hp=60, mana=20, strength=8, dexterity=6, intelligence=6, armor=14),
    EnemyTier.BOSS: Stats(hp=150, mana=50, strength=12, dexterity=10, intelligence=10, armor=16),
    EnemyTier.FINALBOSS: Stats(hp=400, mana=100, strength=18, dexterity=14, intelligence=14, armor=18)
}

# --- CORE LOGIC CLASS ---

class DungeonGenerator:
    def __init__(self):
        self.num_players = 0
        self.avg_level = 0
        self.difficulty_mod = 1.0
        self.campaign_mod = 1.0  # Stat multiplier
        self.spawn_mod = 1.0     # Horde multiplier
        self.loot_chance_mod = 0.0 # Additive percentage

    def setup(self):
        print("\n--- DM ASSISTANT: CAMPAIGN SETUP ---")
        try:
            self.num_players = int(input("Number of Players: "))
            self.avg_level = int(input("Average Party Level: "))
            
            # Campaign Style
            print("\nCampaign Style:")
            print("1. Survival (Tougher enemies, scarce loot)")
            print("2. Power Fantasy (Hordes of weaker enemies, plentiful loot)")
            style = input("Select (1/2): ")
            if style == "1": # Survival
                self.campaign_mod = 1.5
                self.spawn_mod = 1.0
                self.loot_chance_mod = -0.2
            else: # Power Fantasy
                self.campaign_mod = 0.6
                self.spawn_mod = 4.0 # The "Horde" multiplier
                self.loot_chance_mod = 0.2

            # Difficulty
            print("\nDifficulty:")
            print("1. Easy (0.8x Stats)")
            print("2. Medium (1.0x Stats)")
            print("3. Hard (1.2x Stats)")
            diff = input("Select (1/2/3): ")
            if diff == "1": self.difficulty_mod = 0.8
            elif diff == "3": self.difficulty_mod = 1.2
            else: self.difficulty_mod = 1.0
            
        except ValueError:
            print("Invalid input. Using defaults.")
            self.num_players = 4
            self.avg_level = 1

    def calculate_stats(self, tier: EnemyTier) -> Stats:
        base = BASE_STATS[tier]
        # Final Boss gets an extra internal boost on top of base stats if needed
        boss_mult = 2.5 if tier == EnemyTier.FINALBOSS else 1.0
        
        # Total Multiplier
        total_mod = self.avg_level * self.difficulty_mod * self.campaign_mod * boss_mult
        
        return Stats(
            hp=max(1, int(base.hp * total_mod)),
            mana=max(1, int(base.mana * total_mod)),
            strength=max(1, int(base.strength * total_mod)),
            dexterity=max(1, int(base.dexterity * total_mod)),
            intelligence=max(1, int(base.intelligence * total_mod)),
            armor=max(1, int(base.armor * (1 + (self.avg_level * 0.05)))) # Armor scales slower
        )

    def generate_loot(self, tier: EnemyTier) -> str:
        # Base Chance check
        chance = 0.3 + self.loot_chance_mod
        
        # Higher tiers have higher drop chances
        if tier == EnemyTier.MINIBOSS: chance += 0.3
        if tier == EnemyTier.BOSS: chance += 0.5
        if tier == EnemyTier.FINALBOSS: return f"{Rarity.LEGENDARY.value} {random.choice(list(ItemType)).value}"

        if random.random() > chance:
            return "None"

        # Determine Rarity based on Tier
        roll = random.random()
        item_type = random.choice(list(ItemType)).value
        
        rarity = Rarity.COMMON.value
        if tier == EnemyTier.GRUNT:
            if roll > 0.9: rarity = Rarity.RARE.value
        elif tier == EnemyTier.MINIBOSS:
            if roll > 0.5: rarity = Rarity.RARE.value
        elif tier == EnemyTier.BOSS:
            if roll > 0.3: rarity = Rarity.LEGENDARY.value
            else: rarity = Rarity.RARE.value
            
        return f"{rarity} {item_type}"

    def print_enemy(self, tier: EnemyTier, index=None):
        stats = self.calculate_stats(tier)
        loot = self.generate_loot(tier)
        name = f"{tier.value}"
        if index is not None:
            name = f"{tier.value} #{index}"
            
        print(f"[{name}] HP:{stats.hp} AC:{stats.armor} Str:{stats.strength} | Drop: {loot}")

    def run_field(self):
        print("\n--- BIOME: THE FIELD (WARZONE) ---")
        count = int(self.num_players * self.spawn_mod)
        print(f"Generating {count} enemies...")
        input("Press Enter to start the wave...")
        
        for i in range(1, count + 1):
            # Hierarchy Logic
            roll = random.random()
            tier = EnemyTier.GRUNT
            if roll > 0.95: tier = EnemyTier.BOSS
            elif roll > 0.80: tier = EnemyTier.MINIBOSS
            
            self.print_enemy(tier, index=i)
            # Small delay for dramatic effect if list is huge, or remove for speed
            # time.sleep(0.05) 

        print("\n!!! COMMANDER APPROACHING !!!")
        input("Press Enter to spawn Final Boss...")
        self.print_enemy(EnemyTier.FINALBOSS)

    def run_building(self, max_rooms=15):
        num_rooms = random.randint(10, max_rooms)
        print(f"\n--- BIOME: BUILDING ({num_rooms} Rooms) ---")
        
        for i in range(1, num_rooms + 1):
            input(f"Press Enter to generate Room {i}...")
            
            size = random.choice(["Small", "Medium", "Huge"])
            
            # Loot Container Logic
            loot_txt = "None"
            if random.random() < (0.3 + self.loot_chance_mod):
                loot_txt = f"{random.choice(list(Rarity)).value} {random.choice(list(ItemType)).value}"
            
            # Encounter Logic
            encounter_txt = "No"
            enemies = []
            if random.random() < 0.4:
                encounter_txt = "YES"
                # Spawn small group
                num_enemies = random.randint(1, 3)
                if self.spawn_mod > 1: num_enemies *= 2 # Horde scaling
                
                print(f"--- Room {i}: {size} --- Loot Container: {loot_txt} --- Encounter: {encounter_txt}")
                print(f"Enemies appearing:")
                for e in range(num_enemies):
                     # Mostly grunts in rooms
                    tier = EnemyTier.GRUNT if random.random() < 0.9 else EnemyTier.MINIBOSS
                    self.print_enemy(tier, index=e+1)
            else:
                print(f"--- Room {i}: {size} --- Loot Container: {loot_txt} --- Encounter: {encounter_txt}")

        print("\n!!! FINAL ROOM REACHED !!!")
        input("Press Enter to spawn Final Boss...")
        self.print_enemy(EnemyTier.FINALBOSS)

    def run_village(self):
        print("\n--- BIOME: VILLAGE ---")
        try:
            roads = int(input("How many roads? "))
        except:
            roads = 2
            
        for r in range(1, roads + 1):
            print(f"\n=== ROAD {r} ===")
            buildings = random.randint(1, 4)
            
            # Road Encounter
            if random.random() < 0.25:
                print(">> ROAD EVENT: Random Encounter!")
                if random.random() < 0.5:
                    print(">> TYPE: Hostile Ambush")
                    self.print_enemy(EnemyTier.MINIBOSS)
                else:
                    rarity = random.choice(list(Rarity)).value
                    print(f">> TYPE: NPC Trader ({rarity})")
            
            for b in range(1, buildings + 1):
                print(f"\n   [Road {r} - Building {b}]")
                # Run building logic but smaller (1-5 rooms)
                self.run_building(max_rooms=5)

    def main_loop(self):
        self.setup()
        while True:
            print("\nSelect Biome for next Chapter:")
            print("1. Field (The Gauntlet)")
            print("2. Building (Dungeon Crawl)")
            print("3. Village (Exploration)")
            print("Q. Quit")
            choice = input("Choice: ").upper()
            
            if choice == '1': self.run_field()
            elif choice == '2': self.run_building()
            elif choice == '3': self.run_village()
            elif choice == 'Q': break
            else: print("Invalid choice.")

if __name__ == "__main__":
    app = DungeonGenerator()
    app.main_loop()
