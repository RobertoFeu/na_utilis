import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns


# 1. Function to compute ECDF
def ecdf(data):
    """Compute x, y values for an empirical distribution function."""
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return x, y

# 2. Load in the data sets
xa_high = np.loadtxt('xa_high_food.csv', comments='#')
xa_low = np.loadtxt('xa_low_food.csv', comments='#')

# 3. Generate ECDFS
x_high, y_high = ecdf(xa_high)
x_low, y_low = ecdf(xa_low)

# 4. Plot ECDFs
fig, ax = plt.subplots(1, 1)
ax.set_xlabel('egg cross sectional area (µm$^2$)')
ax.set_ylabel('ECDF')
_ = ax.plot(x_high, y_high, marker='.', linestyle='none')
_ = ax.plot(x_low, y_low, marker='.', linestyle='none')
ax.legend(('high food', 'low food'), loc='lower right');

plt.show()
