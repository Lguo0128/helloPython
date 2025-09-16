# 4-8 立方：将同一个数字乘三次称为立方。例如，在 Python中，2的立方用 2**3
# 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for循
# 环将这些立方数都打印出来。

list_num = range(1, 11)

for value in list_num:
    print(value**3)
