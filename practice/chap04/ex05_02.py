# 5-2 更多的条件测试：你并非只能创建10个测试。如果你想尝试做更多的比较，可
# 再编写一些测试，并将它们加入到conditional_tests.py中。对于下面列出的各种测试，
# 至少编写一个结果为True和False的测试。
#  检查两个字符串相等和不等。
#  使用函数lower()的测试。
#  检查两个数字相等、不等、大于、小于、大于等于和小于等于。
#  使用关键字and和or的测试。
#  测试特定的值是否包含在列表中。
#  测试特定的值是否未包含在列表中。

strA = "Good"
strB = "Bad"
strC = "good"

print(strA.lower() == strC)
print(strA == strB)
print(strB != strC)

num1 = 900128
num2 = 890221
print(num1 >= num2)

listA = ["apple", "pear", "banana"]
fruit = "apple"
if fruit in listA:
    print("listA true: " + fruit)
else:
    print("listA false: " + fruit)
