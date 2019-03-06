import numpy as np
import pandas as pd
import json
from data import load_tran_data

df_per = load_tran_data(csv_name = 'df_per.csv')
print(df_per.info())
