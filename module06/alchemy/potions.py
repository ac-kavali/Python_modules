from alchemy import elements

def healing_potion():
    return f"Healing potion brewed with {elements.create_fire()} and {elements.create_water()}"

def strength_potion():
    return f"Strength potion brewed with {elements.create_earth()} and {elements.create_fire()}"

def invisibility_potion():
    return "Invisibility potion brewed with [air_result] and [water_result]"

def wisdom_potion():
    return "Wisdom potion brewed with all elements: [all_four_results]"
