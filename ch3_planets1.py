# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 09:43:57 2023

@author: Liew

pandas merge, aggregation,
seaborn datasets
"""

import numpy as np
import pandas as pd
import seaborn as sns

if __name__ == "__main__":

    # demo dataset available on seaborn
    df_planets = sns.load_dataset("planets",
                        cache=True, data_home="data/planets.csv")

    print("This 'planets' dataset gives information on "
          "planets that astronomers have discovered"
          "around other stars")

    arr_method = df_planets["method"].unique()
    print("\nUnique methods used: \n"
          f"{arr_method}\n"
          f"Number of methods: {len(arr_method)}\n")

    # get a summary of the dataset
    # drop null from the dataset
    #df_planets.dropna(inplace=True)
    #print("Summary of the data:\n"
    #      f"{df_planets.describe()}")

    # iterating over the groupby object
    by_method = df_planets.groupby('method')
    arr_min = by_method['orbital_period'].min()
    arr_max = by_method['orbital_period'].max()
    print("\nShape of the groupby according to method")
    for (method, group) in by_method:
        print("{0:30s} shape={1}".format(method, group.shape))

    # how to locate the element in Series arr_min, arr_max
    """
    print("\nLocating the each method with its orbital period ")
    for i in range(0, len(arr_min)):
        name = arr_min.index.values[i]
        val = arr_min.loc[name]
        print(name, val)
    """

    # drop null from the 'orbital period'
    # group by method and see the corresponding orbital period
    # trying dropna for orbital_period column
    df1 = df_planets.dropna(subset=['orbital_period'])

    # trying to create a df with method and orbital_period
    df_orbit = pd.DataFrame(columns=['method', 'min', 'max'])
    for i in range(0, len(arr_method)):
        name = arr_method[i]
        df_orbit.loc[i, 'method'] = name
        df_orbit.loc[i, 'min'] = arr_min.loc[name]
        df_orbit.loc[i, 'max'] = arr_max.loc[name]

    print("\nOrbital period detected with each method")
    print(df_orbit)

    # transformation
    # with the null values dropped from orbital_period
    # practice lambda again
    dfx = df1.groupby('method')['orbital_period'].transform(lambda x: x-1000)




