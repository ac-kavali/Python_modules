
def mage_counter() -> callable:
    count = 0
    """
    Once the function created the count initialization being executed
    the counter(fun) takes the control 
    """
    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power
    """
    Once ... total is initialized and each accumulator(fun) being
    called with an amount, it be added to the total
    """
    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    """
    Lambda do the role of another function that takes item name
    and return it like enchantment + item name
    """
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, callable]:
    memory = {}
    """
    This fun return a dict of functions
    used like func[fun_name](arguments)
    """
    def store(key: str, value):
        nonlocal memory
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


# TESTING LIKE SUBJECT
if __name__ == "__main__":

    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    print()

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print()
