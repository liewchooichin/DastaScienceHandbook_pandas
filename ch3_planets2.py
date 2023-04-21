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

    # get the number of planets discovered in every decade
    # year // 10 to get the yyyx, then multiply this by 10
    # to get the decade.
    # to get quotient use //
    # to get remainder use %
    # or, built-in divmod()
    # in this case, use // e.g. 1994//10 = 1990,
    # 2013//10 = 2010,
    # % remainder is more suitable in cases like
    # placing values into suitable categories/slots
    year_decade = 10 * (df_planets["year"]//10)
    # now, I convert the dataframe.astype() to str
    # to make decades 1990s, 2000s, etc
    # year_decade is a Series with the same size as df_planets
    year_decade = year_decade.astype(str) + "s"

    # groupby method to count the number in each decade
    # fill null value with 0
    # df1 = the count of planets discovered by each method
    # sum the number of discovery made in each decade
    #
    # Note that the groupby (year_decade): groupby can be used
    # year_decade has the same element as df_planets[year], i.e.
    # they have the same index. So, the rows with the same index
    # will be groupby and sum
    df1 = df_planets.groupby(["method", year_decade])["number"].sum().unstack().fillna("-")
    print("Number of planets discovered each decade: \n"
          f"{df1}")

