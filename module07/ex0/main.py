from ex0.CreatureCard import CreatureCard


print("=== DataDeck Card Foundation ===\n")

print("Testing Abstract Base Class Design:")

data =  {'name': 'Fire Dragon', 'cost': 5, 'rarity': 'Legendary', 'attack': 7, 'health': 5}
card = CreatureCard(**data)

print()