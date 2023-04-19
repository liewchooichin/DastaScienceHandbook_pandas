# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 09:57:09 2023

@author: Liew
Concatenation in pandas
"""

import pandas as pd
import numpy as np

# make_df(): make a DataFrame in the format of
# A0, A1, A2, ...
# cols: the name of the columns
# ind: the name of the row index
# DataFrame = { cols: {contents}}
def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {
        c: [str(c) + str(i) for i in ind]
        for c in cols
    }
    return pd.DataFrame(data, ind)

if __name__ == "__main__":

    # This is what make_df() trying to write
    df_eg = pd.DataFrame( [["A0","B0"], ["A1", "B1"], ["A2", "B2"]],
                       columns=["A","B"], index=[0,1,2])
    print("This is stacking and become multi-index")
    print(df_eg.stack())

    # concat along the rows
    df_1 = make_df('ABC', range(0,3))
    df_2 = make_df('ABC', range(3,6))
    print(df_1)
    print(df_2)
    print("\nThis is concat along the rows \n")
    print(pd.concat([df_1, df_2], axis=0))
    print("\nThis is concat along the cols \n")
    print(pd.concat([df_1, df_2], axis=1))

    # pandas will concatenate duplicate index
    # and this can cause error
    df_3 = make_df("HIJK", range(0,4))
    df_4 = make_df("HIJK", range(0,4))
    print(df_3)
    print(df_4)
    print("\nThis contenation along the row \n"
          "will have duplicated indices")
    df_5 = pd.concat([df_3, df_4])
    print(df_5)

    print("\nUse pd.concat (verify_integrity = True) to raise and exception if there are duplicate indices, but this is an expensive operation")
    try:
        df_5 = pd.concat([df_3, df_4], verify_integrity=True)
    except ValueError as e:
        print("ValueError:", e)

    print("\nIgnore index = True")
    df_5 = pd.concat([df_3, df_4], ignore_index=True)
    print(df_5)

    print("\nConcat with multi-index keys")
    df_5 = pd.concat([df_3, df_4], keys=["H", "I", "J", "K"])
    print(df_5)