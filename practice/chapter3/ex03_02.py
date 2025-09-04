# 3-2 问候语：继续使用练习 3-1 中的列表，但不打印每个朋友的姓名，而为每人打
# 印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名


names = ['alan liu', 'betty Liang', 'carl tan',
         'derk  ma', 'eric chen', 'fancy Ou']

# 按列表索引输出
print(names[0].title() + ', long time no see. How are you?')
print(names[1].title() + ', long time no see. How are you?')
print(names[2].title() + ', long time no see. How are you?')
print(names[3].title() + ', long time no see. How are you?')
print(names[4].title() + ', long time no see. How are you?')
print(names[5].title() + ', long time no see. How are you?')

# for循环输出
for x in names:
    print(x.title() + ', long time no see. How are you?')
