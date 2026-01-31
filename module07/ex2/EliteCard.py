from ex0.Card import Card
from ex2.Magical import Magical
from ex2.Combatable import Combatable


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name, cost: int, rarity: str, health: int):
        super().__init__(name, cost, rarity)
        self.health = health
        self.cost = cost

    def play(self, game_state: dict) -> dict:
        pass

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.get("name"),
            "damage": target.get("damage"),
            "combat_type": target.get("combat_type")
        }

    def defend(self, incoming_damage: int) -> dict:
        defense_pow = 3
        still_alive = self.health - (incoming_damage - defense_pow) > 0
        return {
            "defender": self.name,
            "damage_taken": incoming_damage - defense_pow,
            "damage_blocked": defense_pow,
            "still_alive": still_alive
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4
        }

    def channel_mana(self, amount: int) -> dict:
        mana = 10
        return {
            "channeled": amount,
            "total_mana": mana - amount
        }

    def get_magic_stats(self) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass
