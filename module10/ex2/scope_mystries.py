#!/usr/bin/env python3


def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    return lambda item_name: f"{enchantment_type} {item_name}"


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key: str, value):
        nonlocal memory
        memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


# ======================
# TESTING LIKE SUBJECT
# ======================
if __name__ == "__main__":

    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    print()

    print("Testing spell accumulator...")
    accumulator = spell_accumulator(50)
    print(accumulator(10))
    print(accumulator(20))
    print(accumulator(5))
    print()

    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("spell", "Fireball")
    vault["store"]("power", 99)

    print(vault["recall"]("spell"))
    print(vault["recall"]("power"))
    print(vault["recall"]("unknown"))
