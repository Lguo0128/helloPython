# 15-4 改进的随机漫步：在类 RandomWalk 中，x_step 和y_step 是根据相同的条件生
# 成的：从列表[1, -1]中随机地选择方向，并从列表[0, 1, 2, 3, 4]中随机地选择距离。
# 请修改这些列表中的值，看看对随机漫步路径有何影响。尝试使用更长的距离选择列表，
# 如0~8；或者将1 从x或y方向列表中删除。

# 15-5 重构：方法fill_walk()很长。请新建一个名为get_step()的方法，用于确定
# 每次漫步的距离和方向，并计算这次漫步将如何移动。然后，在 fill_walk()中调用
# get_step()两次：
# x_step = get_step()
# y_step = get_step()

# 通过这样的重构，可缩小fill_walk()的规模，让这个方法阅读和理解起来更容易。

from random import choice

import matplotlib.pyplot as plt


class RandomWalk:
    """生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步，直到列表到达指定长度
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        # 决定前进方向及沿这个方向前进的距离
        direction = choice([1, -1])
        distance = choice(list(range(9)))
        step = distance * direction
        return step


while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues)

    # 突出起点、终点
    plt.scatter(0, 0, c="green", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=100)

    # 隐藏坐标轴

    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    # plt.gca().get_xaxis().set_visible(False)
    # plt.gca().get_yaxis().set_visible(False)

    plt.axis("off")

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
