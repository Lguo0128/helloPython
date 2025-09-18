# 10-8 猫和狗：创建两个文件cats.txt 和dogs.txt，在第一个文件中至少存储三只猫的
# 名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并
# 将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不存
# 在时捕获 FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地
# 方，并确认except 代码块中的代码将正确地执行。

# 10-9 沉默的猫和狗：修改你在练习10-8 中编写的except 代码块，让程序在文件不
# 存在时一言不发。

file_path = "d:\\workspaces\\helloPython\\practice\\chap10\\"
file_name_1 = "cats.txt"
file_name_2 = "dogs.txt"
file_name_3 = "fishes.txt"


def print_file(file):
    try:
        with open(file, "r", encoding="utf8") as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        # print(file + " Not exsit. Please double check the file.")
        pass
    else:
        print("\n" + contents)


print_file(file_path + file_name_1)
print_file(file_path + file_name_2)
print_file(file_path + file_name_3)
