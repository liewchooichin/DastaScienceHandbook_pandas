# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:27:04 2023

@author: Liew

Birthrate data
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    print("This is a freely available data on births in "
          "the United States, provided by the Centers for "
          "Disease Control (CDC).")
    df_birth = pd.read_csv("data/births.csv")

    # get the range of years
    arr_year = df_birth["year"].unique()
    print(f"The years are ranging from {arr_year[0]} "
          f"to {arr_year[-1]}")

    print("Let's add a decade, and take a look at male and female births as a function of decade")
    df_birth["decade"] = 10 * (df_birth["year"]//10)

    # get the unique decade
    arr_decade = df_birth["decade"].unique()
    print(f"The decades that we have are from {arr_decade[0]} "
          f"to {arr_decade[-1]}")

    # create a pivot table to look at male and female births
    pivot_fm = pd.pivot_table(
                df_birth,
                values=["births"],
                index=["decade"],
                columns=["gender"],
                aggfunc = ["sum"]
                )

    # create a ratio column in the pivot table
    # the ratio of female to male
    # pivot_fm:
    #    column name : [("sum", "births", "F")],
    #    column name : [("sum", "births", "M")]
    #pivot_fm[0]/pivot_fm[1]
    ser_ratio = pivot_fm[("sum", "births", "F")]/pivot_fm[("sum", "births", "M")]
    pivot_fm["ratio", "births", "F to M"] = ser_ratio
    print(f"\n{pivot_fm}")

    """
    With a simple pivot table and plot() method, we can   
    immediately see the annual trend in births by gender. 
    By eye, it appears that over the past 50 years male 
    births have outnumbered female births by around 5%.
    """
    sns.set() # use Seaborn styles
    pd.pivot_table(df_birth, values=["births"], index=["year"], columns=["gender"], aggfunc=["sum"]).plot()
    plt.ylabel('Total births per year');


