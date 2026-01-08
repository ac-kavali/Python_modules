def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def print_recursive(start, end):
        if start > end:
            return
        print(start)
        print_recursive(start + 1, end)

    print_recursive(1, days)
    print("Harvest time!")

ft_count_harvest_recursive()