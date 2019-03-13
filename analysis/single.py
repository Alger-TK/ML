import numpy as np
import pandas as pd
import json
from pandas import DataFrame, Series
from dateutil.parser import parse
from data import load_tran_data

df_per = load_tran_data(csv_name = 'df_per.csv')
df_per = df_per[['custno', 'agency_code', 'sender_id', 'unpydt', 'tranti', 'trancd', 'acctno', 'tranmn', 'mcccod',
                 'mrchcd', 'mrchad', 'status', 'area_id', 'lat', 'lng', 'devcod']]
df_per['trantime'] = df_per['unpydt'] + '/' + df_per['tranti']

def count_card(df_per = df_per):
    """
    df_per_len:length of transaction information of single customer
    df_dic: change DataFrame to dict type
    card: card list of customer
    count_card: number of card owned by customer

    """
    df_per_len = len(df_per)
    df_dic = {col: df_per[col].tolist() for col in df_per.columns}
    card = df_dic['acctno']
    count_card = len(list(set(card)))
    ls = [count_card for i in range(df_per_len)]
    df_per.insert(7, 'count_card', ls)
    return df_per


def detail_1(df_per = df_per):
    """
    ls[0]: number of transaction using same pos in 5 minutes
    ls[1]: number of transaction using different pos in 5 minutes
    ls[2]: number of cash withdraw in 5 minutes
    ls[3]: cash withdraw amount in 10 minutes
    ls[4]: number of transaction in 1h
    ls[5]: number of place where transaction took place in 1h
    ls[6]: number of transaction where money is 100 or 200 in 24h
    ls[7]: number of transaction where money is higher 10000 in 1 month

    """
    df_per_len = len(df_per)
    df_dic = {col:df_per[col].tolist() for col in df_per.columns}
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
                if (t1 - t2).days <= 30 and trancode[in2] == '02000000' and tranmn[in2] >= 10000:
                    count[7] = count[7] + 1


        ls[0][in1] = count[0]
        ls[1][in1] = count[1]
        ls[2][in1] = count[2]
        ls[3][in1] = count[3]
        ls[4][in1] = count[4]
        ls[5][in1] = count[5]
        ls[6][in1] = count[6]
        ls[7][in1] = count[7]

    df_per.insert(8, 'tran_5_pos', ls[0])
    df_per.insert(9, 'tran_5_pos_area', ls[1])
    df_per.insert(10, 'tran_dev_area', ls[2])
    df_per.insert(11, 'sum_10_cash', ls[3])
    df_per.insert(12, 'tran_hour_sum', ls[4])
    df_per.insert(13, 'tran_hour_area', ls[5])
    df_per.insert(14, 'tran_small_cash', ls[6])
    df_per.insert(15,'tran_mon_count',ls[7])
    return df_per

def detail_2(df_per = df_per):
    """
    ls[0]: maximum money in history
    ls[1]: number of transaction transform where money is highest
    ls[2]: number of cash withdraw in 5 minutes
    ls[3]: cash withdraw amount in 10 minutes
    ls[4]: number of transaction in 1h
    ls[5]: number of place where transaction took place in 1h

    """
    df_per_len = len(df_per)
    df_dic = {col:df_per[col].tolist() for col in df_per.columns}
    ls = []
    for i in range(6):
        ls.append([0 for i in range(df_per_len)])
    trantime = df_dic['trantime']
    trancode = df_dic['trancd']
    devcode = df_dic['devcod']
    card = df_dic['acctno']
    tranmn = df_dic['tranmn']
    lat = df_dic['lat']
    lng = df_dic['lng']

    for in1 in range(df_per_len):
        count = [0 for i in range(6)]
        if (in1 == 0):
            count[0] = tranmn[0]
        else:
            count[0] = max(tranmn[:in1])

        if trancode[in1] == '0046XX' and tranmn[in1] >= 20000:
            count[1] = count[1] + 1
        ls[0][in1] = count[0]
        ls[1][in1] = count[1]
        ls[2][in1] = count[2]

    df_per.insert(16, 'tran_max', ls[0])
    df_per.insert(17, 'tran_cash', ls[1])
    df_per.insert(18, 'tran_dev_area', ls[2])
    return df_per

def detail_3(df_per = df_per):
    df_per_len = len(df_per)
    df_dic = {col:df_per[col].tolist() for col in df_per.columns}
    ls = []
    for i in range(4):
        ls.append([0 for i in range(df_per_len)])
    trantime = df_dic['trantime']
    trancode = df_dic['trancode']
    tranmn = df_dic['tranmn']
    for in1 in range(df_per_len):
        count = [0 for i in range(4)]
        for in2 in range(df_per_len):
            t1 = parse(trantime[in1])
            t2 = parse(trantime[in2])

            if t1 >= t2 and (t1 - t2).days <= 90:
                if trancode[in2] == '02000000':
                    count[1] = count[1] + 1
                if trancode[in2] == '02000102':
                    max_money = tranmn[in1]
                    if tranmn[in2] > max_money:
                        max_money = tranmn[in2]
                    count[2] = max_money
                    
        ls[1][in1] = count[1]
        ls[2][in1] = count[2]

    df_per.insert(20, 'tran_pos', ls[1])
    df_per.insert(21, 'tran_atm', ls[2])





detail_3(df_per)
#df_per.to_csv('D:/code/data/df_per_new_2.csv', encoding = 'gbk', index = False)














