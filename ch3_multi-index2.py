# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 21:38:26 2023

@author: Liew

Index in pandas.Multi-index must be sorted
"""

import pandas as pd
import numpy as np

# main()
if __name__ == "__main__":

    mi_index = pd.MultiIndex.from_product(
        [
            ["s", "r", "q", "p", "g", "e", "f"], [104, 108, 107, 102]
         ],
        names = ["label", "id_num"]
         )
    data = np.random.randint(0, 50, (28, 4))
    dfa = pd.DataFrame(data, index = mi_index, columns=["M", "F", "D", "A"])

    # can only sort_index, axis=0 or axis=1, one axis at a time
    df_1 = dfa.sort_index(axis=0)
    df_2 = dfa.sort_index(axis=1)

    # sort_index in place, no return value
    dfa.sort_index(axis=0, inplace=True)
    dfa.sort_index(axis=1, inplace=True)

    # unstack
    df_3 = dfa.unstack(level=1)

    # stack
    df_4 = dfa.stack([0])



