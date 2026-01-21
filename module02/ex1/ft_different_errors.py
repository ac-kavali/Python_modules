def garden_operations():
    print("== Garden Error Types Demo ===\n")
    test_error_types()
    print("All error types tested successfully!")


def error_handler(error):
    err_type = type(error).__name__

    if err_type == 'ValueError':
        print("Caught ValueError: invalid literal for int()\n")

    if err_type == 'ZeroDivisionError':
        print("Caught ZeroDivisionError: division by zero\n")

    if err_type == 'FileNotFoundError':
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    if err_type == 'KeyError':
        print("Caught KeyError: 'missing_plant'\n")


def test_error_types():
    my_dict = {'name': "KV", 'age': 19}

    try:
        print("Testing ValueError...")
        int("abc")
    except Exception as e:
        error_handler(e)

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except Exception as e:
        error_handler(e)

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except Exception as e:
        error_handler(e)

    try:
        print("Testing KeyError...")
        print(my_dict["plant"])
    except Exception as e:
        error_handler(e)

    try:
        print("Testing multiple errors together...")
        int("abc")
        5 / 0
    except Exception:
        print("Caught an error, but program continues!\n")


if __name__ == '__main__':
    garden_operations()
