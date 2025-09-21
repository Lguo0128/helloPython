# 11-1 城市和国家：编写一个函数，它接受两个形参：一个城市名和一个国家名。这
# 个函数返回一个格式为City, Country 的字符串，如Santiago, Chile。将这个函数存储
# 在一个名为city _functions.py 的模块中。
# 创建一个名为test_cities.py 的程序，对刚编写的函数进行测试（别忘了，你需要导
# 入模块unittest 以及要测试的函数）。编写一个名为test_city_country()的方法，核实
# 使用类似于'santiago'和'chile'这样的值来调用前述函数时，得到的字符串是正确的。
# 运行test_cities.py，确认测试test_city_country()通过了。

# 11-2 人口数量：修改前面的函数，使其包含第三个必不可少的形参population，并
# 返回一个格式为 City, Country – population xxx 的字符串，如 Santiago, Chile –
# population 5000000。运行test_cities.py，确认测试test_city_country()未通过。
# 修改上述函数，将形参population 设置为可选的。再次运行test_cities.py，确认测
# 试test_city_country()又通过了。
# 再编写一个名为 test_city_country_population()的测试，核实可以使用类似于
# 'santiago'、'chile'和'population=5000000'这样的值来调用这个函数。再次运行
# test_cities.py，确认测试test_city_country_population()通过了。

import unittest
from city_functions import *


class FunctionTest(unittest.TestCase):
    def test_city_country(self):
        msg = city_finctions("Santiago", "Chile")
        self.assertEqual(msg, "Santiago, Chile")
        self.assertEqual(msg, "Santiago, Chile - population 5000000")

    def test_city_country_popluation(self):
        msg = city_finctions("Santiago", "Chile", "5000000")
        self.assertEqual(msg, "Santiago, Chile - population 5000000")


unittest.main()
