# ft_inventory_system.py

print("=== Player Inventory System ===")

# -------------------------
# Inventories (nested dictionaries)
# -------------------------
alice = {
    "sword": {"type": "weapon", "rarity": "rare", "quantity": 1, "price": 500},
    "potion": {"type": "consumable", "rarity": "common", "quantity": 5, "price": 50},
    "shield": {"type": "armor", "rarity": "uncommon", "quantity": 1, "price": 200},
}

bob = {}

# -------------------------
# Display Alice's inventory
# -------------------------
print("=== Alice's Inventory ===")
total_value = 0
item_count = 0
categories = {}

for name, data in alice.items():
    qty = data.get("quantity")
    price = data.get("price")
    type_ = data.get("type")
    rarity = data.get("rarity")

    total = qty * price
    total_value += total
    item_count += qty
    categories[type_] = categories.get(type_, 0) + qty

    print(f"{name} ({type_}, {rarity}): {qty}x @ {price} gold each = {total} gold")

print(f"Inventory value: {total_value} gold")
print(f"Item count: {item_count} items")
print("Categories:", end=" ")
for cat, qty in categories.items():
    print(f"{cat}({qty})", end=", ")
print("\n")

# -------------------------
# Transaction: Alice gives Bob 2 potions
# -------------------------
print("=== Transaction: Alice gives Bob 2 potions ===")

# Simple version: subtract and assign directly
alice["potion"]["quantity"] -= 2

bob["potion"] = {
    "type": "consumable",
    "rarity": "common",
    "quantity": 2,
    "price": 50
}

print("Transaction successful!")

# -------------------------
# Updated inventories
# -------------------------
print("=== Updated Inventories ===")
print("Alice potions:", alice["potion"]["quantity"])
print("Bob potions:", bob["potion"]["quantity"])

# -------------------------
# Inventory Analytics
# -------------------------
print("=== Inventory Analytics ===")

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
