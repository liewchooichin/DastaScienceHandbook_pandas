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
             [56, 42, "Orange", "2020"],
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
        columns=["Geog", "Math", "Class", "Year"]
        )
    # set index according to class and year
    df_1 = dfa.set_index(["Class", "Year"])
    df_2 = dfa.set_index(["Year", "Class"])
    print(f"Index, columns of df_1: \n{df_1.index},\n{df_1.columns}")
    print(f"Index, columns of df_2: \n{df_2.index},\n{df_2.columns}")

    # the average mark for every year
    df_avg_year = df_2.groupby(level="Year").mean()
    avg_geo_year = df_avg_year["Geog"]
    avg_math_year = df_avg_year["Math"]
    print("Average score for geography for each year \n"
          f"{avg_geo_year}")
    print("Average score for math for each year \n"
          f"{avg_math_year}")

    # the average mark for every class
    df_avg_class = df_2.groupby(level="Class").mean()
    avg_geo_class = df_avg_class["Geog"]
    avg_math_class = df_avg_class["Math"]
    print("Average score for geography for each class \n"
          f"{avg_geo_class}")
    print("Average score for math for each class \n"
          f"{avg_math_class}")

     # aggregate along the rows
    avg_score_1 = df_2.mean(axis=0)
    # aggregate along the columns
    avg_score_2 = df_2.mean(axis=1)

    # print the dataset
    #print("Data for scores according to class and year: \n"
    #      f"{dfa}")

    # to access individual element, the DataFrame.loc()
    # must follow the sequence of the index, e.g.
    # in df_2: "Year", "Class"
    # print the score for class, year

    print("Score for geography for Yellow in 2020 :"
          f'{df_2.loc[("2020", "Orange"), "Geog"]}')

    # print the max of each subject
    df_max = (df_2.groupby(level="Year").max())
    geo_max = df_max["Geog"].max()
    math_max = df_max["Math"].max()

    # return values are a multi index: ('2022', 'Yellow')
    # pandas.Index has attributes values in []
    # So, to get the string name of this values[],
    # use values[0].
    # Return the string name of this index
    geo_max_index = df_2[df_2["Geog"]==geo_max].index
    year_geo_max = geo_max_index[0][0]
    class_geo_max = geo_max_index[0][1]
    print(f"Max geography score is {geo_max} in year {year_geo_max} by class {class_geo_max}")
    # Now, which class get this score
    # return values are a multi index: ('2020', 'Orange')
    # also can use pandas.Index.values[0][0] to get the values
    math_max_index = df_2[df_2["Math"]==math_max].index
    year_math_max = math_max_index.values[0][0]
    class_math_max = math_max_index.values[0][1]
    print(f"Max math score is {math_max} in year {year_math_max} by class {class_math_max}")