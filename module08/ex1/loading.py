import sys
import importlib

REQUIRED_PACKAGES = ["pandas", "requests", "matplotlib", "numpy"]

def check_dependencies():
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    versions = {}
    missing = []

    for pkg in REQUIRED_PACKAGES:
        try:
            module = importlib.import_module(pkg)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {pkg} ({version}) - Ready")
            versions[pkg] = version
        except ImportError:
            print(f"[MISSING] {pkg} - Not installed")
            missing.append(pkg)

    if missing:
        print("\nERROR: Missing dependencies!")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("\nOr install with Poetry:")
        print("poetry install")
        sys.exit(1)

    return versions


def analyze_data():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    data = pd.DataFrame({
        "signal_strength": np.random.randint(1, 100, 1000)
    })

    print(f"Processing {len(data)} data points...")

    avg_signal = data["signal_strength"].mean()
    print(f"Average Signal Strength: {avg_signal:.2f}")

    print("Generating visualization...")

    plt.figure()
    plt.hist(data["signal_strength"], bins=20)
    plt.title("Matrix Signal Distribution")
    plt.xlabel("Signal Strength")
    plt.ylabel("Frequency")
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    versions = check_dependencies()
    analyze_data()
