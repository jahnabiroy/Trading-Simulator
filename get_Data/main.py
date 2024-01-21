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

# Linkers
from get_stock_data import get_stock_data
from measure_time_size import measure_time_size

    
def main(stock_symbol,years):
    stock_data = get_stock_data(symbol=stock_symbol,years=years)
    file_formats = ['csv', 'txt', 'binary', 'parquet', 'json','xlsx','feather']
    results = {'File Format': [], 'Write Time (s)': [], 'File Size (MB)': []}
    for format in file_formats:
        time_taken,size=measure_time_size(stock_data,format,symbol=stock_symbol)
        results['File Format'].append(format)
        results['Write Time (s)'].append(time_taken)
        results['File Size (MB)'].append(size)
        
    results_df=pd.DataFrame(results)
    fig, ax1 = plt.subplots(figsize=(10, 6))
    bar_width = 0.35
    index = range(len(results_df))
    ax1.bar(index, results_df['Write Time (s)'], width=bar_width, color='blue', label='Write Time')
    ax1.set_xlabel('File Format')
    ax1.set_ylabel('Write Time (s)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax2 = ax1.twinx()
    ax2.bar([i + bar_width for i in index], results_df['File Size (MB)'], width=bar_width, color='green', label='File Size')
    ax2.set_ylabel('File Size (MB)', color='green')
    ax2.tick_params(axis='y', labelcolor='green')
    plt.title(f'Timing and Size Comparison for {stock_symbol} for the past {years} years')
    plt.xticks([i + bar_width / 2 for i in index], results_df['File Format']) 
    plt.savefig(f'{stock_symbol}.png')
    #plt.show()
          
if __name__ == '__main__':
    if(len(sys.argv)<2):
        raise ValueError("Insufficient Arguments")
    stock_symbol = sys.argv[1]
    years = int(sys.argv[2])
    main(stock_symbol=stock_symbol,years=years)