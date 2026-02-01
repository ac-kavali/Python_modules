class TournamentPlatform:

    def __init__(self):
        self.cards = {}
        self.matches_played = 0

    def register_card(self, card) -> str:
        card_id = card.name.lower().replace(" ", "_")
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        self.matches_played += 1

        # VERY simple winner logic
        if card1.attack_power >= card2.attack_power:
            winner = card1
            loser = card2
            winner_id = card1_id
            loser_id = card2_id
        else:
            winner = card2
            loser = card1
            winner_id = card2_id
            loser_id = card1_id

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        leaderboard = list(self.cards.values())
        leaderboard.sort(key=lambda c: c.rating, reverse=True)

        result = []
        for card in leaderboard:
            result.append(card.get_rank_info())
        return result

    def generate_tournament_report(self) -> dict:
        total_rating = 0
        for card in self.cards.values():
            total_rating += card.rating

        avg_rating = total_rating // len(self.cards)

        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
