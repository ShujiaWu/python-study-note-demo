'''
读取一个文件，并将内容写入到另外一个文件中
'''
# -*- coding = UTF-8 -*-

import os

os.chdir('../assets')

file = open('file.txt', encoding='utf-8')
target = open('target.txt', mode='w+', encoding='utf-8')

for line in file:
    target.writelines(line)

target.seek(0)

for line in target:
    print(line, end='')

file.close()
target.close()