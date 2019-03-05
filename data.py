#get tran data
import os
import pandas as pd
def load_tran_data(csv_name, tran_path = 'D:\code\data'):
    csv_path = os.path.join(tran_path, csv_name)
    return pd.read_csv(csv_path, dtype = str)