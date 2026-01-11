class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height):
        if height < 0:
            print("!! Height cannot be negative!")
            return
        self.__height = height

    def set_age(self, age):
        if age < 0:
            print("!! Age cannot be negative!")
            return
        self.__age = age

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


marijuana = Plant("marijuana", 20, 30)

print("=== Garden Security System ===")

marijuana.set_height(65)
marijuana.set_age(16)

print(f"Plant Created: {marijuana.name}")
print(f"Height updated: {marijuana.get_height()} cm [OK]")
print(f"Age updated: {marijuana.get_age()} days [OK]")

marijuana.set_height(-12)
marijuana.set_age(-2)
