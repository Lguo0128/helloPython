# 10-2 C 语言学习笔记：可使用方法replace()将字符串中的特定单词都替换为另一
# 个单词。下面是一个简单的示例，演示了如何将句子中的'dog'替换为'cat'：
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'

# 读取你刚创建的文件learning_python.txt 中的每一行，将其中的Python 都替换为另
# 一门语言的名称，如C。将修改后的各行都打印到屏幕上。

file_path = "d:\\workspaces\\helloPython\\practice\\chap10\\learning_python.txt"

with open(file_path, encoding="utf8") as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace("Python", "C"))
