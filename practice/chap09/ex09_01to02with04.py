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

# 9-4  就餐人数：在为完成练习 9-1 而编写的程序中，添加一个名为 number_served
# 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实例；打印有
# 多少人在这家餐馆就餐过，然后修改这个值并再次打印它。 
# 添加一个名为 set_number_served()的方法，它让你能够设置就餐人数。调用这个
# 方法并向它传递一个值，然后再次打印这个值。 
# 添加一个名为 increment_number_served()的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
