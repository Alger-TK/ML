import numpy as np
import pandas as pd
import json
from dateutil.parser import parse
from data import load_tran_data

df_per = load_tran_data(csv_name = 'df_per.csv')
print(df_per.tran)


def process(df_per):
    # df_per_len: length of transaction information of single customer
    df_per_len = len(df_per)


