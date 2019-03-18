from data import load_tran_data
df_dic = {col: df_per[col].tolist() for col in df_per.columns}
df_per_len = len(df_per)
devcod = df_dic['devcod']
card = df_dic['acctno']
tranmn = df_dic['tranmn']
mcc_lab = df_dic['subtype_label']
lat = df_dic['lat']
lng = df_dic['lng']
ls = []
def detail_1(df_per, df_per_len):
    ls = []
    for i in range(8):
        ls.append([0 for i in range(df_per_len)])
    trantime = df_dic['trantime']
    trancode = df_dic['trancd']
    devcode = df_dic['devcod']
    card = df_dic['acctno']
    tranmn = df_dic['tranmn']
    lat = df_dic['lat']
    lng = df_dic['lng']

    for in1 in range(df_per_len):
        count = [0 for i in range(8)]
        for in2 in range(df_per_len):
            t1 = parse(trantime[in1])
            t2 = parse(trantime[in2])

            if t1 >= t2 and card[in1] == card[in2]:
                if (t1 - t2).total_seconds() <= 600 and trancode[in2] == '02000000':
                    if devcode[in1] == devcode[in2]:
                        count[0] = count[0] + 1
                    else:
                        count[1] = count[1] + 1

                if (t1 - t2).total_seconds() <= 24 * 3600 and trancode[in2] == '02000102':
                    count[2] = count[2] + 1

                # cash withdraw amount in 10 minutes
                if (t1 - t2).total_seconds() <= 10*60 and trancode[in2] == '02000102':
                    count[3] = count[3] + float(tranmn[in2])

                # number of transaction in 1h
                if (t1 - t2).total_seconds() <= 1*3600:
                    count[4] = count[4] +1

               # number of place where transaction took place
                if (t1 - t2).total_seconds() <= 1*3600 and lat[in1] != lat[in2] and lng[in1] != lng[in2]:
                        count[5] = count[5] + 1

                # number of transactions where money is 100 or 200 in 24h
                if (t1 - t2).total_seconds() <= 24 * 3600 and trancode[in2] == '02000102' and \
                        (tranmn[in2] == 100 or tranmn[in2] == 200):
                    count[6] = count[6] + 1

                # number of transactions where money is higher 10000 in 1 month
                if (t1 - t2).days <= 30 and trancode[in2] == '02000000' and float(tranmn[in2]) >= 10000:
                    count[7] = count[7] + 1


        ls[0][in1] = count[0]
        ls[1][in1] = count[1]
        ls[2][in1] = count[2]
        ls[3][in1] = count[3]
        ls[4][in1] = count[4]
        ls[5][in1] = count[5]
        ls[6][in1] = count[6]
        ls[7][in1] = count[7]

    df_per.insert(1, 'tran_5_pos', ls[0])
    df_per.insert(2, 'tran_5_pos_area', ls[1])
    df_per.insert(3, 'tran_dev_area', ls[2])
    df_per.insert(4, 'sum_10_cash', ls[3])
    df_per.insert(5, 'tran_hour_sum', ls[4])
    df_per.insert(6, 'tran_hour_area', ls[5])
    df_per.insert(7, 'tran_small_cash', ls[6])
    df_per.insert(8,'tran_mon_count',ls[7])
    return df_per