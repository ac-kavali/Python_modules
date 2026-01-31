from ex0.CreatureCard import CreatureCard


print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:")

data = {
    'name': 'Fire Dragon',
    'cost': 5,
    'rarity': 'Legendary',
    'attack': 7,
    'health': 5
         }
card = CreatureCard(**data)

print("CreatureCard Info:")
print(card.get_card_info())

# Test if Playable
print("\nPlaying Fire Dragon with 6 mana available:")
print(f"Playable: {card.is_playable(6)}")


# Test Play Function With Game State
game_state = {
    'card_played': card.name,
    'mana_used': {card.cost},
    'effect': 'Creature summoned to battlefield'
    }
print(f"Play result: {card.play(game_state)}")

# Test Attack Function With Target Information
print("\nFire Dragon attacks Goblin Warrior:")
print(card.attack_target({"name": "Goblin Warrior", "health": 6}))

# Testing Insufficient MANA
print("\nTesting insufficient mana (3 available):")
print(f"Playable: {card.is_playable(3)}")

print("\nAbstract pattern successfully demonstrated!")
