from ex0.Card import Card


class ArtifactCard(Card):
    def __init__ (self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect
        self.type = "Artifact"

    def play (self, game_state: dict) -> dict:
        return game_state

    def activate_ability(self) -> dict:
        pass



