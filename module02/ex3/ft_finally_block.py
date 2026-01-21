def water_plants(plant_list):
    print("Opening watering system")
    err = False
    try:
        for i in range(3):
            print(f"Watering {plant_list[i]}")
    except IndexError:
        print("Error: Cannot water None - invalid plant!")
        err = True
    finally:
        print("Closing watering system (cleanup)")
        if err:
            print("\nCleanup always happens, even with errors!")
        else:
            print("Watering completed successfully!")


print("=== Garden Watering System ===\n")
print("\nTesting Normal watering...")
plant_list = ["tomato", "lettuce", "carrots"]
water_plants(plant_list)

print("\nTesting with Error...")
plant_list = ["tomato"]
water_plants(plant_list)
