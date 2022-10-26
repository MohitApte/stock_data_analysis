# Description: This is a stock market dashboard to show some charts and data on some stock
#Importing Libraries

import streamlit as st
import pandas as pd
import yfinance as yf  
from PIL import Image
import urllib.request

# Add a title and an image

st.write("""
# Stock Market Web Application
**Visually** show data on a stock!
""")

urllib.request.urlretrieve('https://cpb-us-w2.wpmucdn.com/u.osu.edu/dist/6/44792/files/2017/04/stock-market-3-21gyd1b.jpg', "stock_image")

image = Image.open("stock_image")

st.image(image, use_column_width=True)

# Create a sidebar header

st.sidebar.header('User Input')

# Create a function to get the users input

def get_input():
    start_date = st.sidebar.text_input("Start Date", "2015-01-02")
    end_date = st.sidebar.text_input("End Date", "2020-01-02")
    stock_symbol = st.sidebar.text_input("Stock Symbol", "GOOGL")
    return start_date, end_date, stock_symbol





# Create a function to get the proper company data and the proper timeframe

def get_data(symbol, start, end):
    #Load Data

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    df = yf.download(symbol, start, end)


    

    return df

start, end, symbol = get_input()

df = get_data(symbol,start,end)

#Display the close price

st.header(symbol + " Close Price\n")
st.line_chart(df['Close'])

#Display the Volume

st.header(symbol + " Volume\n")
st.line_chart(df['Volume'])


# Display the statistics

st.header('Data Statistics')
st.write(df.describe())





