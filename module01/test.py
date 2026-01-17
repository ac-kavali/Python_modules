class Animal:

    def eat(self):
        print("The animal is eating")

class Rabit(Animal):

    def eat(self):
        print("The rabbit is eating")

rabbit = Rabit()

rabbit.eat()