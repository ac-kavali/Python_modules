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
    import requests
    print("\nAnalyzing Matrix data...")

    url = "https://www.randomnumberapi.com/api/v1.0/random?min=1&max=100&count=100" # noqa 401
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data")
        return

    numbers = response.json()  # list of 100 numbers

    # convert list to numpy array for numerical processing
    np_numbers = np.array(numbers)

    data = pd.DataFrame({
        "signal_strength": np_numbers
    })

    print(f"Processing {len(data)} data points...")

    # compute average using numpy
    avg_signal = np.mean(np_numbers)
    print(f"Average Signal Strength: {avg_signal:.2f}")

    print("Generating visualization...")

    # new blank canvas for plotting.
    plt.figure()
    plt.hist(np_numbers, bins=20)
    plt.title("Matrix Signal Distribution")
    # labeling the x (__) line
    plt.xlabel("Signal Strength")
    # labeling the y (|) line
    plt.ylabel("Frequency")
    # data saving file
    plt.savefig("matrix_analysis.png")

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    # list of versions if everything installed else, unknow.
    versions = check_dependencies()
    # create fake data and analyze it using a plot.
    analyze_data()
