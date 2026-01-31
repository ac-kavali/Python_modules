from abc import ABC, abstractmethod


class CardFactory (ABC):
    @abstractmethod
    def create_creature(self, name_or_power) -> Card:
        pass

class def create_spell(self, name_or_power) -> Card