# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:51:45 2023

@author: Liew

birthrates: Create datetime index, remove outliers
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

if __name__ == "__main__":

    print("This is a freely available data on births in "
          "the United States, provided by the Centers for "
          "Disease Control (CDC).")
    df_birth = pd.read_csv("data/births.csv")

    # In the data, from 1989, there is no more 'day'
    # information, the num of births is recorded for
    # the whole month
    # In the 'day', there are invalid values like '99',
    # June 31, Sep 31, etc
    # remove the outliers,
    # take only values from the interquartile range
    # from 25%-75%
    # sigma 0.74 is a robust estimate of the sample mean,
    # where the 0.74 comes from theinterquartile
    # range of a Gaussian distribution
    quartiles = np.percentile(df_birth["births"], [25, 50, 75])
    mu = quartiles[1] # the mean at 50%
    sig = 0.74 * (quartiles[2] - quartiles[0])

    # create a query
    #    df_births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
    df_int_qua = df_birth[ ( df_birth["births"] > (mu - (5*sig)) ) & ( df_birth["births"] > (mu + (5*sig)) )]
    print(f"Compare the original dataframe shape: {df_birth.shape} to the interquartile dataframe shape: {df_int_qua.shape}")

    # column of births with number less than 1000 contains
    # invalid date, drop these rows also
    ind_to_drop = df_birth[df_birth["births"] < 1000]
    df_day_valid = df_birth.drop(labels = ind_to_drop.index, axis=0)
    print(f"Number of rows with invalid date: {ind_to_drop.shape}")
    print(f"After dropping the rows with invalid date: {df_day_valid.shape}")

    # set 'day' column to integer; it originally was a string due to nulls
    # drop nan day from the dataframe
    df_day_valid = df_day_valid.dropna(axis=0, subset=["day"]).convert_dtypes(convert_integer=True)
    print(f"After dropping the rows with nan day: {df_day_valid.shape}")
    print("Converting the year-month-day to integer type, then change that into a new date index")
    print(f"dtype of column:day is {df_day_valid['day'].dtype}")
    print(f"dtype of column:month is {df_day_valid['month'].dtype}")
    print(f"dtype of column:year is {df_day_valid['year'].dtype}")

    # convert the year-month-day into an index
    # format, e.g. 19990228
    df_day_valid.index = (10000 * df_day_valid["year"]) + \
            (100 * df_day_valid["month"]) + \
            df_day_valid["day"]

    df_day_valid.index = pd.to_datetime(df_day_valid.index, format="%Y%m%d")
    df_day_valid["day_of_week"] = df_day_valid.index.dayofweek

    # get the decades
    df_day_valid["decade"] = 10 * (df_day_valid["year"]//10)

    # plot the number of births according to the day of week
    pivot_day_of_week = pd.pivot_table(
            df_day_valid,
            values=["births"],
            index=["day_of_week"],
            columns=["decade"],
            aggfunc=["mean"]
        )
    print(pivot_day_of_week)
    print("Number of births is usually lowest on Sat \n"
          " for these decades "
          f"{df_day_valid['decade'].unique()}")

    # plot a chart of number of births on each day of week
    plt.style.use('_mpl-gallery')
    pivot_day_of_week.plot()
    #plt.gca().set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.ylabel('mean births by day')

    # birth by date
    # this pivot table has multi-level index
    df_by_date = pd.pivot_table(df_day_valid,
                values=["births"],
                index=[df_day_valid.index.month,
                       df_day_valid.index.day],
                )

    # Make the index of the pivot table to contain
    # month-day throughout the years,
    # choose only one year to create into a datetime,
    # choose a leap year to handle Feb 29, use 1972
    # this index is a list comprehension

    #df_by_date.index = (10000*1972) + (100*range(1, 13)) + range(1, 32)
    df_by_date.index = ["1972-{0:d}-{1:d}".format(month, day) for (month, day) in df_by_date.index]
    df_by_date.index = pd.to_datetime(df_by_date.index, format="%Y-%m-%d")

    # Plot the results
    # ax: matplotlib axes object, default None
    # An axes of the current figure.
    fig, ax = plt.subplots(figsize=(12, 4))
    df_by_date.plot(ax=ax);

    print("The chart shows a dip in birthrate on US holidays \n"
          "(e.g., Independence Day, Labor Day, Thanksgiving, \n"
          "Christmas, New Year’s Day) although this likely \n"
          "reflects trends in scheduled births/n")