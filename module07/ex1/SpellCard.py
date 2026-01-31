from ex0.Card import Card


class SpellCard (Card):
    def __init__ (self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect = effect_type
        self.type = "Spell"

    def play (self, game_state: dict) -> dict:
        return game_state

    def resolve_effect (self, targets: list) -> dict:
        pass