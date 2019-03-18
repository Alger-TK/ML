import along
from dateutil.parser import parse
from data import load_tran_data
df = load_tran_data()
custno = set(df.custno)


df_new = load_tran_data(csv_name = 'df_new_model.csv')

for cust in custno:
    df_per = df[df.custno == cust]
    df_dic = {col: df_per[col].tolist() for col in df_per.columns}
    df_per_len = len(df_per)
    devcod = df_dic['devcod']
    card = df_dic['acctno']
    tranmn = df_dic['tranmn']
    mcc_lab = df_dic['subtype_label']
    lat = df_dic['lat']
    lng = df_dic['lng']
    ls = []
    df_per = detail(df_per)
    df_new = df_new.append(df_per)

df_new.to_csv('D:/code/data/df_new_model.csv', index = False)