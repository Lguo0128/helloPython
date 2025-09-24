# 15-1 立方：数字的三次方被称为其立方。请绘制一个图形，显示前5 个整数的立方
# 值，再绘制一个图形，显示前5000 个整数的立方值。
# 15-2 彩色立方：给你前面绘制的立方图指定颜色映射。


import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# print(x_values)
# print(y_values)

plt.plot(x_values, y_values, c="Red")

plt.show()
