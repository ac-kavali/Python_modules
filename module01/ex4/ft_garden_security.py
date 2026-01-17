class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age

    def set_height(self, height):
        if height < 0:
            print(f"\nInvalid operation attempted: height {height} [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def set_age(self, age):
        if age < 0:
            print(f"\nInvalid operation attempted: age {age} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


marijuana = Plant("Marijuana", 20, 30)

print("=== Garden Security System ===")

marijuana.set_height(65)
marijuana.set_age(16)

print(f"Plant Created: {marijuana.name}")
print(f"Height updated: {marijuana.get_height()} cm [OK]")
print(f"Age updated: {marijuana.get_age()} days [OK]")

marijuana.set_height(-12)

print(f"\nCurrent plant: {marijuana.name} ({marijuana.get_height()}cm, {marijuana.get_age()} days)")