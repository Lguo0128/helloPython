# 10-13 验证用户：最后一个 remember_me.py 版本假设用户要么已输入其用户名，要
# 么是首次运行该程序。我们应修改这个程序，以应对这样的情形：当前和最后一次运行
# 该程序的用户并非同一个人。
# 为此，在greet_user()中打印欢迎用户回来的消息前，先询问他用户名是否是对的。
# 如果不对，就调用get_new_username()让用户输入正确的用户名。

import json

file_path = "d:\\workspaces\\helloPython\\practice\\chap10\\"
file_name = "ex10_username.json"


def get_stored_username():
    """Get stored username if available."""
    filename = file_path + file_name
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = file_path + file_name
    with open(filename, "w") as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    while True:
        check_msg = input(
            f"If your name is {username} ? \n(Print 'y' for Yes, 'n' for No )"
        )
        if check_msg == "y":
            if username:
                print(f"Welcome back, {username}!")
            else:
                username = get_new_username()
                print(f"We'll remember you when you come back, {username}!")
            break
        elif check_msg == "n":
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
            break
        else:
            print(f"Please print 'y' for Yes, 'n' for No")
            continue


greet_user()
