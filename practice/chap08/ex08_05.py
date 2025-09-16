# 8-5 城市：编写一个名为describe_city()的函数，它接受一座城市的名字以及该城
# 市所属的国家。这个函数应打印一个简单的句子，如 Reykjavik is in Iceland。给用
# 于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城
# 市不属于默认国家。

def describe_city(country="Iceland",city="Reykjavik"):
    print(city.title() + " is in "+ country.title())

describe_city()
describe_city("China","Beijing")
describe_city(country="China",city="Tokyo")