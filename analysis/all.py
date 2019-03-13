import numpy as np
import pandas as pd
from data import load_tran_data
from along import detail_1, detail_2, detail_3

df = load_tran_data(csv_name = 'unpy_devcod_new.csv')

customer = list(set(df['custno']))
customer_1 = customer[:1000]
for custno in customer_1:
    df_per = df[df.custno == custno]
    df_per = df_per[['custno', 'agency_code', 'sender_id', 'unpydt', 'tranti', 'trancd', 'acctno', 'tranmn', 'mcccod',
                     'mrchcd', 'mrchad', 'status', 'area_id', 'lat', 'lng', 'devcod']]
    df_per['trantime'] = df_per['unpydt'] + '/' + df_per['tranti']
    df_per = detail_1(df_per)
    df_per = detail_2(df_per)

    df_new.append(df_per)
    df_new.to_csv('D:/code/data/df_new.csv')


