# 3-1 姓名：将一些朋友的姓名存储在一个列表中，并将其命名为 names。依次访问
# 该列表中的每个元素，从而将每个朋友的姓名都打印出来。

names = ['alan liu','betty Liang','carl tan','derk  ma','eric chen','fancy Ou']

# 按列表索引输出
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())

# for循环输出
for x in names:
    print(x.title())