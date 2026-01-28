import alchemy.elements

print("=== Sacred Scroll Mastery ===\n")

print("Testing direct module access:")
print("alchemy.elements.create_fire(): ", end="")
alchemy.elements.create_fire()
print("alchemy.elements.create_water(): ", end="")
alchemy.elements.create_water()
print("alchemy.elements.create_earth(): ", end="")
alchemy.elements.create_earth()
print("alchemy.elements.create_air(): ", end="")
alchemy.elements.create_air()

print("\nTesting package-level access (controlled by __init__.py:")
print("alchemy.create_fire(): ", end="")
alchemy.create_fire()
print("alchemy.create_water(): ", end="")
alchemy.create_water()
try:
    alchemy.create_earth()
except AttributeError:
    print("alchemy.create_earth(): AttributeError - not exposed")

try:
    alchemy.create_earth()
except AttributeError:
    print("alchemy.create_air(): AttributeError - not exposed")

print("\nPackage metadata:")
print(f"Version: {alchemy.__version__}")
print(f"Author: {alchemy.__author__}")