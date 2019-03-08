"""agent_yl data analysising"""

import numpy as np
import pandas as pd
import json
import os
from data import load_tran_data

#df = load_tran_data('unpy_devcod.csv')

# obtain transaction data for a single customer
def get_per_cust(df):
    cust_no = list(set(df.custno))
    cust_len = len(cust_no)
    for it in range(cust_len):
        df_per = df[df.custno == cust_no[it]].copy()
        if len(df_per) > 200:
            print(cust_no[it])
            break
    return df_per

df = load_tran_data()

df_per = get_per_cust(df)
df_per.to_csv('D:\code\data\df_per.csv')





