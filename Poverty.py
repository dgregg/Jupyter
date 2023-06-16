# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 09:40:10 2021

@author: dawng
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Colorado_county_race.csv", index_col=0)

denver  = df.loc['Denver County']
print(denver.to_string())

# Compare poverty population by race
values  = denver.iloc[20:26]
print(values)
xloc = np.arange(values.size)

plt.plot(xloc, values)
plt.xticks(xloc, values.index, rotation=75)
plt.title("Denver County Poverty Population")
plt.show()

plt.title("Denver County Poverty Rate")
plt.bar(xloc, values)
plt.xticks(xloc, values.index, rotation=75)
plt.show()

# Compare poverty rate by race

values  = denver.iloc[27:33]
print(values)
xloc = np.arange(values.size)



plt.title("Denver County Poverty Rate")
plt.bar(xloc, values)
plt.xticks(xloc, values.index, rotation=75)
plt.show()


# Look at poverty rates across all counties using a color map
values = df.iloc[:, 27:33]
print(values)

# Create a pcolormesh of the 4 nutty whiskies
plt.pcolormesh(values)

print("COLUMNS", values.columns)
# Set locations and labels of X axis / labels are column names
plt.xticks(xloc, values.columns, rotation=75)

# Set locations and labels for Y Axis Whey Y labels are distillery names
ylab = values.index
print(ylab)
plt.yticks(np.array(range(ylab.size))+0.5, ylab)

# Add a color bar to show what colors mean 
plt.colorbar()

#Show the plot
plt.show()