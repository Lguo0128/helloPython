# 8-3  T 恤：编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T 恤上
# 的字样。这个函数应打印一个句子，概要地说明T 恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件T 恤；再使用关键字实参来调用这个函数。


def make_shirt(size, logo):
    """打印T-shirt尺码size，与印刷字样logo"""
    print("T-shirt size is : " + size)
    print("The logo is : " + logo)


make_shirt("S", "Winner")

# 8-4 大号T 恤：修改函数make_shirt()，使其在默认情况下制作一件印有字样“I love
# Python”的大号T 恤。调用这个函数来制作如下T 恤：一件印有默认字样的大号T 恤、
# 一件印有默认字样的中号T 恤和一件印有其他字样的T 恤（尺码无关紧要）。


def make_shirt(size="L", logo="I love Python"):
    """打印T-shirt尺码size，与印刷字样logo"""
    print("T-shirt size is : " + size)
    print("The logo is : " + logo)


make_shirt()
make_shirt("M", "Winner")
make_shirt(logo="M", size="Winner")
