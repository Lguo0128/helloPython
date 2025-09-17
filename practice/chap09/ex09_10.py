# 9-10 导入Restaurant 类：将最新的Restaurant 类存储在一个模块中。在另一个文
# 件中，导入Restaurant 类，创建一个Restaurant 实例，并调用Restaurant 的一个方法，
# 以确认import 语句正确无误。

from ex09_06 import Restaurant

restaurant = Restaurant("pizzahut","ice")

restaurant.describe_restaurant()
