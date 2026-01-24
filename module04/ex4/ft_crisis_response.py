print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

# List of archive files to access
archives = [
    "lost_archive.txt",       # missing file
    "classified_vault.txt",   # protected file
    "standard_archive.txt"    # normal file
]

for archive in archives:
    if archive == "lost_archive.txt":
        print(f"CRISIS ALERT: Attempting access to '{archive}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    elif archive == "classified_vault.txt":
        print(f"CRISIS ALERT: Attempting access to '{archive}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    else:
        # Normal file access with error handling and 'with'
        print(f"ROUTINE ACCESS: Attempting access to '{archive}'...")
        try:
            with open(archive, "r") as f:
                content = f.read().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed\n")
        except FileNotFoundError:
            print("RESPONSE: Archive not found")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
