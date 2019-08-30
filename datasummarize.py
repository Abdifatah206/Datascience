# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:33:33 2019

@author: Shire
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('https://raw.githubusercontent.com/LearnDataSci/article-resources/master/Essential%20Statistics/middle_tn_schools.csv')
print(df.describe())