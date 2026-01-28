from alchemy import elements


def healing_potion():
    return (f"Healing potion brewed with {elements.create_fire()} "
            f"and {elements.create_water()}")


def strength_potion():
    return (f"Strength potion brewed with {elements.create_earth()} "
            f"and {elements.create_fire()}")


def invisibility_potion():
    return (f"Invisibility potion brewed with {elements.create_air()} "
            f"and {elements.create_water()}")


def wisdom_potion():
    return (f"Wisdom potion brewed with all elements: {elements.create_fire()},"
            f"{elements.create_water()}, {elements.create_earth()}, "
            f"{elements.create_air()} ")
