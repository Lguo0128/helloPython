# 9-7  管理员：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为
# 完成练习 9-3 或练习 9-5 而编写的 User  类。添加一个名为 privileges 的属性，用于存
# 储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的
# 列表。编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin
# 实例，并调用这个方法。


# 9-8 权限：编写一个名为 Privileges 的类，它只有一个属性——privileges，其中
# 存储了练习9-7 所说的字符串列表。将方法show_privileges()移到这个类中。在Admin
# 类中，将一个 Privileges 实例用作其属性。创建一个 Admin 实例，并使用方法
# show_privileges()来显示其权限。
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


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        if self.privileges:
            print("拥有以下权限： ")
            for privilege in self.privileges:
                print("\t- " + privilege)
        else:
            print("无权限")


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

# 模块测试代码
if __name__ == "__main__":
    # 仅用于测试和演示
    admin = Admin("Linda", "Guo")
    admin.privileges.show_privileges()
