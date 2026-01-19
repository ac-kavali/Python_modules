class GardenManager:
    total_gardens = 0

    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0
            self.plant_types = {
                "regular": 0,
                "flowering": 0,
                "prize": 0,
            }

        def record_plant_addition(self, plant):
            self.plants_added += 1

            if hasattr(plant, "prize_points"):
                self.plant_types["prize"] += 1
            elif hasattr(plant, "flower_color"):
                self.plant_types["flowering"] += 1
            else:
                self.plant_types["regular"] += 1

        def record_growth(self, amount):
            self.total_growth += amount

        def get_summary(self):
            return (
                f"Plants added: {self.plants_added}, "
                f"Total growth: {self.total_growth}cm\n"
                f"Plant types: {self.plant_types['regular']} regular, "
                f"{self.plant_types['flowering']} flowering, "
                f"{self.plant_types['prize']} prize flowers"
            )

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        self.stats.record_plant_addition(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_plants_grow(self):
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            growth = plant.grow()
            self.stats.record_growth(growth)

    def calculate_score(self):
        total = 0
        for plant in self.plants:
            total += plant.height
            if hasattr(plant, "prize_points"):
                total += plant.prize_points
        return total

    def print_report(self):
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_description()}")
        print(self.stats.get_summary())

    @classmethod
    def create_garden_network(cls, owners):
        gardens = []
        for owner in owners:
            gardens.append(cls(owner))
        return gardens

    @staticmethod
    def validate_height(height):
        return 0 <= height <= 1000


class Plant:
    def __init__(self, name, height=100):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")
        return 1

    def get_description(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    def __init__(self, name, height=25, flower_color="white"):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = True

    def get_description(self):
        base_desc = super().get_description()
        bloom_status = (
            "blooming" if self.is_blooming else "not blooming"
        )
        return (
            f"{base_desc}, {self.flower_color} flowers "
            f"({bloom_status})"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name,
        height=50,
        flower_color="yellow",
        prize_points=10,
    ):
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def get_description(self):
        base_desc = super().get_description()
        return f"{base_desc}, Prize points: {self.prize_points}"


def show_garden_scores(garden1, garden2):
    score1 = garden1.calculate_score()
    score2 = garden2.calculate_score()
    print(
        f"Garden scores - {garden1.owner_name}: {score1}, "
        f"{garden2.owner_name}: {score2}"
    )


def main():
    print("=== Garden Management System Demo ===")

    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    tulip = FloweringPlant("Tulip", 20, "pink")
    pine = Plant("Pine Tree", 70)

    bob_garden.add_plant(tulip)
    bob_garden.add_plant(pine)

    alice_garden.help_plants_grow()
    alice_garden.print_report()

    print(
        f"\nHeight validation test: "
        f"{GardenManager.validate_height(oak.height)}"
    )

    print()
    show_garden_scores(alice_garden, bob_garden)

    print(
        f"\nTotal gardens managed: "
        f"{GardenManager.total_gardens}"
    )


if __name__ == "__main__":
    main()
