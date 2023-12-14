import numpy as np
import matplotlib.pyplot as plt


def gaussian_distribution(x, y, mu_x, mu_y, sigma_x, sigma_y):
    exponent = -0.5 * ((x - mu_x) ** 2 / sigma_x ** 2 + (y - mu_y) ** 2 / sigma_y ** 2)
    return np.exp(exponent) / (2 * np.pi * sigma_x * sigma_y)


# 定义高斯分布的参数
mu_x, mu_y = 0, 0  # 圆心的坐标
sigma_x, sigma_y = 50, 50  # 标准差

# 生成二维平面上的点
x = np.linspace(0, 1024, 1024)
y = np.linspace(0, 1024, 1024)
x, y = np.meshgrid(x, y)

# 计算每个点上的高斯分布值
z = gaussian_distribution(x, y, mu_x, mu_y, sigma_x, sigma_y)
print(z)
# 画图
plt.imshow(z, origin='lower', cmap='coolwarm')
plt.colorbar(label='Probability Density')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gaussian Distribution')

plt.show()
