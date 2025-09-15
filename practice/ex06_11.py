# 6-11 城市：创建一个名为cities的字典，其中将三个城市名用作键；对于每座城
# 市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市
# 的事实。在表示每座城市的字典中，应包含country、population和fact等键。将每座
# 城市的名字以及有关它们的信息都打印出来。

cities = {}
cities["shenzhen"] = {
    "country": "china",
    "population": "17989.5k",
    "fact": "technical city",
}

cities["beijing"] = {
    "country": "china",
    "population": "21832k",
    "fact": "capital city",
}

cities["tokyo"] = {
    "country": "japan",
    "population": "14.3 million",
    "fact": "capital city",
}

for city in cities.keys():
    print(city.title() + "'s info: ")
    print("\tCountry: " + cities[city]["country"].title())
    print("\tPopulation: " + cities[city]["population"].title())
    print("\tFact: " + cities[city].get("fact").title())
