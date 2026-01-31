from ex0.Card import Card
import random

class Deck:
    cards = []
    def add_card (self, card: Card) -> None:
        if isinstance(card, Card):
            Deck.cards.append(card)

    def remove_card (self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle (self) -> None:
        random.shuffle(self.cards)

    def draw_card (self) -> Card:
         pass

    def get_deck_stats (self) -> dict:
        pass