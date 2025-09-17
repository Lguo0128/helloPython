# 10-5 关于编程的调查：编写一个while 循环，询问用户为何喜欢编程。每当用户输
# 入一个原因后，都将其添加到一个存储所有原因的文件中。

file_path = "d:\\workspaces\\helloPython\\practice\\chap10\\"
file_name = "reason.txt"

with open(file_path + file_name, "w", encoding="utf8") as file_object:
    flag = True
    while flag:
        promote = "Why you like programming?\n（You can quit at anytime if enter 'q'）\n"
        msg = input(promote)
        if msg != "q":
            file_object.write(msg + "\n")
            continue
        else:
            break

with open(file_path + file_name, encoding="utf8") as file_object:
    contents = file_object.read()

print(contents)