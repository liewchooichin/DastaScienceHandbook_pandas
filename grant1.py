# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 21:27:35 2023

@author: Liew
Plotting various info about a grant
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt


# Amount of grant awarded to each dept
def award_to_dept(df_grant):
    # df_grant: DataFrame for grant read from datafile

    # df_bool: masking variable
    df_bool = df_grant["Approved_Grant_Amount"].notna()

    # dfa: temporary holding var for valid grant amount
    dfa = df_grant[df_bool]

    # dfb: extract the unique department name, and then
    # the amount (sum) granted to each department.
    dfb = pd.DataFrame(
        columns = ["dept", "amount"]
        )
    dfb["dept"] = dfa["Department"].unique()

    # loop through the df for each unique department, and
    # set the total amount received by each department
    for i in range(0, len(dfb["dept"])):
        # sum the grant for a given department
        total_amount = dfa.loc[ \
                        dfa["Department"] == dfb.loc[i, "dept"], \
                        "Approved_Grant_Amount"]
        dfb.loc[i, "amount"] = np.sum(total_amount)

    print("Approved grant for each department \n"
          f"{dfb}")

    # plot a table


# Calculate the number of successful and unsuccessful
# grant application by each department.
def application_outcome(df_grant):

    # dfa: DataFrame to hold the number of outcome of application,
    # count of "Unsucessful" or "successful" for each unique department
    dfa = pd.DataFrame(
            columns=["dept", "unsuccessful", "successful", "total_application"]
        )

    # dfa["dept"] = each of the unique department
    dfa["dept"] = df_grant["Department"].unique()

    # get the count of "Unsucessful" or "successful" for each department
    for i in range(0, len(dfa["dept"])):
        # dfb: locate the department
        #print(f"i = {dfa.loc[i, 'dept']}")
        dfb = df_grant[ df_grant["Department"] == dfa.loc[i, "dept"] ]
        # Series of "Unsuccessul" outcome
        s_unsuccessful = dfb[
            dfb["Outcome_of_Application"]=="Not successful"]
        num_unsuccessful = len(s_unsuccessful)
        dfa.loc[i, "unsuccessful"] = num_unsuccessful
        # Series of "sucessful" outcome
        s_successful = dfb[
            dfb["Outcome_of_Application"]=="successful"]
        num_successful = len(s_successful)
        dfa.loc[i, "successful"] = num_successful
        # Total number of application
        dfa.loc[i, "total_application"] = num_unsuccessful + num_successful

    # find the total for each column, that is total of unsuccessful
    # against successful application.
    dfa.loc["total", "unsuccessful"] = dfa["unsuccessful"].sum()
    dfa.loc["total", "successful"] = dfa["successful"].sum()
    dfa.loc["total", "total_application"] = dfa["total_application"].sum()

    print("Outcome of grant application by each department \n"
          "(number of unsuccessful and successful application) \n"
          f"{dfa}")


# main() program
if __name__ == "__main__":
    df_grant = pd.read_excel("data/grant.xlsx",
                na_values=["-", "#VALUE!"],
                parse_dates=["Grant_Start_Date", "Grant_End_Date"])

    # Calculate the amount awarded to each department
    award_to_dept(df_grant)

    # Calculate the number of successful and unsuccessful
    # grant application by each department.
    application_outcome(df_grant)
