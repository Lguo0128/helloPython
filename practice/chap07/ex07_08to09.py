# 7-8  熟食店：创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名
# 字；再创建一个名为finished_sandwiches 的空列表。遍历列表sandwich_orders，对于
# 其中的每种三明治，都打印一条消息，如I made your tuna sandwich，并将其移到列表
# finished_sandwiches。所有三明治都制作好后，打印一条消息，将这些三明治列出来。

# 7-9  五香烟熏牛肉（pastrami ）卖完了：使用为完成练习 7-8 而创建的列表
# sandwich_orders，并确保'pastrami'在其中至少出现了三次。在程序开头附近添加这样
# 的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个while 循环将
# 列表sandwich_orders 中的'pastrami'都删除。确认最终的列表finished_sandwiches 中
# 不包含'pastrami'。

sandwich_orders = [
    "tuna",
    "potato",
    "cabbage",
    "pastrami",
    "cabbage",
    "pastrami",
    "pastrami",
]
finished_sandwiches = []

while sandwich_orders:
    make = sandwich_orders.pop()
    print("I made your " + make + " sandwich")
    finished_sandwiches.append(make)

print(finished_sandwiches)

sandwich_orders = [
    "tuna",
    "potato",
    "cabbage",
    "pastrami",
    "cabbage",
    "pastrami",
    "pastrami",
]
finished_sandwiches = []

print("Sorry, 'pastrami' is out of service. ")

while "pastrami" in sandwich_orders:
    for order in sandwich_orders:
        if order == "pastrami":
            sandwich_orders.remove(order)

while sandwich_orders:
    make = sandwich_orders.pop()
    print("I made your " + make + " sandwich")
    finished_sandwiches.append(make)

print(finished_sandwiches)
