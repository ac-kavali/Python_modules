from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    """
    Sort artifacts by power (descending).
    """
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    """
    Filter mages whose power is >= min_power.
    """
    return list(
        filter(lambda mage: mage["power"] >= min_power, mages)
    )


def spell_transformer(spells: List[str]) -> List[str]:
    """
    Add '* ' prefix and ' *' suffix to spell names.
    """
    return list(
        map(lambda spell: f"* {spell} *", spells)
    )


def mage_stats(mages: List[Dict]) -> Dict:
    """
    Compute max, min, and average mage power.
    """
    powers = list(map(lambda mage: mage["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


if __name__ == "__main__":

    # ================DATA BLOCK=========================================
    artifacts = [
            {'name': 'Fire Staff', 'power': 92, 'type': 'focus'},
            {'name': 'Light Prism', 'power': 33, 'type': 'focus'},
            {'name': 'Crystal Orb', 'power': 85, 'type': 'relic'},
            {'name': 'Lightning Rod', 'power': 23, 'type': 'accessory'},
    ]

    mages = [
        {'name': 'Kai', 'power': 68, 'element': 'earth'},
        {'name': 'Riley', 'power': 60, 'element': 'water'},
        {'name': 'Riley', 'power': 97, 'element': 'wind'},
        {'name': 'Storm', 'power': 91, 'element': 'water'},
        {'name': 'Morgan', 'power': 61, 'element': 'light'}
    ]

    spells = ['meteor', 'blizzard', 'tornado', 'tsunami']
    # ====================================================================

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f'{sorted_artifacts[0]["name"]}({sorted_artifacts[0]["power"]} '
          f'power) comes before {sorted_artifacts[1]["name"]}'
          f'({sorted_artifacts[1]["power"]} power)')

    print("\nTesting Spell Transformer...")
    formated_spells = spell_transformer(spells)
    for spell in formated_spells:
        print(spell + " ", end="")



























