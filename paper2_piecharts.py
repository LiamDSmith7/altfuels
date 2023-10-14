#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 19:33:16 2023

@author: liamsmith
"""

import numpy as np
import time 

# get the start time
st = time.time()

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Create the first DataFrame
data1 = {'fragments': ['CnH2n', 'CnH2n-1', 'CnH2n+1', 'Aromatic', 'Uncategorised'],
         'percentages': [9, 28, 56, 2, 5]}
df1 = pd.DataFrame(data1)

# Create the second DataFrame
data2 = {'fragments': ['CnH2n', 'CnH2n-1', 'CnH2n+1', 'Aromatic', 'Uncategorised', 'Alkene', 'Organosilicon', 'Oxy'],
         'percentages': [10, 27, 15, 6, 3, 19, 6, 15]}
df2 = pd.DataFrame(data2)

# Create a figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))


# Define custom colors and patterns
custom_colors = ['#006A4E', '#1B4D3E', '#17B169', '#7FFF00', 'black', 'mediumseagreen', 'royalblue', 'mediumslateblue']


custom_patterns = ['/', '\\', '.', '.', '', '', '', '']

# Plot the first pie chart with bold edges
labels1 = df1['fragments']
sizes1 = df1['percentages']
ax1 = axes[0]
ax1.pie(sizes1, labels=labels1, autopct='%1.1f%%', startangle=90, \
        wedgeprops={'linewidth': 3, 'edgecolor': 'k'}, \
            colors=custom_colors, hatch=custom_patterns, \
                textprops={'fontsize': 16})
    
ax1.set_title('Pie Chart 1')

# Plot the second pie chart with bold edges
labels2 = df2['fragments']
sizes2 = df2['percentages']
ax2 = axes[1]
ax2.pie(sizes2, labels=labels2, autopct='%1.1f%%', startangle=90, \
        wedgeprops={'linewidth': 3, 'edgecolor': 'black'}, \
            colors=custom_colors, hatch=custom_patterns, \
                textprops={'fontsize': 16})
    
ax2.set_title('Pie Chart 2', fontsize=18) 









# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()


# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', round(elapsed_time, 2), 'seconds')


# get the end time
et = time.time()

