# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:32:59 2023

@author: Liew
Pivot table
"""

import numpy as np
import pandas as pd
import seaborn as sns

if __name__ == "__main__":

    df_titanic = sns.load_dataset('titanic',
            cache=True, data_home="data/planets.csv")

    # Number of survival by sex
    print(df_titanic.groupby("sex")["survived"].count())

    arr_mean = df_titanic.groupby("sex")["survived"].mean()
    print(arr_mean)

    # Number of survival by sex and class
    print(df_titanic.groupby(["sex", "class"])["survived"].mean().unstack())

    # print the previous info by creating a pivot table
    print(
        pd.pivot_table(df_titanic, values=["survived"],
            index=["class"], columns=["sex"],
            aggfunc=["count", "mean"],
            fill_value=0,
            margins=True)
        )

    # another pivot table
    # print the previous info by creating a pivot table
    test = df_titanic.loc[df_titanic["survived"]==0,
                   ["class", "sex"]]

    # categorize into age
    # drop nan from the df_titanic["age"]
    # df.count() will give the total of non-na values
    age_count = df_titanic["age"].count()
    age_all = df_titanic['age'].size
    print(f"\nTotal number of records: {age_all}")
    print(f"Number of age with values: {age_count}")
    print(f"Percentage of valid age: {(age_count/age_all*100):.2f}%")


    df_age = df_titanic.dropna(subset=["age"])
    arr_age_cat = ["under 18", "18-60", "above 61"]
    age_cat = pd.cut(
        df_age["age"],
        labels= arr_age_cat,
        bins=len(arr_age_cat)
        )
    # people who survive according to their age category
    # what is observed??
    # It gives the same value whether observed=True or False
    print(
        pd.pivot_table(
            df_age,
            values=["class"],
            index=["sex", age_cat],
            columns=["survived"],
            aggfunc=["count"],
            observed=True
            )
        )

