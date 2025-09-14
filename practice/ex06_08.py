# 6-8 宠物：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在
# 每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets的列
# 表中，再遍历该列表，并将宠物的所有信息都打印出来。

cat = {
    "name": "kitty",
    "master": "Adam",
}

dog = {
    "name": "旺财",
    "master": "狗剩",
}

bird = {
    "name": "八爷",
    "master": "老头",
}

pets = [cat, dog, bird]

for pet in pets:
    print("Pet's name: " + pet["name"].title())
    print(pet["name"].title() + "'s master is : " + pet["master"].title() + "\n")
