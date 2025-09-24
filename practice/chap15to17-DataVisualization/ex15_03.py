# 15-3 分子运动：修改 rw_visual.py，将其中的 plt.scatter()替换为plt.plot()。为
# 模拟花粉在水滴表面的运动路径，向 plt.plot()传递 rw.x_values 和 rw.y_values，并
# 指定实参值linewidth。使用5000 个点而不是50 000 个点。

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸 
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues)

    plt.plot(rw.x_values, rw.y_values)

    # 突出起点、终点
    # plt.plot(0, 0, c="green", s=100)
    # plt.plot(rw.x_values[-1], rw.y_values[-1], c="red", s=100)

    # 隐藏坐标轴

    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    # plt.gca().get_xaxis().set_visible(False)
    # plt.gca().get_yaxis().set_visible(False)

    # plt.axis("off")


    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
