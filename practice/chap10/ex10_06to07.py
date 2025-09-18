# 10-6  加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是
# 文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发TypeError 异
# 常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
# 任何一个值不是数字时都捕获TypeError 异常，并打印一条友好的错误消息。对你编写
# 的程序进行测试：先输入两个数字，再输入一些文本而不是数字。

# 10-7  加法计算器：将你为完成练习 10-6 而编写的代码放在一个 while 循环中，让
# 用户犯错（输入的是文本而不是数字）后能够继续输入数字。

print("EX10-6:\n请输入两个数字，将输出相加后的结果。")

try:
    first_num = float(input("请输入第一个数字： "))
    second_num = float(input("请输入第二个数字： "))
except ValueError:
    print("\t请输入数字!")
else:
    print(str(first_num + second_num))


print("EX10-7:\n请输入两个数字，将输出相加后的结果。")

while True:
    try:
        first_num = float(input("请输入第一个数字： "))
        second_num = float(input("请输入第二个数字： "))
    except ValueError:
        print("\t请重新输入数字!")
        continue
    else:
        print(str(first_num + second_num))
        break
