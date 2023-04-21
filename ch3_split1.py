# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:02:39 2023

@author: Liew

Splitting 
"""

import pandas as pd
import numpy as np

if __name__ == "__main__":

    # creating a dataframe for
    dfa = pd.DataFrame(
        {
            "key": ["A", "B", "C", "A", "B", "C"],
            "DATA1": [0, 1, 2, 3, 4, 5],
            "DATA2": [5, 0, 3, 3, 7, 9]
        }
    )

    # sum of each key
    arr_sum = dfa.groupby("key").sum()
    print(arr_sum)

    # a dictionary to map index to a group
    # first, set the key
    df_key = dfa.set_index("key")
    mapping = {
        "A": "vowel",
        "B": "consonant",
        "C": "consonant"
    }
    # to practice changing columns name to lowercase
    # change the columns name to all lowercase
    for i in range(len(df_key.columns.values)):
        df_key.columns.values[i] = str.lower( df_key.columns.values[i])
        
    # now, I have to map the new keys to the previously set index
    df_map = df_key.groupby(mapping).sum()
    print(df_map)



    # I can also groupby on multi-index
    #df2.groupby