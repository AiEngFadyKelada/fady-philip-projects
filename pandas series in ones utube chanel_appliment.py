# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OeH9oYTese5gtgfD6PBuNWFKcfNh2Ank
"""

import numpy as np
import pandas as pd

data=pd.Series([54,95,68,32],index=['first','second','third','fourth'])
print(data,"\n")

type(data.values)
data.values
print(data[0])

population_dict ={
    "NewYork":87125387162,
    "illinois":987129837,
    "California":987294879812,
    "Los Angelos":2984698127948,
    "Florida":981729831792,
    "Texas":912804712982
}
print(population_dict,"\n")
print(population_dict["Texas"],"\n",population_dict['Florida'],"\n")
pop_series=pd.Series(population_dict)
print(pop_series,"\n")
print(pop_series["Texas"],"\n")
print(pop_series["NewYork":"California"],"\n")
print(pop_series[0:2],"\n")

















