# 3-6 添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
#  以完成练习 3-4 或练习 3-5 时编写的程序为基础，在程序末尾添加一条 print 语句，指出你找到了一个更大的餐桌。
#  使用 insert()将一位新嘉宾添加到名单开头。
#  使用 insert()将另一位新嘉宾添加到名单中间。
#  使用 append()将最后一位新嘉宾添加到名单末尾。
#  打印一系列消息，向名单中的每位嘉宾发出邀请。

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
