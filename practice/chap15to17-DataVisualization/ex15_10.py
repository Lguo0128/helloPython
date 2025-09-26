# 15-10  练习使用本章介绍的两个库：尝试使用 matplotlib 通过可视化来模拟掷骰子
# 的情况，并尝试使用Pygal 通过可视化来模拟随机漫步的情况。


import pygal
from die import Die
from random_walk import RandomWalk
import matplotlib.pyplot as plt

# 创建D12骰子
die = Die(12)

# 投几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die.roll()
    results.append(result)

# print(results)

# analysis results
frequencies = []
max_result = die.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# visual frequencies.
# 设置绘图窗口的尺寸
plt.figure(figsize=(10, 6))

point_numbers = list(range(1, die.num_sides + 1))
plt.bar(point_numbers, frequencies)
plt.show()

# visual random walk
rw = RandomWalk(10000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))
rw_list = []

xy_chart = pygal.XY()
xy_chart.title = "XY Cosinus"

for step in point_numbers:
    # print(rw.x_values[step])
    # print(rw.y_values[step])
    rw_list.append([rw.x_values[step], rw.y_values[step]])

xy_chart.add("Random Walk", rw_list)
xy_chart.render_to_file("random_walk.svg")

# print(point_numbers)
# print(rw_list)
