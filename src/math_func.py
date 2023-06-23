import numpy as np

def euc_distance(lat1, long1, lat2, long2):
    dis = np.sqrt((lat1-lat2)**2+(long1-long2)**2)
    return dis
    