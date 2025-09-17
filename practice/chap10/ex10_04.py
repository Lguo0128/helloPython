# 10-4 访客名单：编写一个while 循环，提示用户输入其名字。用户输入其名字后，
# 在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。确保这个
# 文件中的每条记录都独占一行。

file_path = "d:\\workspaces\\helloPython\\practice\\chap10\\"
file_name = "guest_book.txt"

with open(file_path + file_name, "w", encoding="utf8") as file_object:
    flag = True
    while flag:
        promote = "Please enter your name:\n（You can quit at anytime if enter 'q'）\n"
        msg = input(promote)
        if msg != "q":
            greet = "Hello " + msg.title() + ", welcome!\n"
            print(greet)
            file_object.write(greet)
            continue
        else:
            break

with open(file_path + file_name, encoding="utf8") as file_object:
    contents = file_object.read()

print(contents)
