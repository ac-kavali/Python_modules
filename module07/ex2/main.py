from ex2.EliteCard import EliteCard


print("=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

# perform an attack (Create two cards The Attacker and Defender)
print("\nPlaying Arcane Warrior (Elite Card:\n")
card = EliteCard("Arcane Warrior", 4, "Legendary", 6)

target = {'name': 'Enemy', 'damage': 5, 'combat_type': 'melee'}
print(f"\nAttack result{card.attack(target)}")
print(f"Defense result result{card.defend(5)}")

print(f"\nSpell cast: {card.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
print(f"Mana channel:{card.channel_mana(3)}")

print("\nMultiple interfaces implementation successful!")
