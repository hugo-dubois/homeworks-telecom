# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 08:43:44 2021

@author: hugod
"""


import pandas as pd

dataset = pd.read_csv("DataHugoDubois.csv", sep = ",", dtype=str, encoding="utf-8")
for i in range (1000):
    dataset['price'][i]= float(dataset['price'][i][1:].replace(",","."))
    

info_max = dataset[dataset['price'] == dataset['price'].max()] #how to obtain max
info_min = dataset[dataset['price'] == dataset['price'].min()] #min


test =dataset.agg({"car_year" : ["min", "max", "median"]}) #other method to obtain same value


color_price = dataset[["color", "price"]] #display a certain number of columns