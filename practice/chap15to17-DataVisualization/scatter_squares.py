import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, s=100)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both", which="major", labelsize=14)

# 函数axis()要求提供四个值：x和y坐标轴的最小值和最大值。
plt.axis([0, 1100, 0, 1100000])

# plt.scatter(x_values, y_values, edgecolor='none', s=40)
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none", s=40)

plt.show()
