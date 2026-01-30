print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")

# --- Secure Extraction ---
print("SECURE EXTRACTION:")

# Simulate reading classified data safely

try:
    with open("classified_data.txt", "r") as vault:
        data = vault.read().strip()
        print(data)
except FileNotFoundError:
    print("[CLASSIFIED] ERROR: Vault data not found")
except Exception as e:
    print(f"[classified] ERROR: {e}")

print("\nSECURE PRESERVATION:")

# Simulate writing new data safely
try:
    with open("new_security_protocols.txt", "w") as vault:
        vault.write("New security protocols archived\n")
        print("[CLASSIFIED] New security protocols archived")
except Exception as e:
    print(f"[classified] ERROR during preservation: {e}")

print("Vault automatically sealed upon completion")
print("All vault operations completed with maximum security.")

to delte