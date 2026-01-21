class plant_name_error(ValueError):
    pass

class water_level_error(ValueError):
    pass

class sunlight_error(ValueError):
    pass

def check_plant_name(name):
    if len(name) == 0:
        raise plant_name_error("Error: Plant name cannot be empty!")
    else:
        pass

def check_water_level(level):
    if level < 0:
        raise water_level_error(f"Water level {level} is too low (min 0)")
    elif level > 10:
        raise water_level_error(f"Water level {level} is too hight (max 10)")
    else:
        pass

def check_sunlight_hours(hours):
    if hours < 2:
        raise sunlight_error(f"Error: Sunlight hours {hours} is too low (min 2)")
    if hours > 12:
        raise sunlight_error(f"Error: Sunlight hours {hours} is too low (min 2)")

def check_plant_health(plant_name, water_level, sunlight_hours):
    print("=== Garden Plant Health Checker ===\n")
    try:
        check_plant_name(plant_name)
    except Exception as e:
        print(e)
    try:
        check_water_level(water_level)
    except Exception as e:
        print(e)
    try:
        check_sunlight_hours(sunlight_hours)
    except Exception as e:
        print(e)

    print

print("Testing good values...")

