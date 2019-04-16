# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:37:59 2019

@author: Justin L Ross
"""

# core imported data science libraries
import pandas as pd;
import numpy as np;
import matplotlib as mpl;
import matplotlib.pyplot as plt;
import seaborn as sns;
# %matplotlib inline; # This is just for Jupyter notebook, to display graphs inline.

# extended imported data science libraries
import csv;
import seaborn as sns;
from sklearn import datasets, linear_model;
from sklearn.metrics import mean_squared_error, r2_score;


# importing data
# df = pd.read_csv("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dialect=None)
# x = np.genfromtxt("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dtype=None)
# f = open("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", 'r')
# ds = csv.reader("C:\\Users\Justin\Desktop\Datasets\Heralded Diffraction SM\0001.asc", dialect=csv.excel_tab)

# styling
plt.style.use('seaborn-whitegrid')


# The Code

fig = plt.figure() 
ax = plt.axes() 





"""
#You want to use csv.reader() with the csv.excel_tab dialect.

Examples of csv usage

"""