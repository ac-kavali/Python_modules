from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    def __init__ (self):
        self.strategy = None
        self.factory = None

    def configure_engine (self, factory: CardFactory, strategy: GameStrategy) -> None:
        # assign dependencies
        self.factory = factory
        self.strategy = strategy

        # print configuration info
        print("=== Engine Configuration ===")
        print(f"CardFactory: {factory.__class__.__name__}")
        print(f"GameStrategy: {strategy.__class__.__name__}")
        print("Engine configured successfully.")

    def simulate_turn (self) -> dict:
        if not hasattr(self, "factory") or not hasattr(self, "strategy"):
            raise RuntimeError("Engine is not configured. Call configure_engine() first.")

        # 1. Create cards for this turn
        cards = self.factory.create_cards()

        # 2. Strategy decides what to do
        chosen_card = self.strategy.choose_card(cards)

        # 3. Simulate playing the card
        result = {
            "available_cards": [card.name for card in cards],
            "played_card": chosen_card.name,
            "cost": chosen_card.cost,
            "rarity": chosen_card.rarity,
        }

        # 4. Print turn summary
        print("=== Turn Simulation ===")
        print(f"Available cards: {result['available_cards']}")
        print(f"Played card: {result['played_card']}")
        print(f"Cost: {result['cost']} | Rarity: {result['rarity']}")

        return result

    def get_engine_status (self) -> dict:
        return {
            "configured": hasattr(self, "factory") and hasattr(self, "strategy"),
            "card_factory": (
                self.factory.__class__.__name__
                if hasattr(self, "factory") else None
            ),
            "strategy": (
                self.strategy.__class__.__name__
                if hasattr(self, "strategy") else None
            )
        }
