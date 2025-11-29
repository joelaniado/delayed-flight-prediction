import os
import glob
import time
import sys
sys.path.append(os.getcwd())

import pandas as pd
import polars as pl

from src.utils.paths import DATA_DIR

def main():

    start_time = time.time()

    directory = DATA_DIR / "raw" / "airline_data" / "*.csv"
    files = glob.glob(str(directory))
    dfs = [pl.scan_csv(file) for file in files]
    final_df = pl.concat(dfs).collect()
    final_df.write_parquet(DATA_DIR / "raw"/ "airline_data" / "2024-airline-data.parquet")

    print(f'Run time: {time.time()-start_time:.4f}')
        

if __name__ == "__main__":
    main()