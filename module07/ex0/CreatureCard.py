from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.type = "Creature"

        if not isinstance(attack, int) or attack <= 0:
            self.attack = 0
            print("attack must be a positive integer <default=0>!")
        else:
            self.attack = attack

        if not isinstance(health, int) or health <= 0:
            self.health = 0
            print("health must be a positive integer <default=0>!")
        else:
            self.health = health

    def play(self, game_state: dict) -> dict:
        return game_state

    def attack_target(self, target) -> dict:
        combat_result = False
        if target["health"] <= self.attack:
            combat_result = True
        return {
            "attacker": self.name,
            "target": target.get("name"),
            "damage_dealt": self.attack,
            "combat_resolved": combat_result,
        }
