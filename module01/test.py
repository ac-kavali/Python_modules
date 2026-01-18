
class Engine:
    def __init__(self, brand,hp, volume):
        self.brand = brand
        self.hp = hp
        self.volume = volume

class Front_Glass:
    def __init__(self, brand, length, width):
        self.brand = brand
        self.length = length
        self.width = width

class Back_Glass(Front_Glass):
    def __init__(self, brand, length, width):
        super().__init__(brand, length, width)

class Car:
    def __init__(self, brand, module):
        self.module = module
        self.brand = brand
        self.components = []

    def add_component(self, component):
        self.components.append(component)
        print(f"New component added : {component} to the {self.brand} {self.module}")




