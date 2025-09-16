# 8-7 专辑：编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函
# 数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑
# 的信息。
# 给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调
# 用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并
# 至少在一次调用中指定专辑包含的歌曲数。


def make_album(artist, album, song_num=""):
    if song_num:
        dict_album = {
            "artist": artist,
            "album": album,
            "song_num": int(song_num),
        }
        return dict_album
    else:
        dict_album = {
            "artist": artist,
            "album": album,
        }
        return dict_album


print(make_album("nanjo", "omg", 10))
print(make_album("nanjo", "omg2"))

# 8-8  用户的专辑：在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户
# 输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album()，并
# 将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。

flag = True
while flag:
    artist = input(
        "Please input the artist name:\n(You can quit anytime if enter 'q')\n"
    )
    if artist == "q":
        break
    album = input("Please input the album name: \n(You can quit if anytime 'q')\n")
    if album == "q":
        break
    print("\n\tThe artist is :" + make_album(artist, album)["artist"].title())
    print("\tThe album is :" + make_album(artist, album)["album"].title())
