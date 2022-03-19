import streamlit as st
import pandas as pd
import json
import os
import re
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

# global geocode for apply(do_geocode) call
# # create locator
# locator = Nominatim(user_agent="myGeocoder")
# # delay between geocode calls
# geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

# helper function removes postal code from address so geocode works
def createGeocodeableAddress(string):
    new_address = re.sub(',........', ',', string)
    return new_address

# this helper function avoids timing out the geocode() call
def do_geocode(address, attempt=1, max_attempts=5):
    print(address)
    try:
        return geocode(address)
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            return do_geocode(address, geocode, attempt=attempt+1)
        raise

def addressToCoords():
    # specify file here (for now)
    file = "output/amsterdam.json"

    # make data frame
    df = pd.read_json(path_or_buf = file, typ ='frame')

    # create coord column from location
    # we start with location without postal code because that breaks it
    df['coordinates'] = df['location'].apply(createGeocodeableAddress)

    # create locator
    locator = Nominatim(user_agent="myGeocoder")
    # delay between geocode calls
    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

    # print(1)
    # apply the geocode
    # df['coordinates'] = df['coordinates'].apply(do_geocode)
    df['coordinates'] = df['coordinates'].apply(geocode)

    # create longitude, latitude from coordinates (returns tuple)
    df['point'] = df['coordinates'].apply(lambda coord: tuple(coord.point) if coord else None)
    
    # split point column into 3 columns: latitude, longitude and altitude
    df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
    
    # drop point and altitude, and missing data
    df = df.drop(columns=['point','altitude'])

    # print(1)
    # write out
    df.to_csv(path_or_buf = (re.sub('.json', '.csv', filename), index = True)

if __name__ == "__main__":
    addressToCoords()