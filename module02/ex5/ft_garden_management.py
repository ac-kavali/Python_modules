class GardenError(Exception):
    pass


class PlantNameError(ValueError):
    pass


class WaterLevelError(ValueError):
    pass


class SunlightError(ValueError):
    pass


class Plant:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def check_plant_name(name):
        if len(name) == 0:
            raise PlantNameError("Plant name cannot be empty!")

    @staticmethod
    def check_water_level(level):
        if level < 0:
            raise WaterLevelError(f"Water level {level} is too low (min 0)")
        if level > 10:
            raise WaterLevelError(f"Water level {level} is too high (max 10)")

    @staticmethod
    def check_sunlight_hours(hours):
        if hours < 2:
            raise SunlightError(f"Sunlight hours {hours} is too low (min 2)")
        if hours > 12:
            raise SunlightError(f"Sunlight hours {hours} is too high (max 12)")



class GardenManager:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []

    def add_plant(self, name):
        try:
            Plant.check_plant_name(name)
            plant = Plant(name)
            self.plants.append(plant)
            print(f"Added {name} successfully")
        except PlantNameError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise GardenError("Not enough water in tank")

            for plant in self.plants:
                print(f"Watering {plant.name} - success")

        except GardenError as e:
            print(f"Caught GardenError: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        try:
            Plant.check_plant_name(plant_name)
            Plant.check_water_level(water_level)
            Plant.check_sunlight_hours(sunlight_hours)
            print(f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})")

        except (PlantNameError, WaterLevelError, SunlightError) as e:
            print(f"Error checking {plant_name}: {e}")



if __name__ == "__main__":
    print("=== Garden Management System ===")

    manager = GardenManager("Ahmed")

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("Watering plants...")
    manager.water_plants()

    print("Checking plant health...")
    manager.check_plant_health("tomato", 5, 8)
    manager.check_plant_health("lettuce", 15, 6)

    print("Testing error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")
