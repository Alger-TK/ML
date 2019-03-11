import numpy as np
import pandas as pd
import json
from pandas import DataFrame, Series
from dateutil.parser import parse
from data import load_tran_data

df_per = load_tran_data(csv_name = 'df_per.csv')
df_per = df_per[['custno', 'agency_code', 'sender_id', 'unpydt', 'tranti', 'trancd', 'acctno', 'tranmn', 'mcccod',
                 'mrchcd', 'mrchad', 'status', 'area_id', 'lat', 'lng', 'devcod']]


def count_card(df_per = df_per):
    """
        df_per_len:length of transaction information of single customer
        df_dic: change dataframe to dict type
        card: card list of customer
        count_card: number of card owned by customer
    """
    df_per_len = len(df_per)
    df_dic = {col: df_per[col].tolist() for col in df_per.columns}
    card = df_dic['acctno']
    count_card = len(list(set(card)))
    ls = [count_card for i in range(df_per_len)]
    df_per.insert(7, 'count_card', ls)
    return df_per

count_card()
df_per.to_csv('D:/code/data/df_new.csv')





