import os
import glob
import time
import sys
sys.path.append(os.getcwd())

import pandas as pd
import polars as pl

from src.utils.paths import DATA_DIR

def airline_files_merge():
    directory = DATA_DIR / "raw" / "airline_data" / "*.csv"
    files = glob.glob(str(directory))
    dfs = [pl.scan_csv(file) for file in files]
    final_df = pl.concat(dfs).collect()
    final_df.write_parquet(DATA_DIR / "raw"/ "airline_data" / "2024-airline-data.parquet")

def raw_weather_data_processing():
    data_path = DATA_DIR / "raw" / "weather-data" / "raw_weather_data.csv"
    df = pd.read_csv(data_path)
    print(f'{df.info()}\n{df.head()}')

    

def main():

    start_time = time.time()
    #airline_file_merge()
    raw_weather_data_processing()

    

    print(f'Run time: {time.time()-start_time:.4f}')
        

if __name__ == "__main__":
    main()