# 4-5 计算1~1 000 000的总和：创建一个列表，其中包含数字1~1 000 000，再使用
# min()和 max()核实该列表确实是从1开始，到1 000 000结束的。另外，对这个列表调
# 用函数sum()，看看Python将一百万个数字相加需要多长时间。 

list_num=range(1,1000001)

print(min(list_num))
print(max(list_num))
print(sum(list_num))
