#3-7 缩减名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习 3-6 时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用 pop()不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用 del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。

invites= ['alan liu','betty Liang','carl tan','derk  ma','eric chen','fancy Ou']

for person in invites:
    print( person.title() + ',do you have time?')

print('\n\t'+invites[3].title()  + ' isn\'t free at that time')

invites[3] = 'gerk bo'

for person in invites:
    print( person.title() + ',do you have time?')

print('\n\t We get a larger table.')

invites.insert(0,'Kate pei')
invites.insert(4,'Rob pei')
invites.append('Yummm Owd')

for person in invites:
    print( person.title() + ',do you have time?')

print('\n\t The table seems can not be on time.')
print('We can only invite 2 person.')


while (len(invites) >2):
    print('sorry for '+ invites.pop())

print('\n\t Finally we will invite:')
for person in invites:
    print('\t\t'+ person.title())
