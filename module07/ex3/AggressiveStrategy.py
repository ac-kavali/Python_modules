from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        targets_attacked = []
        mana_used = 0
        damage_dealt = 0

        # play ONE card for simplicity
        if len(hand) > 0:
            card = hand[0]  # take first card
            hand.remove(card)  # remove from hand
            battlefield.append(card)

            cards_played.append(card.name)
            mana_used += card.cost
            damage_dealt += card.attack
            targets_attacked.append("Enemy Player")

        actions = {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets_attacked,
            "damage_dealt": damage_dealt
        }

        print("Actions:", actions)

        return actions

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        creatures = [t for t in available_targets if t != "Enemy Player"]
        player = [t for t in available_targets if t == "Enemy Player"]
        return creatures + player
