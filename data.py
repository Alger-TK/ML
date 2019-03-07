#get tran data
import os
import numpy as np
import pandas as pd

def load_tran_data(csv_name, tran_path = 'D:\code\data'):
    csv_path = os.path.join(tran_path, csv_name)
    return pd.read_csv(csv_path, dtype = str)

# compute distance
def haversine(lat1, lon1, lat2, lon2):
    if (lat1 ==lat2)&(lon1 ==lon2)or(lat1==lat2==lon1==lon2==0):
        distance =0
    else:
        miles_constant = 6371
        lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
        c = 2 * np.arcsin(np.sqrt(a))
        distance = miles_constant * c
    return distance*1000*3600

#compute speed
def calDistance(log):
    list_sudu =[0]
    len_table =len(log)
    for i in range(0,len_table-1):
        if (log.iloc[i+1]['useraccount']==log.iloc[i]['useraccount']):
            time_diff = log.iloc[i+1]['reqtime']-log.iloc[i]['reqtime']
            distance = haversine(log.iloc[i]['transLat'],log.iloc[i]['transLon'],log.iloc[i+1]['transLat'],log.iloc[i+1]['transLon'])
            if distance>3:
                sudu = round(distance/time_diff,4)
                list_sudu.append(sudu)
            else:
                list_sudu.append(0)
        else:
            list_sudu.append(0)
    return list_sudu