from ex2.EliteCard import EliteCard


print("=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

# perform an attack (Create two cards The Attacker and Defender)
attacker = EliteCard("Crown of Kings", 4, "Legendary", 10, 2)
defender = EliteCard("Ice Shard", 4, "Legendary", 10, 2)

attacker.attack()

