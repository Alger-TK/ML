import numpy as np
import pandas as pd
import json
from pandas import DataFrame, Series
from dateutil.parser import parse
from data import load_tran_data

df_per = load_tran_data(csv_name = 'df_per.csv')
df_per = df_per[['custno', 'agency_code', 'sender_id', 'unpydt', 'tranti', 'trancd', 'acctno', 'tranmn', 'mcccod',
                 'mrchcd', 'mrchad', 'status', 'area_id', 'lat', 'lng', 'devcod']]
df_per_len = len(df_per)
df_dic = {col: df_per[col].tolist() for col in df_per.columns}

def process(df_dic, df_per_len):
    ls = [0 for i in range(df_per_len)]
    dev = df_dic['devcod']
    """
    df_per_len:lenggth of transaction information of single customer
    df_dic: change dataframe to dict type 
    
    """

    return ls

def count_card(df_dic, df_per_len):
    card = df_dic['acctno']
    count_card = len(list(set(card)))
    return count_card




c = count_card(df_dic, df_per_len)
card_num = [c for i in range(df_per_len)]
df_dic['card_num'] = card_num
df_per = DataFrame(df_dic)
print(df_per.info())
print(df_per)




