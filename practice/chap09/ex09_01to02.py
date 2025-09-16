# 9-1  餐馆：创建一个名为 Restaurant 的类，其方法__init__()设置两个属性：
# restaurant_name 和 cuisine_type。创建一个名为 describe_restaurant()的方法和一个
# 名为 open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，
# 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述
# 两个方法。


class Restaurant:
    """一个名为 Restaurant 的类，其方法__init__()设置两个属性：restaurant_name 和 cuisine_type。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性 restaurant_name 和 cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """打印restaurant_name 和 cuisine_type"""
        print("Restaurant name is " + self.restaurant_name)
        print("Cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        """打印一条消息，指出餐馆正在营业"""
        print("The restaurant " + self.restaurant_name.title() + " is Open.")


restaurant_1 = Restaurant("rest a", "fruit")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()


# 9-2  三家餐馆：根据你为完成练习9-1 而编写的类创建三个实例，并对每个实例调
# 用方法describe_restaurant()。

restaurant_2 = Restaurant("rest b", "fish")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("rest C", "fish1")
restaurant_3.describe_restaurant()

restaurant_4 = Restaurant("rest d", "fish2")
restaurant_4.describe_restaurant()