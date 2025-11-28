import os
import glob

from src.utils.paths import DATA_DIR

def main():
    directory = DATA_DIR / "raw" / "airline_data"
    for filename in glob.glob(f"{directory}/*"):
        print(filename)

if __name__ == "__main__":
    main()