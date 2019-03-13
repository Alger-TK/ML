import numpy as np
import pandas as pd
from data import load_tran_data



df = load_tran_data(csv_name = 'unpy_devcod_new.csv')
customer = list(set(df['custno']))
customer_1 = customer[:1000]
for custno in customer_1:
    df_per = df[df.custno == custno]

