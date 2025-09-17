# 10-1  Python 学习笔记：在文本编辑器中新建一个文件，写几句话来总结一下你至
# 此学到的Python 知识，其中每一行都以“In Python you can”打头。将这个文件命名为
# learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。编写一
# 个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；
# 第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在 with 代码
# 块外打印它们。

file_path = "d:\\workspaces\\helloPython\\practice\\chap10\\learning_python.txt"

print("\n First")
with open(file_path, encoding="utf-8") as file_object:
    contents_1 = file_object.read()

times = 1
while times <= 3:
    print("\n" + contents_1)
    times += 1

print("\n Second")

with open(file_path, encoding="utf-8") as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n Third")

with open(file_path, encoding="utf-8") as file_object:
    contents_2 = file_object.readlines()

for lines in contents_2:
    print(lines.rstrip())
