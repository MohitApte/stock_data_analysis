# Description: This is a stock market dashboard to show some charts and data on some stock
#Importing Libraries

import streamlit as st
import pandas as pd
import yfinance as yf  
from PIL import Image
import urllib.request
from bsedata.bse import BSE
import json
from datetime import date
from datetime import timedelta
# Add a title and an image

st.write("""
# Stock Market Analysis
""")

urllib.request.urlretrieve('https://cpb-us-w2.wpmucdn.com/u.osu.edu/dist/6/44792/files/2017/04/stock-market-3-21gyd1b.jpg', "stock_image")

image = Image.open("stock_image")

st.image(image, width=500)

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

#Display the Sensex
today = date.today()
yesterday = today - timedelta(days = 1)
senstart = pd.to_datetime(yesterday)
senend = pd.to_datetime(yesterday)

sen_df = yf.download("^BSESN", senstart, senend)

st.write("""
# Current Sensex Close Value
""")
cur_val = sen_df['Close'][0]
st.write("# ", cur_val)

st.write("""
# BSE Sensex Close Price
""")
new_start = pd.to_datetime("2000-01-01")
new_sen_df = yf.download("^BSESN", new_start, senend)

st.line_chart(new_sen_df['Close'])



# BSE Top Runners and Top Losers

b = BSE()
tg = b.topGainers()
tg_data = json.dumps(tg)
tg_df = pd.read_json(tg_data)
tl = b.topLosers()
tl_data = json.dumps(tl)
tl_df = pd.read_json(tl_data)

st.write("""
# BSE Top Runners
""")

st.write(tg_df)

st.write("""
# BSE Top Losers
""")

st.write(tl_df)
st.write("----------------------------------------------------------------------------------")

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    color: red;
}
.norm-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Disclaimer : </p>', unsafe_allow_html=True)
st.markdown('<p class="norm-font">On Mobile, Open > at the top left for Company Specific Stock Details</p>', unsafe_allow_html=True)



st.write("# Stock Statistics of "+ symbol)



#Display the close price

st.header(symbol + " Close Price\n")
st.line_chart(df['Close'])

#Display the Volume


st.header(symbol + " Volume\n")
st.line_chart(df['Volume'])


# Display the statistics

st.header('Data Statistics')
st.write(df.describe())





