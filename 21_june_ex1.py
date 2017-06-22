import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns

#open the data
data = np.loadtxt('collins_switch.csv', skiprows=2, delimiter=',')

#slice data all the row,
iptg = data[:,0]
gfp = data[:,1]

#build the figures
fig, ax = plt.subplots(1, 1, figsize=(10, 3))
ax.set_xlabel('IPTG')
ax.set_ylabel('GFP')
ax.set_xscale('log')


#paint the data
_ = ax.plot(iptg, gfp)

#this is to show the plotting in the script
plt.show()
