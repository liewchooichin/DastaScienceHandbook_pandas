# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 08:45:22 2023

@author: Liew

String vectorized operation
"""

import pandas as pd

if __name__ == "__main__":

    df_person = pd.DataFrame(
        {"first": ["f1", "f2", "f3", "f4", "f5", "f6", ],
         "last": ["la1", "la2", "la3", "la4", "la5", "la6"],
         "email":["p1@email.com", "p2@somemail.com",
                  "p3@email.com", "p4@somemail.com",
                  "p5@email.com", "p6@somemail.com"]
         },
        index=["p1", "p2", "p3", "p4", "p5", "p6"]
        )

    print("pandas string vectorized operation")
    print(df_person)
    arr_f = df_person.get(["first", "email"])
    print("pd.DataFrame.loc(index, column) locates using element names, \n"
          "but get([col, col]) is used with column names")
    arr_col = df_person.columns
    print(f"columns: \n{arr_col}")
    arr_ind = df_person.index
    print(f"index: \n{arr_ind}")

    arr_1 = df_person.loc["p4":"p6", "email"]
    arr_2 = df_person.loc["p2", "last"]
    arr_first = df_person.get(["last", "email"])

    df_person["full_name"] = df_person["last"].str.cat(df_person["first"], sep=", ")
    print("pd.DataFrame.str.cat() to concatenate two strings")
    print(df_person)

    boo = df_person["email"].str.contains("@")

