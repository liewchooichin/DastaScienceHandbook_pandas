# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:10:21 2023

@author: Liew
"""

from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

# input("Enter your choice of 'red', 'blue' or 'green': ")
color = Color("red")
print(f"color: {color}, type: {type(color)}")
color = Color("blue")
print(f"color: {color}, type: {type(color)}")
color = Color("green")
print(f"color: {color}, type: {type(color)}")

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")