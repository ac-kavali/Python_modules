from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str, attack: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack

        # tournament stats
        self.wins = 0
        self.losses = 0
        self.rating = 1200  # default starting rating

    # ----- Card -----
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "effect": "Tournament card entered match"
        }

    # ----- Combatable -----
    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        survived = incoming_damage < self.attack_power
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "survived": survived
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power
        }

    # ----- Rankable -----
    def calculate_rating(self) -> int:
        # VERY simple rating system
        self.rating = 1200 + (self.wins * 16) - (self.losses * 16)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }
