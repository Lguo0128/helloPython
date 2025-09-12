# 3-8 放眼世界：想出至少 5 个你渴望去旅游的地方。
#  将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
#  按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python 列表。
#  使用 sorted()按字母顺序打印这个列表，同时不要修改它。
#  再次打印该列表，核实排列顺序未变。
#  使用 sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。
#  再次打印该列表，核实排列顺序未变。
#  使用 reverse()修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
#  使用 reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
#  使用 sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
#  使用 sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。

places = ["tokyo", "singapore", "beijing", "kyoto", "washington", "new zeland"]

print("Orignal List: " + str(places))

print("Sorted List: " + str(sorted(places)))
print("List status: " + str(places))

print("Reversed sorted List: " + str(sorted(places, reverse=True)))
print("List status: " + str(places))

print("Reversed List: " + str(places.reverse()))
print("List status: " + str(places))

print("Reversed again the List: " + str(places.reverse()))
print("List status: " + str(places))

print("Sort the List: " + str(places.sort()))
print("List status: " + str(places))

print("Reversed Sort the List: " + str(places.sort(reverse=True)))
print("List status: " + str(places))
