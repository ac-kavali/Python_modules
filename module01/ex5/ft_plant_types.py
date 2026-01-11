class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!\n")

    def flower_details(self):
        print(
            f"{self.name} (Flower): {self.height} cm, "
            f"{self.age} days, {self.color} color"
        )
        self.bloom()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides 10 square meters of shade\n")

    def tree_details(self):
        print(
            f"{self.name} (Tree): {self.height} cm, "
            f"{self.age} days, {self.trunk_diameter} cm diameter"
        )
        self.produce_shade()


class Vegetable(Plant):
    def __init__(
        self,
        name,
        height,
        age,
        harvest_season,
        nutritional_value,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def vegetable_details(self):
        print(
            f"{self.name} (Vegetable): {self.height} cm, "
            f"{self.age} days, {self.harvest_season} harvest"
        )
        print(
            f"{self.name} is rich in {self.nutritional_value}\n"
        )


rose = Flower("Rose", 20, 30, "red")
sunflower = Flower("Sunflower", 100, 50, "yellow")

bamboo = Tree("Bamboo", 1500, 5002, 70)
coconut = Tree("Coconut", 10000, 2100, 20)

carrot = Vegetable("Carrot", 30, 60, "summer", "vitamin A")
potato = Vegetable("Potato", 60, 23, "summer", "Omega 3")

print("=== Garden Plant Types ===\n")

rose.flower_details()
coconut.tree_details()
potato.vegetable_details()
