def test_error_types(error):
    err_type = type(error).__name__
    if err_type == 'ValueError':
        print("Caught ValueError: invalid literal for int()\n")

    if err_type == 'ZeroDivisionError':
        print("Caught ZeroDivisionError: division by zero\n")

    if err_type == 'FileNotFoundError':
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    if err_type == 'KeyError':
        print("Caught KeyError: 'missing\_plant'")

def garden_operations():
    my_dict = {'name': "KV", 'age': 19}
    try:
        print("Testing ValueError...")
        value = int("abc")
    except Exception as e:
        test_error_types(e)

    try:
        print("Testing ZeroDivisionError...")
        value = 10 / 0
    except Exception as e:
        test_error_types(e)

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except Exception as e:
        test_error_types(e)

    try:
        print("Testing KeyError...")
        print(my_dict["plant"])
    except Exception as e:
        test_error_types(e)



if __name__ == '__main__':
    garden_operations()