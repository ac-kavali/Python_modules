from ex2.EliteCard import EliteCard


print("=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

# perform an attack (Create two cards The Attacker and Defender)
card = EliteCard("Arcane Warrior", 4, "Legendary")


print(f"\nAttack result{card.attack({"name": "Enemy", "damage": 5, "combat_type": "melee"})}")
print(f"\nDefense result result{card.defend({"name": "Enemy", "damage": 5, "combat_type": "melee"})}")


#{'attacker': 'Fire Dragon', 'target': 'Goblin Warrior', 'damage_dealt': 7, 'combat_resolved': True}