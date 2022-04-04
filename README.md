# Fudmaa
Funda data scraper using Python Scrapy.  
Analysis on this data using NumPy(not done).  
Data visualization web app using Streamlit and Pandas.  
Address to coordinate using GeoPy with Nominatim.  

## Dependencies
Scrapy 2.6.1  
Python 3.8.5  
Numpy 1.22.3  
Pandas 1.16.0  
Streamlit 1.8.1  
GeoPy 2.2.0  

## How to use

### Web scraper:
--------------------
Specify funda(index) URL, output filename, and output format when running main.py.  
example call:  

__python3 main.py "https://www.funda.nl/koop/amsterdam" amsterdam json__  

Output in Fudmaa/output.  
<br>
<br>

### Convert address to coordinates
--------------------

Change addressToCords.py to use your .json file (currently only supports json import).  

__python3 addressToCords.py__  

May take a while... output in Fudmaa/output/  
<br>
<br>

### Run webserver to visualize data on map  
--------------------
Change in webapp.py what files should be visualized.

__streamlit run webapp.py__  




