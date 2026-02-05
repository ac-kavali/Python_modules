#!/usr/bin/env python3

from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    created with 2 spells(fun)
    then return their returns combined
    """
    def combined(target):
        result1 = spell1(target)
        result2 = spell2(target)
        return result1, result2

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    created with base damage_spell(fun), then return
    the base damage multiplied
    """
    def amplified():
        result = base_spell()
        return result * multiplier

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Created with Condition(True or False) and a spell(condition),
    then decide what return based on the condition.
    """
    def conditional(target):
        if condition(target):
            return spell(target)
        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    Created with a list of spells(fun),
    Then applies all spells to the target.
    """
    def sequence(target):
        results = []
        for spell in spells:
            results.append(spell(target))
        return results

    return sequence


# TESTING
if __name__ == "__main__":

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage_spell() -> int:
        return 10

    def is_enemy(target: str) -> bool:
        return target == "Dragon"

    # combine two functions to be applied to the Dragon:
    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    result = combined_spell("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")
    print()

    # take the original damage-spell and amplify it * multiplier
    print("Testing power amplifier...")
    amplified_spell = power_amplifier(damage_spell, 3)
    print(f"Original: {damage_spell()}, Amplified: {amplified_spell()}")
    print()

    # Creating function with the condition and spell
    print("Testing conditional caster...")
    conditional_spell = conditional_caster(is_enemy, fireball)
    # Then give it the target
    print(conditional_spell("Dragon")) # dragon is an enemy
    print(conditional_spell("Villager")) # Villager not, spell fizzled
    print()

    # Create function with spells to apply them to target
    print("Testing spell sequence...")
    sequence_spell = spell_sequence([fireball, heal])
    # Give it the target to create a sequence
    print(sequence_spell("Knight"))
