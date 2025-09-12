# 3-5 修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
# 3-4 时编写的程序为基础，在程序末尾添加一条 print 语句，指出哪位嘉宾无法赴约。
# 修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
# 再次打印一系列消息，向名单中的每位嘉宾发出邀请。。

invites = ["alan liu", "betty Liang", "carl tan", "derk  ma", "eric chen", "fancy Ou"]

for person in invites:
    print(person.title() + ",do you have time?")

print("\n\t" + invites[3].title() + " isn't free at that time")

invites[3] = "gerk bo"

for person in invites:
    print(person.title() + ",do you have time?")
