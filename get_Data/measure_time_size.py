# importing necessary libraries
from datetime import date
from jugaad_data.nse import bhavcopy_save, bhavcopy_fo_save
import pandas as pd
import time
import os
import matplotlib.pyplot as plt
from jugaad_data.nse import stock_df
import sys
import pyarrow

def measure_time_size(data,file_format,symbol):
    if file_format=='csv':
        file_path=f'{symbol}.csv'
        start=time.time()
        data.to_csv(file_path, index=False)
        end = time.time()
    elif file_format=='txt':
        file_path=f'{symbol}.txt'
        start=time.time()
        data.to_csv(file_path, index=False,sep='\t')
        end = time.time()
    elif file_format=='binary':
        file_path=f'{symbol}.pkl'
        start=time.time()
        data.to_pickle(file_path)
        end = time.time()
    elif file_format=='parquet':
        file_path=f'{symbol}.parquet'
        start=time.time()
        data.to_parquet(file_path, index=False)
        end = time.time()
    elif file_format=='json':
        file_path=f'{symbol}.json'
        start=time.time()
        data.to_json(file_path, index=False)
        end = time.time()
    elif file_format=='xlsx':
        file_path=f'{symbol}.xlsx'
        start=time.time()
        data.to_excel(file_path, index=False)
        end = time.time()
    elif file_format=='feather':
        file_path=f'{symbol}.feather'
        start=time.time()
        data.to_feather(file_path)
        end = time.time()
    else:
        raise ValueError(f"Unsupported file format: {file_format}")
    
    time_taken = end-start
    file_size=os.path.getsize(file_path)/(1024*1024) # Convert to MB
    return time_taken,file_size