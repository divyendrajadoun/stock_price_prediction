from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import pdb
from pandas.io.json import json_normalize

api_k = "8s4jrzt0g8l2goim"  # api_key
api_s = "ow9thuel7etz60y2nlpj10dpg2rgfghv"  # api_secret
access_token = "4DW92eKyS5XkTeZhw5C6CWPLAqdmx617"


def get_login(api_k, api_s):
    global kws, kite
    kite = KiteConnect(api_key=api_k)

    # comment after getting access data for first time

    # print("[*] Generate Request Token : ", kite.login_url())
    # request_tkn = input("[*] Enter Your Request Token Here : ")
    # data = kite.generate_session(request_tkn, api_secret=api_s)
    # kite.set_access_token(data["access_token"])
    # kws = KiteTicker(api_k, data["access_token"])
    # print(data['access_token'])


    kite.set_access_token(access_token)
    kws = KiteTicker(api_k, access_token)


    return kite

kite = get_login(api_k, api_s)
# pdb.set_trace()

