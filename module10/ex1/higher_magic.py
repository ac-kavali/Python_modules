#!/usr/bin/env python3

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        result = base_spell(*args, **kwargs)
        return result * multiplier

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results

    return sequence


# ===========================
# TESTING (like example output)
# ===========================
if __name__ == "__main__":

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage_spell() -> int:
        return 10

    def is_enemy(target: str) -> bool:
        return target == "Dragon"

    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    result = combined_spell("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print()

    print("Testing power amplifier...")
    amplified_spell = power_amplifier(damage_spell, 3)
    print(f"Original: {damage_spell()}, Amplified: {amplified_spell()}")
    print()

    print("Testing conditional caster...")
    conditional_spell = conditional_caster(is_enemy, fireball)
    print(conditional_spell("Dragon"))
    print(conditional_spell("Villager"))
    print()

    print("Testing spell sequence...")
    sequence_spell = spell_sequence([fireball, heal])
    print(sequence_spell("Knight"))
