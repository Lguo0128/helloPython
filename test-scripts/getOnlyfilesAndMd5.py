# toFile = 'filenames.txt'

import os
import time
import sys
import hashlib

filePath = r'k:\backups\1.209'
# print(os.listdir(filePath))

def get_file_md5(fname):
    m = hashlib.md5()   #创建md5对象
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)  #更新md5对象

    return m.hexdigest()    #返回md5对象

# reload(sys)
# sys.setdefaultencoding('utf-8')

for root, dirs, files in os.walk(filePath):
    # print(root,dirs,files)
    # print(root+'\t'+time.asctime(time.localtime(os.path.getmtime(root))))
    # print('---------------')
    # print(dirs)
    # print('---------------')
    for theFile in files:
        excectFile = root + '\\' + theFile
        file_md5 = get_file_md5(excectFile)
        print(theFile+'\t'+time.asctime(time.localtime(os.path.getmtime(excectFile)))+'\t'+file_md5)

    # print("----------Root End-----------")
print("----------All End-----------")
