"""agent_yl data analysising"""

import numpy as np
import pandas as pd
import json
import os
from data import load_tran_data

df = load_tran_data('unpy_devcod.csv')
df_new = df[['custno', 'unpydt', 'tranti', 'acctno']]
def gain_info(df):
    cust_no = list(set(df.custno))
    cust_len = len(cust_no)
   



