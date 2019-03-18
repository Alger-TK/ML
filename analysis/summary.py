import along
from dateutil.parser import parse
from data import load_tran_data
df = load_tran_data()
df = df[['custno', 'agency_code', 'sender_id', 'unpydt', 'tranti', 'trancd', 'acctno', 'tranmn', 'mcccod',
                 'mrchcd', 'status', 'area_id', 'lat', 'lng', 'devcod']]
df['trantime'] = df['unpydt'] + '/' + df['tranti']
custno = set(df.custno)

df_new = load_tran_data(csv_name = 'df_new_model.csv')

for cust in custno:
    df_per = df[df.custno == cust]
    df_per = detail(df_per)
    df_new = df_new.append(df_per)

df_new.to_csv('D:/code/data/df_new_model.csv', index = False)