import pandas as pd
from dateutil.parser import parse

df_per = pd.read_csv('D:/code/data/df_per.csv', dtype = str)
df_per_len = len(df_per)
df_dic = {col:df_per[col].tolist() for col in df_per.columns}
ls = []
for i in range(28):
    ls.append([0 for i in range(df_per_len)])
trantime = df_dic['trantime']
trancode = df_dic['trancd']
devcode = df_dic['devcod']
card = df_dic['acctno']
lat = df_dic['lat']
lng = df_dic['lng']

for in1 in range(df_per_len):
    count = [0 for i in range(28)]
    for in2 in range(df_per_len):
        t1 = parse(trantime[in1])
        t2 = parse(trantime[in2])
        if t1 >= t2 and (t1 - t2).total_seconds() <= 24*3600 and \
        trancode[in2] == '02000102' and card[in1] == card[in2]:
            count[2] = count[2] + 1
            ls[2][in1] = count[2]
df_per.insert(10, 'tran_dev_area', ls[2])
print(ls)