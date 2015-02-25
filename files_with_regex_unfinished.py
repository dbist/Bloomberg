__author__ = 'artem'

import os, re

count = 0

for filenum in range(100):
    filename = 'file_00' + str(filenum)

    for nodenum in range(10):
        if re.match('file_00' + str(nodenum) + "\d*", filename) and filename.__len__() < 9:
            print('nodename:' + str(nodenum) + ' ' + filename)
            count = count + 1


print(count)
