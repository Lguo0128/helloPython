# 9-8 权限：编写一个名为Privileges 的类，它只有一个属性——privileges，其中
# 存储了练习9-7 所说的字符串列表。将方法show_privileges()移到这个类中。在Admin
# 类中，将一个 Privileges 实例用作其属性。创建一个 Admin 实例，并使用方法
# show_privileges()来显示其权限。 

# 9-9 电瓶升级：在本节最后一个electric_car.py 版本中，给Battery 类添加一个名为
# upgrade_battery()的方法。这个方法检查电瓶容量，如果它不是85，就将它设置为85。
# 创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，然后对电瓶进行升级，
# 并再次调用get_range()。你会看到这辆汽车的续航里程增加了。