import streamlit as st
import pandas as pd
import json
import os


st.write("""
    # Simple data visualization of scraped data from funda.
""")

csv_files = []
csv_dataframes = []

# iterate over .csv files
for file in os.scandir('output/'):
    if file.is_file():
        # check extrension
        if (file.path[-4:] == ".csv"):
            print(file.path)
            csv_files.append(file.path)
            
# read csv files as dataframes
for file in csv_files:
    csv_dataframes.append(pd.read_csv(file))

# drop NaN
csv_dataframes = map(lambda df : df.dropna(subset=['longitude']), csv_dataframes)

# print on page
for index, df in enumerate(csv_dataframes):
    # "output/filename.csv" -> "filename"
    st.write(csv_files[index][7:-4])
    st.map(df)
