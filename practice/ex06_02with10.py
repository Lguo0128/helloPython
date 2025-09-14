# 6-2 喜欢的数字：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，
# 并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存储
# 在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保
# 数据是真实的。

# 6-10 喜欢的数字：修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢
# 的数字，然后将每个人的名字及其喜欢的数字打印出来。

import random

favorite_num = {"Adam": 777, "Betty": 666, "Carl": 128, "David": 999, "Eric": 000}

print("Adam's favorite num is : " + str(favorite_num["Adam"]))
print("Betty's favorite num is : " + str(favorite_num["Betty"]))
print("Carl's favorite num is : " + str(favorite_num["Carl"]))
print("David's favorite num is : " + str(favorite_num["David"]))
print("Eric's favorite num is : " + str(favorite_num["Eric"]))

# 6-10
print(favorite_num)
for person in favorite_num.keys():
    tmp = [favorite_num[person]]
    tmp.append(random.randint(0, 1000))
    favorite_num[person] = tmp
    print(person.title() + "'s favorite nums are : " + str(favorite_num[person]))
