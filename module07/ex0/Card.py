from abc import ABC, abstractmethod


class Card(ABC):
    def __init__ (self, name: str, cost: int, rarity: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play (self, game_state: dict) -> dict:
        pass

    def get_card_info (self) -> dict:
        info = {
            "name": getattr(self, "name", None),
            "cost": getattr(self, "cost", None),
            "rarity": getattr(self, "rarity", None),
        }
        if hasattr(self, "attack"):
            info["attack"] = self.attack
        if hasattr(self, "health"):
            info["health"] = self.health
        return info

    def is_playable (self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        else:
            return False