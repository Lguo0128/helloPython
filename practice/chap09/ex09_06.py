# 9-6  冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的
# 类，让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。这两个版本的
# Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为flavors 的属性，用于
# 存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个
# IceCreamStand 实例，并调用这个方法。


class Restaurant:
    """一个名为 Restaurant 的类，其方法__init__()设置两个属性：restaurant_name 和 cuisine_type。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性 restaurant_name 和 cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """打印restaurant_name 和 cuisine_type"""
        print("Restaurant name is " + self.restaurant_name)
        print("Cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        """打印一条消息，指出餐馆正在营业"""
        print("The restaurant " + self.restaurant_name.title() + " is Open.")

    def set_number_served(self, num):
        """它让你能够设置就餐人数"""
        return num

    def increment_number_served(self, num):
        """它让你能够将就餐人数递增"""
        return num


class IceCreamStand(Restaurant):
    """继承Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类的属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []


ice_cream_stand = IceCreamStand("蜜雪冰城", "饮料")
ice_cream_stand.describe_restaurant()
