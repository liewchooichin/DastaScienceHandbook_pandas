# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 12:00:26 2023

@author: Liew

Vectorized string operation in pandas
"""

import pandas as pd

if __name__ == "__main__":

    ser = pd.Series(["Carrot", "Brocolli", "Wong bok", None, None, "Cauliflower", "Corn cob", "Asparagus", "1", "2", "3"])

    veg_name_len = ser.str.len()
    print(f"{veg_name_len}, type: {type(veg_name_len)}")

    print(ser.str.isalpha())
    print(ser.str.isnumeric())

    print(ser.transform(lambda i: i+"--"))


