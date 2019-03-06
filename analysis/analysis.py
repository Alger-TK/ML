"""agent_yl data analysising"""

import numpy as np
import pandas as pd
import json
import os
from data import load_tran_data

df = load_tran_data('unpy_devcod.csv')

# obtain transaction data for a single customer
def get_per_cust(df):
    df_new = df[['custno', 'unpydt', 'tranti', 'acctno']]
    cust_no = list(set(df.custno))
    cust_len = len(cust_no)
    for it in range(cust_len):
        df_per = df[df.custno == cust_no[it]]
        if len(df_per) > 200:
            break
    return df_per

df_per = get_per_cust(df)
df_per.to_csv('D:\code\data\df_per.csv')




