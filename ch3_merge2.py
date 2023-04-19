# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:49:35 2023

@author: Liew
Set arithmetic on pd.join()
"""
import pandas as pd
import numpy as np

# main()
if __name__ == '__main__':

    df1 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary', 'Howie', 'Carrs', 'Ace', 'Zap'],
                        'food': ['fish', None, 'bread', None, 'soup', 'beans', 'cake']},
                       columns=['name', 'food'])

    df2 = pd.DataFrame({'name': ['Mary', 'Joseph', 'Carrs', 'Ace'],
                        'drink': ['wine', 'beer', 'tea', 'coffee']},
                       columns=['name', 'drink'])

    # discovery: using ; to separate statements on a line
    # it looks elegant to have these statements on one line
    #print(df1); print(df2); print(f"\n{pd.merge(df1, df2)}")

    # inner join
    #print(f"\nInner join\n{pd.merge(df1, df2, how='inner')}")
    #print(f"\nOuter join, sort=True\n{pd.merge(df1, df2, sort=True, how='outer')}")
    #print(f"\nMerge ordered, outer join\n{pd.merge_ordered(df1, df2, how='outer')}")

    # fill in the missing value
    df_all = pd.merge(df1, df2, sort=True, how='outer')
    print(f"\nBefore filling in missing values:\n{df_all}")
    df_fill = df_all.fillna('water')
    print(f"\nMissing values are filled in\n{df_fill}")



