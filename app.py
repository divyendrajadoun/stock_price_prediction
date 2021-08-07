import zrd_login
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bs4 import BeautifulSoup
import requests
import json
import time
import csv

kite = zrd_login.kite
st.set_page_config(layout="wide")

image = Image.open(r'C:\Users\user\PycharmProjects\Algo Trading\sm_devi11.png')
st.image(image)
# st.title("Polymath Algo Solutions")
st.markdown("""
This app retrieves stock prices for the all Companies Listed under NSE
""")

#About
expander_bar = st.expander("Polymath Algorithmic Trading Solutions")
expander_bar.markdown("""
* This web app has been created to give time and execution leverage to the retail traders, so that they can make quick decisions and quick execution as well 
* Creator of Stocks Scanner App is Polymath Algo Solutions, Divyendra Singh Jadoun
""")


stock = st.text_input("Enter Stock Name", "Type here..")
col1 = st.sidebar
col2, col3 = st.columns((2,1))

col1.header('Polymath Algo Solutions')

exchange = col1.selectbox('Select EXCHANGE',('NSE','BSE','CRYPTO'))

if st.button('Price'):
    zrd_name = 'NSE:'+stock
    a = kite.quote(zrd_name)[zrd_name]['last_price']
    st.text("The Price is")
    st.success(a)

if st.button('OHLC'):
    zrd_name = 'NSE:'+stock
    b = kite.quote(zrd_name)[zrd_name]['ohlc']
    st.text("OHLC is :")
    st.success(b)

if st.button('Volume'):
    zrd_name = 'NSE:'+stock
    c = kite.quote(zrd_name)[zrd_name]['volume']
    st.text("Volume is :")
    st.success(c)

if st.button('Buy'):
    zrd_name = 'NSE:'+stock
    d = kite.place_order(tradingsymbol=stock,
                 exchange=kite.EXCHANGE_NSE,
                 transaction_type=kite.TRANSACTION_TYPE_BUY,
                 quantity=10,variety=kite.VARIETY_AMO,
                 order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_MIS)
    st.text("Congrats you Bought 1 Share :")
    st.success(d)

if st.button('Sell'):
    zrd_name = 'NSE:'+stock
    e = kite.place_order(tradingsymbol=stock,
                 exchange=kite.EXCHANGE_NSE,
                 transaction_type=kite.TRANSACTION_TYPE_SELL,
                 quantity=10,variety=kite.VARIETY_AMO,
                 order_type=kite.ORDER_TYPE_MARKET,product=kite.PRODUCT_MIS)
    st.text("Congrats you Sold 1 Share :")
    st.success(e)

# if st.button('Historical Data'):
#     df = pd.read_csv(fr"C:\Users\user\PycharmProjects\Algo Trading\5_min_data\RELIANCE.csv)
#     st.title(stock)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)


if st.button('Graph'):
    zrd_name = 'NSE:'+stock

    # st.text("Graph :")
    # st.success(c)
    df = pd.read_csv(fr'C:\Users\user\PycharmProjects\Algo Trading\{stock}.csv')
    a = plt.plot()
    plt.show()
    print(a)

# df = pd.read_excel(...)  # will work for Excel files




# @st.cache

# text_input("Stock Name","type here")


    # df = load_data()
    #
    #
    # sorted_coin = sorted(df['coin-symbol'])
    # selected_coin = col1.multiselect('Cryptocurrency', sorted_coin, sorted_coin )
    #
    # df_selected_coin = df[(df['coin_symbol'].isin(selected_coin))]
    #
    # num_coin = col1.slider('Display Tom N Coins', 1, 100, 100)
    # df_coins = df_selected_coin[:num_coin]
    #
    # percent_timeframe = col1.selectbox('Percent change time frame',
    #                                    ['7d','24h','1h'])
    # percent_dict = {"7d": 'percent_change_7d', "24h":'percent_change_24h', "1h": 'percent_change_1h'}
    # selected_percent_timeframe = percent_dict[percent_timeframe]
    #
    # sort_values = col1.selectbox('Sort Values?', ['Yes','No'])
    #
    # col2.subheader('Price Data of Selected Cryptocurrency')
    # col2.write('Data Dimension: ' + srt(df_selected_coin.shape[0]) + ' rows and ' + str(df_selected_coin.shape[1]))