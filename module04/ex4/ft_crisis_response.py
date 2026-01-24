print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

archives = [
    "lost_archive.txt",
    "classified_vault.txt",
    "standard_archive.txt"
]

for archive in archives:
    try:
        if archive == "classified_vault.txt":
            # Simulate restricted access
            raise PermissionError

        print(f"\nROUTINE ACCESS: Attempting access to '{archive}'...")
        with open(archive, "r") as f:
            content = f.read().strip()

        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{archive}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{archive}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

print("All crisis scenarios handled successfully. Archives secure.")
