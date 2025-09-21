# 11-3 雇员：编写一个名为Employee 的类，其方法__init__()接受名、姓和年薪，并
# 将它们都存储在属性中。编写一个名为 give_raise()的方法，它默认将年薪增加 5000
# 美元，但也能够接受其他的年薪增加量。
# 为 Employee 编写一个测试用例，其中包含两个测试方法：test_give_default_
# raise()和 test_give_custom_raise()。使用方法 setUp()，以免在每个测试方法中都创
# 建新的雇员实例。运行这个测试用例，确认两个测试都通过了。

import unittest

from Employee import *


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Linda", "Guo", "156000")
        self.responses = [161000, 166000]

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertIn(self.employee.annual_salary, self.responses)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertIn(self.employee.annual_salary, self.responses)


unittest.main()
