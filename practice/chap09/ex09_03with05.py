# 9-3 用户：创建一个名为User 的类，其中包含属性first_name 和last_name，还有
# 用户简介通常会存储的其他几个属性。在类User 中定义一个名为describe_user()的方
# 法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化
# 的问候。
# 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """打印用户信息摘要"""
        print("First name is: " + self.first_name)
        print("Last name is: " + self.last_name)

    def greet_user(self):
        """向用户发出个性化的问候"""
        full_name = self.first_name.title() + " " + self.last_name.title()
        print("Hello, " + full_name)

    def increment_login_attempts(self):
        """将属性login_attempts 的值加 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """将属性login_attempts 的值重置为0"""
        self.login_attempts = 0


user_1 = User("james", "guo")
user_2 = User("ryan", "smith")
user_3 = User("zorah", "Lee")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

# 9-5  尝试登录次数：在为完成练习 9-3 而编写的 User 类中，添加一个名为
# login_attempts 的属性。编写一个名为increment_login_attempts()的方法，它将属性
# login_attempts 的值加 1。再编写一个名为 reset_login_attempts()的方法，它将属性
# login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts()多次。打印属
# 性login_attempts 的值，确认它被正确地递增；然后，调用方法reset_login_attempts()，
# 并再次打印属性login_attempts 的值，确认它被重置为0。

user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)
