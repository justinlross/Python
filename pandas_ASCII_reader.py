# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:37:59 2019

@author: Justin L Ross
"""

# default imported data science libraries
import pandas as pd;
import numpy as np;
import matplotlib as mpl;
import matplotlib.pyplot as plt;

# expanded imported libraries
import csv



# importing data
#df = pd.read_csv("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dialect=None)
# x = np.genfromtxt("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dtype=None)
#f = open("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", 'r')

ds = csv.reader("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dialect=csv.excel_tab)

# styling
plt.style.use('seaborn-whitegrid')


# Teh Code

fig = plt.figure() 
ax = plt.axes() 

print(ds)

"""
#You want to use csv.reader() with the csv.excel_tab dialect.

Examples of csv usage

"""