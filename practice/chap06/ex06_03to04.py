# 6-3 词汇表：Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后
# 者称为词汇表。
#  想出你在前面学过的 5个编程词汇，将它们用作词汇表中的键，并将它们的含
# 义作为值存储在词汇表中。
#  以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加
# 上一个冒号，再打印词汇的含义；也可在一行打印词汇，再使用换行符（\n）
# 插入一个空行，然后在下一行以缩进的方式打印词汇的含义。

# 6-4 词汇表 2：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写
# 的代码，将其中的一系列print语句替换为一个遍历字典中的键和值的循环。确定该循
# 环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些
# 新术语及其含义将自动包含在输出中。

vocabulary = {}

vocabulary["add"] = "增加"
vocabulary["del"] = "删除"
vocabulary["remove"] = "移除"
vocabulary["update"] = "更新"
vocabulary["insert"] = "插入"

print("add means " + vocabulary["add"] + " in chinese.\n")
print("del means " + vocabulary["del"] + " in chinese.\n")
print("remove means " + vocabulary["remove"] + " in chinese.\n")
print("update means " + vocabulary["update"] + " in chinese.\n")
print("insert means " + vocabulary["insert"] + " in chinese.\n")

for eng, chn in vocabulary.items():
    print("\t" + eng.title() + " means " + chn + " in chinese.\n")
