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
import numpy as np

# Linkers
from measure_time_size import measure_time_size
from get_stock_data import get_stock_data

def main():
    data=pd.read_csv('ind_nifty50list.csv')
    file_formats = ['csv', 'txt', 'binary', 'parquet', 'json','xlsx','feather']
    results = {'File Format': [], 'Write Time (s)': [], 'File Size (MB)': [], 'Years':[]}
    datasize=[1,2,3,4]
    symbol='SBIN'
    years=1
    for format in file_formats:
        years_list = []
        time_list = []
        space_list = []
        format_list=[]
        years=1
        while(years<21):
            # print(format)
            # print(symbol)
            # print(years)
            temp_data = pd.DataFrame(get_stock_data(symbol=symbol,years=years))
            time,space = measure_time_size(temp_data,format,symbol=symbol)
            results['File Format'].append(format)
            results['Write Time (s)'].append(time)
            results['File Size (MB)'].append(space)
            results['Years'].append(years)
            years=years+1
            years_list.append(years)
            time_list.append(time)
            space_list.append(space)
            format_list.append(format)
    results_df = pd.DataFrame(results)
    
    # Plotting
    plt.figure(figsize=(12, 6))

    # Plotting Time
    plt.subplot(1, 2, 1)
    for file_format in file_formats:
        format_mask = results_df['File Format'] == file_format
        plt.plot(results_df[format_mask]['Years'], results_df[format_mask]['Write Time (s)'], label=f"{file_format} - Time")

    plt.xlabel("Years")
    plt.ylabel("Time (s)")
    plt.title("Time for each file format")
    plt.legend()
    plt.xticks(np.arange(min(years_list), max(years_list)+1, 1))

    # Plotting Space
    plt.subplot(1, 2, 2)
    for file_format in file_formats:
        format_mask = results_df['File Format'] == file_format
        plt.plot(results_df[format_mask]['Years'], results_df[format_mask]['File Size (MB)'], label=f"{file_format} - Space")

    plt.xlabel("Years")
    plt.ylabel("Space (MB)")
    plt.title("Space for each file format")
    plt.legend()
    plt.xticks(np.arange(min(years_list), max(years_list)+1, 1))

    plt.tight_layout()
    plt.savefig('Format_performance.png')
    #print(results_df)

                
            
    
if __name__=='__main__':
    main()
    