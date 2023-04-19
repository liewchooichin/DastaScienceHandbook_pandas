# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 11:38:19 2023

@author: Liew
pandas - merge
"""
import pandas as pd

if __name__ == "__main__":

    df1 = pd.DataFrame(
        {'employee': ['Bob', 'Jake', 'Mona', 'Lisa', 'Tan', 'Sue', 'Lily', 'Rosie'],
         'group': ['Accounting', 'Accounting', 'Engineering', 'Engineering', 'Engineering', 'HR', 'Marketing', 'Marketing']
        }
        )
    df2 = pd.DataFrame(
        {'employee': ['Bob', 'Jake', 'Mona', 'Lisa', 'Tan', 'Sue', 'Lily', 'Rosie'],
         'hire_date': [2004, 2008, 2012, 2014, 2004, 2008, 2012, 2014]
        }
        )

    # discover that ; can be used to separate two statements
    print(df1); print(df2)

    # difference pandas.merge() and pandas.concat()
    print("\nWhen using concat(axis=0, ignore_index=True to avoid repeating indices)")
    df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
    print(df3)

    # one-to-one join
    print("\nWhen using merge()\nOne-to-one join")
    df3 = pd.merge(df1, df2)
    print(df3)

    # many-to-one join
    df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR', 'Marketing'],
'supervisor': ['Fong', 'Carly', 'Guido', 'Steve']})
    df5 = pd.merge(df3, df4)
    print("\nMany to one join")
    print(df5)

    # find the subordinates
    supervisor_name = 'Carly'
    group_list = df5[df5['supervisor'] == supervisor_name]['group']
    print("\nAssessing the elements")
    print(f"{supervisor_name} is the supervisor of {group_list.values[0]}")
    employee_list = df5[df5['supervisor'] == supervisor_name]['employee']
    # em: to try lambda function in a list
    em = [c for c in employee_list.values]
    # this print will include the []
    print(f"{[i for i in employee_list.values]}")


    # many-to-many merge
    df6 = pd.DataFrame({'group': ['Accounting', 'Accounting',
'Engineering', 'Engineering', 'HR', 'HR', 'Marketing', 'Marketing'],
                        'skills': ['math', 'spreadsheets', 'coding', 'linux',
'spreadsheets', 'organization', 'promotion', 'design']})

    df7 = pd.merge(df1, df6)
    #print("many-to-many merge")

    # reindex with a new index
    df8 = pd.concat([df7, pd.DataFrame({'employee': ['Pang'], 'group': ['Sales'], 'skills': ['selling']})], ignore_index=True)
    #print(df8)

    # who has skills='selling'
    seller = df8[df8['skills']=='selling']['employee']
    # the df.values[0] is to get the content of the list,
    # so that the print will not include the [ ] brackets
    print(f"{seller.values[0]} has selling skills")