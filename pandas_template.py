# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:37:59 2019

@author: Justin L Ross

A default template for pandas to use in doing data science work.


"""

"""
# imported libraries
"""

# core data science libraries
import pandas as pd; # For dealing with data, creating dataframes, importing data.
import numpy as np; # For dealing with numbers, more efficient processing of arrays.
import matplotlib as mpl; # For creating visualizations.
import matplotlib.pyplot as plt; # For creating plots/graphs.
# %matplotlib inline; # For Jupyter notebook, to display graphs inline. Uncomment if needed.

# extended data science libraries
# import csv; # Pandas includes some csv import stuff, but sometimes pythons default is better.
import seaborn as sns; # For prettying visualizations.
from sklearn import datasets, linear_model;
from sklearn.metrics import mean_squared_error, r2_score;


"""
# importing data
"""

# df = pd.read_csv("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dialect=None)
# x = np.genfromtxt("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dtype=None)
# f = open("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", 'r')
# ds = csv.reader("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dialect=csv.excel_tab)

"""
# declaring constants
"""

"""
# declaring variables
"""


"""
# Other Statements Section
"""
# Processing the data.

fig = plt.figure() 
ax = plt.axes() 


# Presenting the data.


# styling
plt.style.use('seaborn-whitegrid')







"""
#You want to use csv.reader() with the csv.excel_tab dialect.

Examples of csv usage

"""