# 9-13  使用OrderedDict：在练习6-4 中，你使用了一个标准字典来表示词汇表。请
# 使用 OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键—值对的
# 顺序一致。

from collections import OrderedDict


# 模块测试代码
if __name__ == "__main__":
    # 仅用于测试和演示
    vocabulary = OrderedDict()

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