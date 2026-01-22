class PlantNameError(ValueError):
    pass


class WaterLevelError(ValueError):
    pass


class SunlightError(ValueError):
    pass


def check_plant_name(name):
    if len(name) == 0:
        raise PlantNameError("Error: Plant name cannot be empty!")


def check_water_level(level):
    if level < 0:
        raise WaterLevelError(f"Water level {level} is too low (min 0)")
    elif level > 10:
        raise WaterLevelError(f"Water level {level} is too high (max 10)")


def check_sunlight_hours(hours):
    if hours < 2:
        raise SunlightError(f"Sunlight hours {hours} is too low (min 2)")
    if hours > 12:
        raise SunlightError(f"Sunlight hours {hours} is too high (max 12)")


def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        check_plant_name(plant_name)
        check_water_level(water_level)
        check_sunlight_hours(sunlight_hours)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Plant {plant_name} is healthy!")


print("=== Garden Plant Health Checker ===\n")

print("Testing good values...")
check_plant_health("Tomato", 7, 5)

print("\nTesting empty plant name...")
check_plant_health("", 7, 5)

print("\nTesting bad water level...")
check_plant_health("Tomato", 15, 5)

print("\nTesting bad sunlight hours...")
check_plant_health("Tomato", 7, 0)

print("\nAll error raising tests completed!")
