# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:16:27 2023

@author: Liew
planets.csv
Practise using mapping to put distance
into categories.
"""

import numpy as np
import pandas as pd
import seaborn as sns

if __name__ == "__main__":

    # demo dataset available on seaborn
    df_planets = sns.load_dataset("planets",
                        cache=True, data_home="data/planets.csv")

    print("This 'planets' dataset gives information on "
          "planets that astronomers have discovered "
          "around other stars.")
    """
    # get the unique names of each method
    arr_method = df_planets["method"].unique()
    print("\nUnique methods used: \n"
          f"{arr_method}\n"
          f"Number of methods: {len(arr_method)}\n")
    """

    # check for null values in distance
    # df_boo: boolean dataframe to check for boolean
    # status
    # count() returns the number on non-NA values
    val_boo = df_planets["distance"].isna().any()
    count_all = df_planets["distance"].size
    count_non_na = df_planets["distance"].count()
    print(f"Total number of records: {count_all}")
    print(f"Total number non-null in the record: {count_non_na}")
    print("Percentage of non-null records: "
          f"{(count_non_na/count_all*100):.2f}%")

    # drop null values from the array
    df_planets.dropna(inplace=True, subset=["distance"])

    # Now, I will get a summary of distance with describe()
    print(df_planets["distance"].describe())

    # Use pandas.cut() to categorize the distance
    labels_distance = pd.Series(["near", "not near", "not far", "far", "very far"])
    arr_distance = pd.cut(df_planets["distance"], bins=len(labels_distance), labels=labels_distance)

    # Count the category
    dis_cat = df_planets.groupby(arr_distance)["distance"].count()
    print(f"\n{dis_cat}")

    # the number of distance category discovered by each method
    # ["method", "distance"]
    dis_met_cat = df_planets.groupby(["method", arr_distance])["distance"].count().unstack()
    print(f"\n{dis_met_cat}")



