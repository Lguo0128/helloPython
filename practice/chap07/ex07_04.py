# 7-4 比萨配料：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入
# 'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添
# 加这种配料。

配料 = []
flag = True

while flag:
    msg = input("输入一系列的比萨配料，若输入'quit'则结束: ")
    if msg != "quit":
        配料.append(msg)
        print("我们会在比萨中添加这种配料： " + msg)
        continue
    else:
        print("比萨将中添加以下配料：")
        for k in 配料:
            print("\t" + k)
        break
