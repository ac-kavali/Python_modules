from ex3.GameStrategy import GameStrategy

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets (self, available_targets: list) -> list:
        creatures = [t for t in available_targets if t != "Enemy Player"]
        player = [t for t in available_targets if t == "Enemy Player"]
        return creatures + player
