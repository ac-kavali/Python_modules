def check_temperature():
    try:
        temp_str = input("Enter a value: ")
        value = int(temp_str)
    except ValueError:
        print("The input isn't a number!")
        return None

    if value < 0:
        print("The temperature is too cold (min 0°C)!")
        return None
    if value > 40:
        print("The temperature is too hot (max 40°C)!")
        return None
    print(f"Temperature {value}°C is perfect for plants!")
    return value



check_temperature()
