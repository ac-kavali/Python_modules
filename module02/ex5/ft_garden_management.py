class GardenError(Exception):
    pass


class PlantNameError(ValueError):
    pass


class WaterLevelError(ValueError):
    pass


class SunlightError(ValueError):
    pass


def check_plant_name(name):
    if len(name) == 0:
        raise PlantNameError("Plant name cannot be empty!")


def check_water_level(level):
    if level < 4:
        raise WaterLevelError(f"Water level {level} is too low (min 0)")
    if level > 10:
        raise WaterLevelError(f"Water level {level} is too high (max 10)")


def check_sunlight_hours(hours):
    if hours < 2:
        raise SunlightError(f"Sunlight hours {hours} is too low (min 2)")
    if hours > 12:
        raise SunlightError(f"Sunlight hours {hours} is too high (max 12)")


class Plant:
    def __init__(self, name):
        self.name = name


class GardenManager:
    def __init__(self, owner_name, tank_level):
        self.owner_name = owner_name
        self.plants = []
        self.tank_level = tank_level

    def add_plant(self, name):
        try:
            check_plant_name(name)
            plant = Plant(name)
            self.plants.append(plant)
            print(f"Added {name} successfully")
        except PlantNameError as e:
            print(f"Error adding plant: {e}")

    def water_plants (self):
        try:
            if self.tank_level < 6:
                raise GardenError("Not enough water in tank")

            print("Opening watering system")
            for plant in self.plants:
                self.tank_level -= 2
                print(f"Watering {plant.name} - success")

        except GardenError as error:
            print(f"Caught GardenError: {error}")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        try:
            check_plant_name(plant_name)
            check_water_level(water_level)
            check_sunlight_hours(sunlight_hours)
            print(f"{plant_name}: healthy "
                  f"(water: {water_level},"
                  f" sun: {sunlight_hours})")

        except (PlantNameError, WaterLevelError, SunlightError) as e:
            print(f"Error checking {plant_name}: {e}")


if __name__ == "__main__":
    print("=== Garden Management System ===")

    manager = GardenManager("Ahmed", 6)

    print("\nAdding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 6)

    print("\nTesting error recovery...")
    manager.water_plants()

    print("\nGarden management system test complete!")
