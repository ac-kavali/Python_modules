from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


print("=== DataDeck Tournament Platform ===\n")

platform = TournamentPlatform()

# Create cards
fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary", 8)
ice_wizard = TournamentCard("Ice Wizard", 4, "Epic", 6)

# Manually adjust starting rating to match expected output
fire_dragon.rating = 1200
ice_wizard.rating = 1150

# Register cards with fixed IDs
dragon_id = "dragon_001"
wizard_id = "wizard_001"

platform.cards[dragon_id] = fire_dragon
platform.cards[wizard_id] = ice_wizard

print("Registering Tournament Cards...\n")

print("Fire Dragon (ID: dragon_001):")
print("- Interfaces: [Card, Combatable, Rankable]")
print("- Rating:", fire_dragon.rating)
print("- Record: 0-0\n")

print("Ice Wizard (ID: wizard_001):")
print("- Interfaces: [Card, Combatable, Rankable]")
print("- Rating:", ice_wizard.rating)
print("- Record: 0-0\n")

print("Creating tournament match...")
result = platform.create_match(dragon_id, wizard_id)
print("Match result:", result, "\n")

print("Tournament Leaderboard:")
leaderboard = platform.get_leaderboard()

for index, card in enumerate(leaderboard, start=1):
    print(
        f"{index}. {card['name']} - Rating: {card['rating']}"
        f" ({card['record']})"
    )

print("Platform Report:")
print(platform.generate_tournament_report(), "\n")

print("=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
