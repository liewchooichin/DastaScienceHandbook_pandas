# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 10:42:44 2023

@author: Liew

Open Recipes
"""

import numpy as np
import pandas as pd
import json

# main()
if __name__ == "__main__":

    # When first run, there is a trailing error.
    # ValueError: Trailing data
    # it’s due to using a file in which each line
    # is itself avalid JSON, but the full file is not
    filename = 'data\openrecipes.txt'
    # Apparently each line is a valid JSON, so we’ll
    # need to string them together. One way we can do
    # this is to actually construct a string representation
    # containing all these JSON entries, and then load
    # the whole thing with pd.read_json
    with open(filename, "r") as f:
        # Extract each line
        data = (line.strip() for line in f)
        # Reformat so each line is the element of a list
        data_json = "[{0}]".format(','.join(data))

    try:
        recipes = pd.read_json(data_json)
    except ValueError as e:
        print("ValueError: ", e)

    print("Shape of the json object: ", recipes.shape)

    # print the list of columns
    print("Columns: \n", recipes.columns)

    # we will see the summary of ingredients and description
    #print(recipes["ingredients"].str.len().describe())
    #print(recipes["description"].str.len().describe())

    # see the ingredients with the max string len
    # If you want the index of the maximum, use idxmax.
    ing_max = recipes["ingredients"].str.len().max()
    # locate the row of the recipe with the max len of
    # ingredients
    ing_name = recipes["name"][np.argmax(recipes["ingredients"].str.len())]
    print(f"{ing_name} -- has the longest ingredients {ing_max}")

    # see the name with the max string len
    # If you want the index of the maximum, use idxmax.
    ing_max = recipes["name"].str.len().max()
    # locate the row of the recipe with the max len of
    # ingredients
    ing_name = recipes["name"][np.argmax(recipes["name"].str.len())]
    print(f"{ing_name} -- has the longest name {ing_max}")

    # We can do other aggregate explorations;
    # for example, let’s see how many of the recipes
    # are for breakfast and easy
    print("Number of recipes for breakfast: "
          f"{recipes.description.str.contains('[Bb]reakfast').sum()}")
    print("Number of recipes for easy: "
          f"{recipes.description.str.contains('easy').sum()}")
    print("Number of recipes for potatoes: "
          f"{recipes.description.str.contains('potato*').sum()}")
    print("Number of recipes for chicken: "
          f"{recipes.description.str.contains('chicken').sum()}")
    print("Number of recipes for cheese: "
          f"{recipes.description.str.contains('cheese').sum()}")
    print("Number of recipes for rice: "
          f"{recipes.description.str.contains('rice').sum()}")
    # Make a recipe recommendation project
    # Use a easy approach where each ingredient is matched
    # against a list of predefined ingredients
    spice_list = ['potatoes', 'rice', 'chicken', 'cheese',
                  'salt', 'sugar', 'flour',
                  'egg*', 'easy', 'breakfast']

    # make a boolean list to see if each ingredient appear
    # in the list,
    # the spice_list will become the column names for
    # the DataFrame spice_df
    import re
    spice_df = pd.DataFrame(
        dict((spice, recipes.ingredients.str.contains(spice, re.IGNORECASE))for spice in spice_list)
        )

    # now, the spice_df contains the boolean for each rows
    # whether the row contains the listed ingredients
    # now, I want to choose a recipe that contains the
    # following ingredients
    # recipe_name_list : Series
    ing_list = ["potatoes"]
    recipe_name_list = recipes.loc[spice_df[ing_list[0]]==True, "name"]
    sweet_potato_list = recipe_name_list.loc[recipe_name_list.str.contains("[Ss]weet")]
    print("Recipes with sweet potato\n", sweet_potato_list[-3:])

    # see the recipes with rice
    ing_list = ["rice", "chicken"]
    recipe_name_list = recipes.loc[
        (spice_df[ing_list[0]]==True) &
        (spice_df[ing_list[1]]==True),
        "name"
        ]
    print(f"{len(recipe_name_list)} recipes with {ing_list[0]} and {ing_list[1]}\n{recipe_name_list[-5:]}")

    # see the recipes with flour
    ing_list = ["flour", "cheese"]
    recipe_name_list = recipes.loc[
        (spice_df[ing_list[0]]==True) &
        (spice_df[ing_list[1]]==True),
        "name"
        ]
    print(f"{len(recipe_name_list)} recipes with {ing_list[0]} and {ing_list[1]}\n{recipe_name_list[-5:]}")

    # see the recipes with easy
    ing_list = ["easy", "chicken"]
    recipe_name_list = recipes.loc[
        (spice_df[ing_list[0]]==True) &
        (spice_df[ing_list[1]]==True),
        "name"
        ]
    print(f"{len(recipe_name_list)} recipes with {ing_list[0]} and {ing_list[1]}\n{recipe_name_list[-5:]}")

    # see the recipes with breakfast
    ing_list = ["easy", "breakfast"]
    recipe_name_list = recipes.loc[
        (spice_df[ing_list[0]]==True) &
        (spice_df[ing_list[1]]==True),
        "name"
        ]
    print(f"{len(recipe_name_list)} recipes with {ing_list[0]} and {ing_list[1]}\n{recipe_name_list[-5:]}")

    # see the recipes with flour
    ing_list = ["flour", "potatoes"]
    recipe_name_list = recipes.loc[
        (spice_df[ing_list[0]]==True) &
        (spice_df[ing_list[1]]==True),
        "name"
        ]
    print(f"{len(recipe_name_list)} recipes with {ing_list[0]} and {ing_list[1]}\n{recipe_name_list[-5:]}")
