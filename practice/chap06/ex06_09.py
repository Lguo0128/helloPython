# 6-9 喜欢的地方：创建一个名为 favorite_places 的字典。在这个字典中，将三个
# 人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。为让这个练习更有
# 趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字
# 及其喜欢的地方打印出来。

favorite_places = {
    "adam": ["guangzhou", "shenzhen"],
    "Betty": ["shanghai"],
    "Cathy": ["beijing", "hangzhou", "foshan"],
}

for person, places in favorite_places.items():
    print("\n" + person.title() + " likes the following places:")
    for place in places:
        print("\t" + place.title())
