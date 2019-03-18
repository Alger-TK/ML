# add transaction time
from data import load_tran_data
df = load_tran_data(csv_name = 'unpy_mcc_only_haze.csv')
df['trantime'] = df['unpydt'] + '/' + df['tranti']
df.to_csv('D:/code/data/unpay_tran.csv')