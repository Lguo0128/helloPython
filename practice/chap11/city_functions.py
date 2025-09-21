def city_finctions(city, country, population=""):
    """接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为City, Country 的字符串，如Santiago, Chile。\n可选参数population，返回'City, Country – population xxx 的字符串'"""
    if population:
        msg = city + ", " + country + " - population " + str(population)
    else:
        msg = city + ", " + country
    return msg
