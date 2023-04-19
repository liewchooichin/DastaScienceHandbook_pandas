# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:20:27 2023

@author: Liew

US population: merging tables
"""

import pandas as pd

def check_nan(df_to_check):

    # check if any of the values is null,
    # then, the columns with null will be
    # processed accordingly.
    boo_val = df_to_check.isnull().any()

    print(boo_val.index.values)
    print(boo_val.values)

    col_name = []

    for i in range(0, len(boo_val)):
        if boo_val.values[i] == True:
            col_name = boo_val.index.values[i]
            print(f"{col_name} has Nan values")
    # return the bool dataframe containing the
    # col names that have null values
    return boo_val


if __name__ == "__main__":

    popu = pd.read_csv("data\state-population.csv")
    area = pd.read_csv("data\state-areas.csv")
    abbr = pd.read_csv("data\state-abbrevs.csv")

    df1 = pd.merge(popu, abbr, how='outer',
             left_on='state/region',
             right_on='abbreviation')
    df1 = df1.drop(columns='abbreviation')

    # check for null values
    check_nan(df1)

    # now, we see which rows has null values
    # locate the unique value
    # the 'population' has null value, and I need
    # the corresponding state/region name
    nul_val = df1.loc[df1['state'].isna(), 'state/region'].unique()
    print(f"{nul_val} has null state")

    # in popu dataframe, we have PR, USA
    # but, in abbreviation dataframe, we don't have
    # any values/names for PR, USA, so during the merge,
    # the state PR, USA appeared null
    # now, we assigned a state name to them
    df1.loc[df1['state/region']=='PR', 'state'] = 'Puerto Rico'
    df1.loc[df1['state/region']=='USA', 'state'] = 'United States'

    # in popu dataframe, the PR population number is nan,
    # I get the name of the state with null population,
    # and the year with the null population
    check_nan(df1)
    nul_val = df1.loc[df1['population'].isna(), 'state/region'].unique()
    print(f"{nul_val} has null population")
    nul_val = df1.loc[df1['population'].isna(), 'year'].unique()
    print(f"{nul_val} has null population")

    # now, I will merge the population with the area table,
    # merge on state name, use left table:
    # left: use only keys from left frame,
    # similar to a SQL left outer join; preserve key order.
    df2 = pd.merge(df1, area, on= 'state', how='left')
    check_nan(df2)

    # We see that our areas DataFrame does not contain the
    # area of the United States as a whole. We could insert
    # the appropriate value (using the sum of all state areas,
    # for instance), but in this case we’ll just drop the
    # null values because the population density of the
    # entire United States is not relevant to our calculation
    nul_val = df2.loc[df2['area (sq. mi)'].isna(), 'state/region'].unique()
    print(f"{nul_val} has null area")
    df2.dropna(subset=['area (sq. mi)'], inplace=True)

    # I also drop the value of PR where population=null,
    # after checking for null value, I know that there is
    # no more null value
    df2.dropna(subset=['population'], inplace=True)
    check_nan(df2)

    # Aggregation
    # find the rows in "year == 2010 & ages == 'total'"
    # year 2010 is NOT a string
    data2010 = (df2.loc[ (df2["year"] == 2010)
                        &
                        (df2["ages"] == "total")]
                )

    # set the state to be the index
    data2010.set_index('state', inplace=True)

    # I will count the population density
    # population / area
    density2010 = data2010["population"] / data2010["area (sq. mi)"]
    print("\nMost densed states: "
          f"{density2010.sort_values(ascending=False).head(3)}"
          "\nLeast densed states: "
          f"{density2010.sort_values(ascending=True).head(3)}")

