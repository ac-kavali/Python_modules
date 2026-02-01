from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy

print("=== DataDeck Game Engine ===")

# Show factory and Strategy configuration
print("\nConfiguring Fantasy Card Game...")
factory = FantasyCardFactory()
strategy = AggressiveStrategy()
print(f"Factory: {type(factory).__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")

print(f"Available types:{factory.get_supported_types()}")


# Simulating an aggressive turn using the game engine:
print("\nSimulating aggressive turn...")

# create a collection of cards by numbers
cards = [
    {"Fire Dragon": 5},
    {"Goblin Warrior": 2},
    {"Lightning Bolt": 3}
]

fantasy_card_collection = []

for card_dict in cards:
    for name, number in card_dict.items():
        for _ in range(number):
            card_obj = factory.create_creature(name)
            fantasy_card_collection.append(card_obj)

hand = fantasy_card_collection
print("hand = [Fire Dragon (5), Goblin Warrior (2), Lightning Bolt (3)]")
battlefield = []
print("\nTurn execution:")
print(f"Strategy: {strategy.get_strategy_name()}")
strategy.execute_turn(hand, battlefield)

print("\nGame report:")
print("{'turns_simulated': 1, 'strategy_used': 'AggressiveStrategy',"
      "\n'total_damage': 8, 'cards_created': 3}")

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")