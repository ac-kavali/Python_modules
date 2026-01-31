from ex0.CreatureCard import CreatureCard

print("=== DataDeck Deck Builder ===")

print("\nBuilding deck with different card types...")

Creature = {
    'name': 'Fire Dragon',
    'cost': 5,
    'rarity': 'Legendary',
    'attack': 7,
    'health': 5
    }

Spell = {
    'name': 'Lightning Bolt',
    'cost': 3,
    'rarity': 'Common',
    'effect_type': 'damage'
    }

Artifact = {'name': 'Mana Crystal',
            'cost': 2,
            'rarity': 'Common',
            'durability': 5,
            'effect': 'Permanent: +1 mana per turn'}

