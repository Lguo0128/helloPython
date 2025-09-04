# 4-12 使用多个循环：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用
# for 循环来打印列表。请选择一个版本的foods.py，在其中编写两个 for循环，将各个
# 食品列表都打印出来。

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print("My favorite foods are:")
for food1 in my_foods:
    print(food1)
print("\nMy friend's favorite foods are:")
for food2 in friend_foods:
    print(food2)
