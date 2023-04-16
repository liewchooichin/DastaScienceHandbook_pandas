# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:47:57 2023

@author: Liew

Multi-indexing
"""

import pandas as pd
import numpy as np

if __name__ == "__main__":

    index_arr = [
        ("Country_A", 2000), ("Country_A", 2010), ("Country_A", 2020),
        ("Country_B", 2000), ("Country_B", 2010), ("Country_B", 2020),
        ("Country_C", 2000), ("Country_C", 2010), ("Country_C", 2020),
        ("Country_D", 2000), ("Country_D", 2010), ("Country_D", 2020),
        ]

    multi_index = pd.MultiIndex.from_tuples(index_arr)
    print("multi_index.levels: \n"
          f"{multi_index.levels}")
    print("multi_index.labels: \n"
          f"{multi_index.levels}")

    population_arr = [
        1000, 1030, 1200,
        1540, 1500, 1490,
        3050, 3850, 3920,
        2950, 3050, 3200
        ]

    population_series = pd.Series(
        population_arr, index=multi_index, name="Population"
    )
    population_series.index.names = ["Country", "Year"]
    print(f"{population_series}")

    # aggregate some data
    popu = population_series[:, 2000].sum()
    print(f"population in year 2000: {popu}")

    popu = population_series["Country_A"].sum()
    print(f"population in Country_A from 2000 to 2020: {popu}")

    # Among these populations, people who are over 65, and under 18
    over65_arr = [
        200, 190, 180,
        210, 200, 190,
        150, 140, 130,
        210, 200, 190
        ]
    under18_arr = [
        300, 320, 340,
        280, 290, 300,
        410, 430, 450,
        110, 120, 130
        ]

    df_popu = pd.DataFrame(
            {
                'total': population_arr,
                'over65': over65_arr,
                'under18': under18_arr
            }
            , index=multi_index
        )
    print(f"{df_popu}")

    a_old = df_popu.loc["Country_A", "over65"].sum()
    a_young = df_popu.loc["Country_A", "under18"].sum()
    a_total = df_popu.loc["Country_A", "total"].sum()
    percent_old = a_old / a_total * 100
    print(f"Percent of old population = {percent_old:.0f}%")
    percent_young = a_young / a_total * 100
    print(f"Percent of young population = {percent_young:.0f}%")
