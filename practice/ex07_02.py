# 7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一
# 条消息，指出没有空桌；否则指出有空桌。


people = input("请问有多少人用餐?\n 人数: ")
people = int(people)

if people >= 8:
    print("没有空桌")
else:
    print("有空桌")

