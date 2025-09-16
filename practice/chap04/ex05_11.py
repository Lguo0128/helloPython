# 5-11 序数：序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3
# 例外。
#  在一个列表中存储数字1~9。
#  遍历这个列表。
#  在循环中使用一个if-elif-else结构，以打印每个数字对应的序数。输出内容
# 应为1st、2nd、3rd、4th、5th、6th、7th、8th和 9th，但每个序数都独占一行。

list_num = list(range(1, 10))
print(list_num)
for num in list_num:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")
