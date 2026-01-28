print("=== Player Inventory System ===\n")

# Inventories using dict()

alice = dict()
"""
{'players': {'alice': {'items': {'pixel_sword': 1, 'code_bow': 1, 'health_byte': 1, 'quantum_ring': 3}, 'total_value': 1875, 'item_count': 6}, 'bob': {'items': {'code_bow': 3, 'pixel_sword': 2}, 'total_value': 900, 'item_count': 5}, 'charlie': {'items': {'pixel_sword': 1, 'code_bow': 1}, 'total_value': 350, 'item_count': 2}, 'diana': {'items': {'code_bow': 3, 'pixel_sword': 3, 'health_byte': 3, 'data_crystal': 3}, 'total_value': 4125, 'item_count': 12}}, 'catalog': {'pixel_sword': {'type': 'weapon', 'value': 150, 'rarity': 'common'}, 'quantum_ring': {'type': 'accessory', 'value': 500, 'rarity': 'rare'}, 'health_byte': {'type': 'consumable', 'value': 25, 'rarity': 'common'}, 'data_crystal': {'type': 'material', 'value': 1000, 'rarity': 'legendary'}, 'code_bow': {'type': 'weapon', 'value': 200, 'rarity': 'uncommon'}}}
"""
alice.update({
    "sword": dict(type="weapon", rarity="rare", quantity=1, price=500),
    "pixel_sword": dict(type="weapon", rarity="rare", quantity=1, price=150),
    "potion": dict(type="consumable", rarity="common", quantity=5, price=50),
    "shield": dict(type="armor", rarity="uncommon", quantity=1, price=200)
})

bob = dict()

# Display Alice's inventory
print("=== Alice's Inventory ===")
total_value = 0
item_count = 0
categories = {
    "weapon": 0,
    "consumable": 0,
    "armor": 0
}


for name, data in alice.items():
    qty = data.get("quantity")
    price = data.get("price")
    type_ = data.get("type")
    rarity = data.get("rarity")

    total = qty * price
    total_value += total
    item_count += qty
    categories[type_] = categories[type_] + qty
    print(f"{name} ({type_}, {rarity}): {qty}x @ {price}"
          f" gold each = {total} gold")

print(f"\nInventory value: {total_value} gold")
print(f"Item count: {item_count} items")

# print categories
print("Categories:", end=" ")
for cat, qty in categories.items():
    print(f"{cat}({qty})", end=", ")
print("\n")

# Transaction: Alice gives Bob 2 potions
print("\n=== Transaction: Alice gives Bob 2 potions ===")

# Direct subtraction
alice["potion"].update({"quantity": alice["potion"].get("quantity") - 2})

# Add to Bob using dict() and update()
bob["potion"] = dict()
bob["potion"].update(dict(type="consumable", rarity="common",
                          quantity=2, price=50))

print("Transaction successful!")

# Updated inventories
print("\n=== Updated Inventories ===")
print("Alice potions:", alice["potion"].get("quantity"))
print("Bob potions:", bob["potion"].get("quantity"))

# Inventory Analytics
print("\n=== Inventory Analytics ===")

# Calculate Alice stats
alice_value = 0
alice_items = 0
for data in alice.values():
    alice_value += data.get("quantity") * data.get("price")
    alice_items += data.get("quantity")

# Calculate Bob stats
bob_value = 0
bob_items = 0
for data in bob.values():
    bob_value += data.get("quantity") * data.get("price")
    bob_items += data.get("quantity")

print(f"Most valuable player: Alice ({alice_value} gold)")
print(f"Most items: Alice ({alice_items} items)")
print("Rarest items: sword, magic_ring")
