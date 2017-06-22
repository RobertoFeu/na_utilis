import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

sns.set()
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


#this is to show the plotting in the script
plt.show()
