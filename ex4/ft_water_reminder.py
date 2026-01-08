def ft_water_reminder():
    last_one = int(input("Days since last  watering: "))

    if last_one <= 2:
        print("Plants are fine.")
    else:
        print("Water the plants!")
