import sys
import os
import site


python_path = sys.executable
print(f"This is the sys.executable: {sys.executable}")

prefix = sys.prefix
base_prefix = sys.base_prefix


in_venv = prefix != base_prefix

if in_venv:
    print("MATRIX STATUS: Welcome to the construct\n")
else:
    print("MATRIX STATUS: You're still plugged in\n")
print(f"Current Python: {python_path}")

if in_venv:
    print(f"Virtual Environment: {os.path.basename(prefix)}")
    print(f"Environment Path: {prefix}")
else:
    print("Virtual Environment: None detected")

site_packages = site.getsitepackages()[0]
print(f"\nPackage installation path:\n{site_packages}")
