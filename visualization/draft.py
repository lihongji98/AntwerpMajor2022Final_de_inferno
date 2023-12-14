import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5', 'Category 6']
data = [4, 3, 5, 2, 4, 9]

fig, ax = plt.subplots(subplot_kw=dict(polar=True))
theta = np.linspace(0, 2*np.pi, len(categories), endpoint=False)
data += data[:1]
theta = np.concatenate((theta, [theta[0]]))

ax.plot(theta, data, label='Data')
ax.fill(theta, data, alpha=0.25)

ax.set_xticks(theta[:-1])
ax.set_xticklabels(categories)

# 显示图例
ax.legend()

# 显示雷达图
plt.show()
