# 7-10 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“If
# you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。

flag = True
promote = "Thanks for taking our investigation."
promote += (
    "\n You can enter 'quit' to quit the investigation, else press enter to start: "
)
places = []

while flag:
    msg = input(promote)
    if msg != "quit":
        name = input("Please what's your name? ")
        place = input("If you could visit one place in the world, where would you go? ")
        tmp = {
            "name": name,
            "place": place,
        }
        places.append(tmp)
        continue
    else:
        break


print(places)
