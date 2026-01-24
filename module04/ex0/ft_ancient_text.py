print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print("\nAccessing Storage Vault: ancient_fragment.txt")

file = open("/home/achahi/PyCharmMiscProject/Python_modules/module04/files/ancient_fragment.txt", "r")
print("Connection established...")
print("\nRECOVERED DATA:")

data = file.read()
print(data)

file.close()
print("\nData recovery complete. Storage unit disconnected.")
