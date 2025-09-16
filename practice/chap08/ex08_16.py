# 8-16  导入：选择一个你编写的且只包含一个函数的程序，并将这个函数放在另一
# 个文件中。在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import ex08_09to11


magicians = ["adam", "betty", "carl", "Dave"]
great_magicians = []

ex08_09to11.make_great(magicians, great_magicians)

print(magicians)
print(great_magicians)
