# -14 骰子：模块 random 包含以各种方式生成随机数的函数，其中的randint()返回
# 一个位于指定范围内的整数，例如，下面的代码返回一个1~6 内的整数：
# from random import randint
# x = randint(1, 6)

# 请创建一个Die 类，它包含一个名为sides 的属性，该属性的默认值为6。编写一
# 个名为roll_die()的方法，它打印位于1 和骰子面数之间的随机数。创建一个6 面的骰
# 子，再掷10 次。
# 创建一个10 面的骰子和一个20 面的骰子，并将它们都掷10 次

import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        num = random.randint(1, self.sides)
        print(num)


# 模块测试代码
if __name__ == "__main__":
    # 仅用于测试和演示
    die = Die()
    print(die.sides)
    times = 0
    while times < 10:
        print("Die sides: "+ str(die.sides) +"\nRoll time: " + str(times + 1))
        die.roll_die()
        times += 1

    die_10faces = Die(10)
    print(die_10faces.sides)
    times = 0
    while times < 10:
        print("Die sides: "+ str(die_10faces.sides) +"\nRoll time: " + str(times + 1))
        die_10faces.roll_die()
        times += 1

    die_20faces = Die(20)
    print(die_20faces.sides)
    times = 0
    while times < 10:
        print("Die sides: "+ str(die_20faces.sides) +"\nRoll time: " + str(times + 1))
        die_20faces.roll_die()
        times += 1
