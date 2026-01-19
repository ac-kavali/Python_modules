class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age
        self.plant_creation_log()

    def plant_creation_log(self):
        print(f"Plant Created: {self.name}")

    def set_height(self, height):
        if height < 0:
            print(
                f"\nInvalid operation attempted: "
                f"height {height} [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            self.__height = height
            print(
                f"Age updated: "
                f"{self.get_age()} days [OK]"
            )

    def set_age(self, age):
        if age < 0:
            print(
                f"\nInvalid operation attempted: "
                f"age {age} [REJECTED]"
            )
            print("Security: Negative age rejected")
        else:
            self.__age = age
            print(
                f"Height updated: "
                f"{self.get_height()} cm [OK]"
            )

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age


def main():
    print("=== Garden Security System ===")

    marijuana = Plant("Marijuana", 20, 30)
    marijuana.set_height(65)
    marijuana.set_age(16)

    marijuana.set_height(-12)

    print(
        f"\nCurrent plant: {marijuana.name} "
        f"({marijuana.get_height()}cm, "
        f"{marijuana.get_age()} days)"
    )


if __name__ == "__main__":
    main()
