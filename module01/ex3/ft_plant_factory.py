class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"Created: {self.name} ({self.height} cm, {self.age} days)"


plants_data = [
    ("Rose", 12, 150),
    ("Lotus", 15, 678),
    ("Marijuana", 97, 300),
    ("Vanilla", 18, 89),
    ("Coca", 30, 78),
]

plants = []

print("=== Plant Factory Output ===")
for name, height, age in plants_data:
    new_plant = Plant(name, height, age)
    print(new_plant)
    plants.append(new_plant)

print(f"\nTotal plant created: {len(plants)}")
