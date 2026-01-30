from ex0.Card import Card

class Creaturecard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")

        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict)-> dict:
        pass

    def attack_target (self, target) -> dict:
        pass