# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:11:43 2023

@author: Liew
Revision of basic concepts of pandas' data structure.
Missing data.
"""
import numpy as np
import pandas as pd
import datetime

if __name__ == "__main__":

    s_animal = pd.Series(
        ["zebra", "camel", "boa constrictor", "stingray"],
        index = ['a1', 'a2', 'a3', 'a4']
        )

    print(f"{s_animal.index=}")
    print(f"{s_animal.values=}")

    fruit_name = ['guava', 'papaya', 'apple', 'banana', 'plum']
    price = [2.65, 3.25, 3.85, 3.25, 4.45]
    df_fruit = pd.DataFrame(
        {
        'fruit': fruit_name,
        'price': price
        }
        )
    print(df_fruit)

    vege_name = ['veg1', 'veg2', 'veg3', 'veg4', 'veg5']
    idx_vege = pd.Index(vege_name)
    print(idx_vege)
    df_fruit.index = idx_vege
    print(df_fruit)

    print(f"{df_fruit.fruit=}")
    print(f"{df_fruit.fruit.values=}")
    if 'banana' in df_fruit["fruit"].values:
        print("Yes, there is banana.")
    else:
        print("No, there is no banana.")

    a = df_fruit.loc['veg3', 'fruit']
    print(f"{a=}")

    df_fruit["volume"] = [168, 39.4, 102, 87, 148]
    df_fruit["total"] = df_fruit["price"] * df_fruit["volume"]

    # Add column, None and np.nan for unknown value
    df_fruit["origin"] = [None] * 5
    df_fruit["cost"] = [np.nan] * 5

    # How does np.nan affect aggregte?
    # np.nan is ignored in pandas
    df_fruit.loc["veg1", "cost"] = 3.0
    df_fruit.loc["veg2", "cost"] = 4.0
    df_fruit.loc["veg3", "cost"] = 3.0
    val_max = df_fruit["cost"].max()
    val_sum = df_fruit["cost"].sum()

    # How does None affect DataFrame?
    df_fruit.loc["veg3", "origin"] = "Vietnam"
    df_fruit.loc["veg4", "origin"] = "Malaysia"
    df_fruit.loc["veg5", "origin"] = "Philipines"
    val_nul = df_fruit[df_fruit["origin"].isnull()]
    print(f"\nval_null: \n{val_nul}")

    val_valid = df_fruit[df_fruit["origin"].notnull()]
    print(f"\nval_valid: \n{val_valid}")

    # dropna()
    dfa = df_fruit.dropna()
    print(f"{dfa=}")

    # Only this columns is considered,
    # like pd.Series
    dfa = df_fruit["fruit"].dropna()
    print(f"{dfa=}")

    # define which columns to look for missing values
    dfa = df_fruit.dropna(subset=["origin"])
    print(f"{dfa=}")

    # add a datetime column
    df_fruit["delivered"] = [
        datetime.datetime(2023, 3, 2),
        datetime.datetime(2023, 3, 3),
        pd.NaT,
        datetime.datetime(2023, 2, 28),
        datetime.datetime(2023, 4, 1)
        ]
    print(f"{df_fruit}")

    # fill in missing values
    df_filled = df_fruit["origin"].fillna("unknown")
    print(f"{df_filled}")

    df_filled = df_fruit.fillna(method="ffill")
    print(f"{df_filled}")


