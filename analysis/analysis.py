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
        df_per = df[df.custno == cust_no[it]]
        if len(df_per) > 200:
            print(cust_no[it])
            break
    return df_per

df = pd.read_csv('D:/code/data/unpy_devcod.csv')




