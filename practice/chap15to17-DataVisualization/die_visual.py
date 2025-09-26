import pygal
from die import Die

# 创建两个D6骰子
die_1 = Die(6)
die_2 = Die(10)

# 投几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# print(results)

# analysis results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# visual frequencies
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = list(range(2, max_result + 1))
hist.x_title = "Result"
hist.y_title = "Frequency of Result "

hist.add("D6+D10", frequencies)
hist.render_to_file("die_visual.svg")


# print([attr for attr in dir(hist) if 'title' in attr.lower()])
# help(hist)
