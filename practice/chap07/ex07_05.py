# 7-5 电影票：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；
# 3~12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问
# 用户的年龄，并指出其票价。

# 7-6 三个出口：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
#  在while循环中使用条件测试来结束循环。
#  使用变量active来控制循环结束的时机。
#  使用break语句在用户输入'quit'时退出循环。

flag = True
while flag:
    age = input(
        "电影院根据观众的年龄收取不同的票价，若输入'quit'则退出询问。\n请输入你的年龄： "
    )
    if age != "quit":
        age = int(age)
        if age < 0:
            print("请输入正确年龄！")
            continue
        elif age < 3:
            print("不到3岁的观众免费")
            continue
        elif age <= 12:
            print("3~12岁的观众为10美元")
            continue
        else:
            print("超过12岁的观众为15美元")
            continue
    else:
        print("退出咨询")
        break
