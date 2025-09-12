# 3-9 晚餐嘉宾：在完成练习 3-4~练习 3-7 时编写的程序之一中，使用 len()打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。

invites = ["alan liu", "betty Liang", "carl tan", "derk  ma", "eric chen", "fancy Ou"]

for person in invites:
    print(person.title() + ",do you have time?")

print("Finally we invited " + str(len(invites)) + " persons.")
