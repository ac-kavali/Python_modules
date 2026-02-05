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


# Optional quick test (allowed: print)
if __name__ == "__main__":
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "magic"},
        {"name": "Fire Staff", "power": 92, "type": "fire"},
    ]

    mages = [
        {"name": "Aelin", "power": 70, "element": "fire"},
        {"name": "Drake", "power": 95, "element": "lightning"},
        {"name": "Nyx", "power": 40, "element": "shadow"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Sorted artifacts:", artifact_sorter(artifacts))
    print("Filtered mages:", power_filter(mages, 60))
    print("Transformed spells:", spell_transformer(spells))
    print("Mage stats:", mage_stats(mages))






























