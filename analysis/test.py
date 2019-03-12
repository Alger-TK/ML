import pandas as pd
from data import load_tran_data
df_per = load_tran_data(csv_name = 'df_per.csv')
df_per = df_per[['custno', 'agency_code', 'sender_id', 'unpydt', 'tranti', 'trancd', 'acctno', 'tranmn', 'mcccod',
                 'mrchcd', 'mrchad', 'status', 'area_id', 'lat', 'lng', 'devcod']]
df_per['trantime'] = df_per['unpydt'] + '/' + df_per['tranti']
df_per.to_csv('D:/code/data/df_per_new.csv')