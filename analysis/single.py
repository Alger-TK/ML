import numpy as np
import pandas as pd
import json
from pandas import DataFrame, Series
from dateutil.parser import parse
from data import load_tran_data

df_per = load_tran_data(csv_name = 'df_per.csv')
df_per = df_per[['custno', 'agency_code', 'sender_id', 'unpydt', 'tranti', 'trancd', 'acctno', 'tranmn', 'mcccod',
                 'mrchcd', 'mrchad', 'status', 'area_id', 'lat', 'lng', 'devcod']]
df_per['trantime'] = df_per['unpydt'] + '/' + df_per['tranti']

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

def detail(df_per = df_per):
    df_per_len = len(df_per)
    df_dic = {col:df_per[col].tolist() for col in df_per.columns}
    ls = [0 for i in range(df_per_len)]
    trantime = df_dic['trantime']
    trancode = df_dic['trancd']
    devcod = df_dic['devcod']
    for in1 in range(df_per_len):
        t1 = parse(trantime[in1])
        for in2 in range(df_per_len):
            t2 = parse(trantime[in2])
            count_pos = 0
            if t1 >= t2 and (t1 - t2).total_seconds() <= 600 \
            and trancode[in2] == '02000000' and devcod[in1] == devcode[in2]:
                count_pos = count_pos + 1
                ls[in1] = count_pos
    df_per.insert(8,'tran_5_num',ls)
    return df_per













