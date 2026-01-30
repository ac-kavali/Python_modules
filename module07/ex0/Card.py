
from abc import ABC, abstractmethod


class Card(ABC):
    def __self__(self, name, cost, rarity):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self ):
        pass

    def get_card_info(self):
        pass

    def is_playable(self):
        pass
