class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def details(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")

    def growth_stats(self, days):
        self.height += 1.5 * days
        self.age += days
        self.details()


marijuana = Plant("Marijuana", 3, 1)

print("=== Day 1 ===")
marijuana.details()

print("=== Day 2 ===")
marijuana.growth_stats(1)

print("=== Day 5 ===")
marijuana.growth_stats(3)

print("=== Day 7 ===")
marijuana.growth_stats(2)

print(f"Growth this week: +{7 * 1.5} cm")
