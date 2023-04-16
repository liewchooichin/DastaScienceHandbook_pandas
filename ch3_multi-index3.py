# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 22:23:12 2023

@author: Liew
Build multi-index from usual csv, excel row*column forms
"""

import numpy as np
import pandas as pd

if __name__ == "__main__":

    dfa = pd.DataFrame(
        [
             [56, 30, "Orange", "2020"],
             [53, 33, "Orange", "2021"],
             [56, 31, "Orange", "2022"],
             [50, 40, "Orange", "2023"],
             [45, 35, "Blue", "2020"],
             [48, 38, "Blue", "2021"],
             [43, 41, "Blue", "2022"],
             [49, 38, "Blue", "2023"],
             [56, 25, "Yellow", "2020"],
             [54, 29, "Yellow", "2021"],
             [60, 31, "Yellow", "2022"],
             [57, 34, "Yellow", "2023"]
         ],
        columns=["Geography", "Math", "Class", "Year"]
        )
    # set index according to class and year
    df_1 = dfa.set_index(["Class", "Year"])
    df_2 = dfa.set_index(["Year", "Class"])

    # get the average mark for every year
    avg_geo_year = df_2.groupby(level="Year").mean()
    avg_math_year = df_2.groupby(level="Year").mean()

    avg_geo_class = df_2.groupby(level="Class").mean()
    avg_math_class = df_2.groupby(level="Class").mean()

     # aggregate along the rows
    avg_score_1 = df_2.mean(axis=0)
    # aggregate along the columns
    avg_score_2 = df_2.mean(axis=1)

    # groupby() [] a list of index
    year_class = df_2.groupby(level=["Year", "Class"]).max()
