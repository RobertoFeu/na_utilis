import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
#this should be to change color
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


#sns.set()



#load file
xa_high = np.loadtxt('xa_high_food.csv', comments='#')
xa_low = np.loadtxt('xa_low_food.csv', comments='#')


 #set up nice bin widths

bins = np.arange (1700, 2501, 50)

#set up lot

#define the figure
fig, ax = plt.subplots(1, 1)

#call the axes
ax.set_xlabel('Cross-sectional area (µm$^2$)')
ax.set_ylabel('count');

#paint the data
_ = ax.hist(xa_low, bins=bins)


#safe the figure
plt.savefig('aaaa.pdf')

#this is to show the plotting in the script
plt.show()
