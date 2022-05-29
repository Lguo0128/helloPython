# 4-1 比萨：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用 for循环将每种比萨的名称都打印出来。
#  修改这个 for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
#  在程序末尾添加一行代码，它不在 for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。

pizzas = ['pizza1','pizza2','pizza3','pizza4','pizza5']

for pizza in pizzas:
    print('I like ' + pizza)

print('I really love pizza!')