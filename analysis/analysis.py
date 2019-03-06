"""agent_yl data analysising"""

import numpy as np
import pandas as pd
import json
import os
#from data import load_tran_data

def load_tran_data(csv_name, tran_path = 'D:\code\data'):
    csv_path = os.path.join(tran_path, csv_name)
    return pd.read_csv(csv_path, dtype = str)
df = load_tran_data('unpy_devcod.csv')
df_new = df[['custno', 'unpydt', 'tranti', 'acctno']]
# def gain_info(df):
#     cust_no = list(set(df.custno))
#     cust_len = len(cust_no)

cust_no = list(set(df.custno))
cust_len = len(cust_no)
for it in range(cust_len):
    df_per = df[df.custno == cust_no[it]]
    if len(df_per) > 200:
        break
df_per.to_csv('D:\code\data\df_per.csv')




