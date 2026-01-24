print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
print("\nInitializing new storage unit: new_discovery.txt")

file = open("new_discovery.txt", "w")

print("Storage unit created successfully...\n")
print("Inscribing preservation data...")

data = [
    "{[}ENTRY 001{]} New quantum algorithm discovered\n",
    "{[}ENTRY 002{]} Efficiency increased by 347%\n"
    "{[}ENTRY 003{]} Archived by Data Archivist trainee\n"
]

for line in data:
    file.write(line)
    print(line, end="")

file.close()

print("\nData inscription complete. Storage unit sealed.")
print("Archive 'new_discovery.txt' ready for long-term preservation.")
