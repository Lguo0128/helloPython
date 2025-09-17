# 10-3  访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写
# 入到文件guest.txt 中。

file_path = "d:\\workspaces\\helloPython\\practice\\chap10\\"
file_name = "guest.txt"

with open(file_path + file_name, "w", encoding="utf8") as file_object:
    msg = input("Please enter your name: ")
    file_object.write(msg)

with open(file_path + file_name, encoding="utf8") as file_object:
    contents = file_object.read()

print(contents)
