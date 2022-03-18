import streamlit as st
import pandas as pd
import json
import os


st.write("""
# Simple data visualization of scraped data from funda.
""")

df_amsterdam = pd.read_csv("output/amsterdam.csv")
df_nunspeet = pd.read_csv("output/nunspeet_18-03-2022.csv")
# df_groningen = pd.read_csv("output/groningen.csv")

df_amsterdam['latitude']=pd.to_numeric(df_amsterdam['latitude']) 
df_amsterdam['longitude']=pd.to_numeric(df_amsterdam['longitude'])

df_nunspeet['latitude']=pd.to_numeric(df_nunspeet['latitude']) 
df_nunspeet['longitude']=pd.to_numeric(df_nunspeet['longitude'])

# df_groningen['latitude']=pd.to_numeric(df_groningen['latitude']) 
# df_groningen['longitude']=pd.to_numeric(df_groningen['longitude'])

# drop NaN
df_amsterdam = df_amsterdam.dropna(subset=['longitude'])
df_nunspeet = df_nunspeet.dropna(subset=['longitude'])
# df_groningen = df_groningen.dropna(subset=['longitude'])

# paint map figure
st.map(df_amsterdam)
st.map(df_nunspeet)
# st.map(df_groningen)
