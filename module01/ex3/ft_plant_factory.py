class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def details(self):
        print(f"Created: {self.name} ({self.height} cm, {self.age} days)")


rose = Plant("Rose", 12, 150)
lotus = Plant("Lutos", 15, 678)
marijuana = Plant("Marijuana", 97, 300)
vanilla = Plant("Vanilla", 18, 89)
coca = Plant("Coca", 30, 78)

plants = [rose, lotus, marijuana, vanilla, coca]

for plant in plants:
    plant.details()
