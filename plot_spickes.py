import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
#this should be to change color
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors, rc={'axes.labelsize': 16})


#load the data and skip 2 rows

data = np.loadtxt('retina_spikes.csv', skiprows=2, delimiter=',')

#slice time all the row,
t = data[:,0]
V = data[:,1]

#build the figures
fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax.set_xlabel('t (ms)')
ax.set_ylabel('V (µV)')


#paint the data
_ = ax.plot(t, V)

#this is to show the plotting in the script
plt.show()
