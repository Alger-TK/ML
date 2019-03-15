from data import load_tran_data

df = load_tran_data(csv_name = 'unpy_mcc_only_haze.csv')
mcc = list(set(df.type))
print(mcc)