from functools import reduce, partial, lru_cache, singledispatch
import operator


# Use operator
def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError("Unsupported operation")

    return reduce(lambda a, b: operations[operation](a, b), spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


def spell_dispatcher():
    """
    Returns a single-dispatch spell system.
    Handles int, str, and list types.
    """

    @singledispatch
    def cast(spell):
        raise TypeError(f"Unsupported spell type: {type(spell)}")

    # Damage spell: int
    @cast.register
    def _ (damage: int):
        return f"Dealt {damage} points of damage!"

    # Enchantment spell: str
    @cast.register
    def _ (enchant: str):
        return f"Casted {enchant} enchantment!"

    # Multi-cast spell: list
    @cast.register
    def _ (spells: list):
        results = []
        for s in spells:
            # recursively call the dispatcher on each element
            results.append(cast(s))
        return results

    return cast


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


# TESTING
if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
