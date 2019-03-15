import numpy as np
import pandas as pd
from data import load_tran_data
from pandas import DataFrame, Series
from along import detail_1, detail_2, detail_3

df = load_tran_data(csv_name = 'df_new.csv')
custno = list(set(df.custno))


df_new = load_tran_data(csv_name = 'df_new_model.csv')

custno1 = custno[:1000]
for cust in custno1:
    df_per = df[df.custno == cust]
    df_per = detail_1(df_per)
    df_new = df_new.append(df_per)

df_new.to_csv('D:/code/data/df_ana_new.csv', index = False)












