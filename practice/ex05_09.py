# 5-9 处理没有用户的情形：在为完成练习5-8编写的程序中，添加一条if语句，检
# 查用户名列表是否为空。
#  如果为空，就打印消息“We need to find some users!”。
#  删除列表中的所有用户名，确定将打印正确的消息。

import random

userList = ['admin', 'guoyifen', 'Linda', 'Ryan', 'James']

id = random.randint(0, 4)
if userList:
    if userList[id] == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + userList[id]+", thank you for logging in again")
else:
    print("We need to find some users!")


userList = []

if userList:
    if userList[id] == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + userList[id]+", thank you for logging in again")
else:
    print("We need to find some users!")
