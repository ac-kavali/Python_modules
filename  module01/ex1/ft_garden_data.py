class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def details(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")


rose = Plant("rose", 12, 150)
lutos = Plant("lutos", 15, 678)
marijuana = Plant("marijuana", 97, 300)

print("=== Garden Plant Registry ===")
rose.details()
lutos.details()
marijuana.details()
