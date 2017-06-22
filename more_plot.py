import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
#this should be to change color
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

#define the figure
fig, ax = plt.subplots(1, 1)


#call the axes
ax.set_xlabel('x')
ax.set_ylabel('sin(x)');


#paint the data
_ = ax.plot (x, y, marker='.', linestyle='none')

#this is to show the plotting in the script
plt.show()
