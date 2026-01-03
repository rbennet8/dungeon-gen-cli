import random
import time

def generate_character(level: int):
    # 1. Base Stats (Everyone starts with a baseline)
    strength = 3
    dexterity = 3
    intelligence = 3
    
    # 2. Distribute Points based on Level
    # Logic: Characters get approx 2-3 stat points per level to distribute randomly
    # We add an initial pool of 10 points so Level 1 chars aren't helpless
    points_to_distribute = 10 + int(level * 2.5) 
    
    for _ in range(points_to_distribute):
        roll = random.randint(1, 3)
        if roll == 1: strength += 1
        elif roll == 2: dexterity += 1
        elif roll == 3: intelligence += 1

    # 3. Calculate Vitals (Derived from Level + Random Stats)
    # HP is influenced slightly by Strength
    base_hp = 20 + (level * 6)
    hp = base_hp + (strength * 2) + random.randint(-5, 5)
    
    # Mana is influenced slightly by Intelligence
    base_mana = 10 + (level * 3)
    mana = base_mana + (intelligence * 2) + random.randint(-5, 5)
    
    # Armor scales with Level + Dexterity bonus
    armor = 10 + (level // 2) + (dexterity // 3)

    # 4. Trait Roll (The 1-3 number you requested)
    trait_count = random.randint(1, 3)

    # --- OUTPUT ---
    print(f"\n--- Random Character (Level {level}) ---")
    print(f"HP: {hp}  |  Mana: {mana}  |  Armor: {armor}")
    print(f"Str: {strength}  |  Dex: {dexterity}  |  Int: {intelligence}")
    print(f"Traits to Roll: {trait_count}")

def main():
    print("--- RANDOM STAT GENERATOR ---")
    while True:
        try:
            val = input("\nHow many characters? (Q to quit): ")
            if val.lower() == 'q': break
            num_chars = int(val)
            
            level = int(input("Target Level: "))
            
            print(f"\nRolling {num_chars} characters...")
            # Small delay just so it feels like it's 'thinking'
            time.sleep(0.3) 
            
            for _ in range(num_chars):
                generate_character(level)
                
        except ValueError:
            print("Please enter valid integers.")

if __name__ == "__main__":
    main()
