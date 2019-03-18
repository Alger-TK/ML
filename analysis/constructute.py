from data import load_tran_data

df = load_tran_data(csv_name = 'unpy_mcc_only_haze.csv')
length = len(df)
print(length)