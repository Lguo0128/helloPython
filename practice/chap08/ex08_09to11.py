# 8-9 魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为
# show_magicians()的函数，这个函数打印列表中每个魔术师的名字。
magicians = ["adam", "betty", "carl"]


def show_magicians(magicians):
    if magicians:
        for magician in magicians:
            print("Magician: " + magician.title())
    else:
        print("No magicians")


show_magicians(magicians)

# 8-10  了不起的魔术师：在你为完成练习 8-9 而编写的程序中，编写一个名为
# make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the
# Great”。调用函数show_magicians()，确认魔术师列表确实变了。


def make_great(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append("the Great " + current_magician)


great_magicians = []
make_great(magicians, great_magicians)

show_magicians(magicians)
show_magicians(great_magicians)

# 8-11  不变的魔术师：修改你为完成练习 8-10 而编写的程序，在调用函数
# make_great()时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后
# 的列表，并将其存储到另一个列表中。分别使用这两个列表来调用show_magicians()，
# 确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the
# Great”的魔术师名字

new_great_magicians = []
make_great(great_magicians[:], new_great_magicians)

show_magicians(great_magicians)
show_magicians(new_great_magicians)
