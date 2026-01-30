from abc import ABC


class Card(ABC):
    def __self__(self, name, cost, rarity):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    def get_card_info(self):
        pass

    def is_playable(self):
        pass


#play to be implemented later