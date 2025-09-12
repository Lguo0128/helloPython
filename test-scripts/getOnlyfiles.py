# toFile = 'filenames.txt'

import os
import time

filePath = "e:\\guoyifen\\files\\"
# print(os.listdir(filePath))


for root, dirs, files in os.walk(filePath):
    # print(root,dirs,files)
    # print(root+'\t'+time.asctime(time.localtime(os.path.getmtime(root))))
    # print('---------------')
    # print(dirs)
    # print('---------------')
    for theFile in files:
        excectFile = root + "\\" + theFile
        print(
            theFile + "\t" + time.asctime(time.localtime(os.path.getmtime(excectFile)))
        )
    # print("----------Root End-----------")
print("----------All End-----------")
