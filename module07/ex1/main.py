from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck

print("=== DataDeck Deck Builder ===")

print("\nBuilding deck with different card types...")
my_deck = Deck()

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

creature = CreatureCard(**Creature)
spell = SpellCard(**Spell)
artifact = ArtifactCard(**Artifact)

#Add them All
my_deck.add_card(creature)
my_deck.add_card(spell)
my_deck.add_card(artifact)

# Show Deck Status
print(f"Deck stats: {my_deck.get_deck_stats()}\n")

#Drew first card
print(my_deck.draw_card())

#Drew second card
print(my_deck.draw_card())

#Drew Third card
print(my_deck.draw_card())

print("Polymorphism in action: Same interface, different card behaviors!")
