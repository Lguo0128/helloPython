# 10-11  喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用
# json.dump()将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打
# 印消息“I know your favorite number! It’s _____.”。

# 10-12  记住喜欢的数字：将练习 10-11 中的两个程序合而为一。如果存储了用户喜
# 欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运
# 行这个程序两次，看看它是否像预期的那样工作。

import json

file_path = "d:\\workspaces\\helloPython\\practice\\chap10\\"
file_name = "ex10_favorite_number.json"

try:
    num = input("输入喜欢的数字: ")

    with open(file_path + file_name, "w", encoding="utf8") as file_object:
        json.dump(num, file_object)

except TypeError:
    pass
else:
    print("OK, got it.")

try:
    with open(file_path + file_name, "r", encoding="utf8") as file_object:
        fav_num = json.load(file_object)
except FileNotFoundError:
    print("File not found.")
else:
    print("I know your favorite number! It’s " + fav_num)
