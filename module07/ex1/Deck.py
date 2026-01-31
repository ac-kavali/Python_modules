from errno import EILSEQ

from winsound import PlaySound

from ex0.Card import Card
import random

class Deck:
    cards = []
    def add_card (self, card: Card) -> None:
        if isinstance(card, Card):
            # card = {"name": card.name, "type": card.type}
            Deck.cards.append(card)

    def remove_card (self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle (self) -> None:
        random.shuffle(self.cards)



    def draw_card (self):
        if not self.cards:
            return None

        index = random.randint(0, len(self.cards) - 1)
        card = self.cards[index]
        if card.name =="Fire Dragon":
            effect = "Creature summoned to battlefield"
        else:
            effect = getattr(card, 'effect', None)
        game_state = {
            'card_played': card.name,
            'mana_used': card.cost,
            'effect': effect
        }

        print(f"Drew: {card.name} ({card.type})")

        stats = card.play(game_state)

        self.cards.pop(index)  # remove by index, not object
        return stats

    def total_cost (self):
        total = 0
        for card in self.cards:
            total += card.cost
        return total




    def get_deck_stats (self) -> dict:
        creature_num = 0
        spell_num = 0
        artifact_num = 0
        for card in self.cards:
            if card.type == "Creature":
                creature_num += 1
            elif card.type == "Artifact":
                artifact_num += 1
            elif card.type == "Spell":
                spell_num += 1

        return {
            "total_cards" : len(self.cards),
            "creatures": creature_num,
            "spells": spell_num,
            "artifacts": artifact_num,
            "avg_cost": float("{:.2f}".format(self.total_cost() / len(self.cards))) if self.cards else 0

        }


