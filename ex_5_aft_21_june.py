# 1. Generate ECDFs
x_high, y_high = bootcamp_utils.ecdf(xa_high)
x_low, y_low = bootcamp_utils.ecdf(xa_low)

# 2. Make smooth curves
x = np.linspace(1600, 2500, 400)
cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high), scale=np.std(xa_high))
cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))

# 3. Plot smooth curves in gray
fig, ax = plt.subplots(1, 1)
ax.set_xlabel('egg cross sectional area (sq. µm)')
ax.set_ylabel('CDF')
ax.plot(x, cdf_high, color='gray')
ax.plot(x, cdf_low, color='gray')

# 4. Plot ECDFs
_ = ax.plot(x_high, y_high, marker='.', linestyle='none', label='high food')
_ = ax.plot(x_low, y_low, marker='.', linestyle='none', label='low food')

# Make the legend
ax.legend(loc='lower right');

plt.show()
