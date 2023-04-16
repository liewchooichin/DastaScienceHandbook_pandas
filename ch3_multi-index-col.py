# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:52:05 2023

@author:  Liew
MultiIndex for columns
"""

import pandas as pd
import numpy as np

if __name__ == "__main__":
    # hierarchical indices and columns
    index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
    names=['year', 'visit'])

    columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
    names=['subject', 'type'])

    # mock some data for HR(heart rate) and Temp(temperature)
    # round to 1 decimal point
    data = np.round(np.random.randn(4, 6), 1)
    # start=0, every two col * 10
    data[:, ::2] *= 10
    # add 37 to all data
    data += 37

    # create the DataFrame
    health_data = pd.DataFrame(data, index=index, columns=columns)
    print(f"{health_data}")

    # get the record of only one person
    print("\nHealth data for Guido \n"
        f"{health_data['Guido']}")

    # get only the HR of Sue
    print("HR for Sue \n"
          f"{health_data.loc[ :, ('Sue', 'HR')]}")

    # get only the record for 'Bob' in 2014
    print("Record for Bob in 2014 \n"
          f"{health_data.loc[2014, 'Bob']}")
