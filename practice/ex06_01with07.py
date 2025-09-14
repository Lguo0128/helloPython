# 6-1 人：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应包含键first_name、last_name、age和city。将存储在该字典中的每项信息都
# 打印出来。

# 6-7 人：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这
# 三个字典都存储在一个名为 people 的列表中。遍历这个列表，将其中每个人的所有信
# 息都打印出来。

person = {}
person["first_name"] = "Linda"
person["last_name"] = "Guo"
person["age"] = 35
person["city"] = "Guangzhou"

print(person)

person_1 = {"first_name": "Ryan", "last_name": "Guo", "age": 37, "city": "shenzhen"}

person_2 = {"first_name": "Cathy", "last_name": "Chen", "age": 35, "city": "shenzhen"}

people = [person, person_1, person_2]
for man in people:
    for k, v in man.items():
        print(k.title() + " : " + str(v).title())
