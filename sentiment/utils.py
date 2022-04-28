import numpy as np 
import pandas as pd
from collections import OrderedDict


def months_maping(review_month):
    
    month_No = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sept",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    
    for key, month in  month_No.items():
        if review_month == key :
            return month


