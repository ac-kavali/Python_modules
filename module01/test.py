class Dog:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound

    def speak(self):
        print (f"{self.sound}... {self.sound}...{self.sound}. ")

    def smell (self):
        print ("Dog smells somthing...")

class Cat(Dog):
    def __init__(self, name, color, sound):
        super().__init__(name, color, sound)

    def jump(self):
        print("Cat is jumping...")

kitty = Cat("Kitty", "White", "Meow")
spick = Dog("Spick", "black", "bark")

print(f"Animal name: {kitty.name}")
kitty.speak()

