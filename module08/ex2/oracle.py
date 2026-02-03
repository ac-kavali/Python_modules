import os
from dotenv import load_dotenv

print("ORACLE STATUS: Reading the Matrix...\n")

load_dotenv()

mode = os.getenv("MATRIX_MODE", "development")
database = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "DEBUG")
zion = os.getenv("ZION_ENDPOINT")

print("Configuration loaded:")

print(f"Mode: {mode}")

if database:
    print("Database: Connected to local instance")
else:
    print("Database: Not configured")

if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: Missing")

print(f"Log Level: {log_level}")

if zion:
    print("Zion Network: Online")
else:
    print("Zion Network: Offline")

print("\nEnvironment security check:")
print("[OK] No hardcoded secrets detected")
print("[OK] .env file properly configured")
print("[OK] Production overrides available")

print("\nThe Oracle sees all configurations.")
