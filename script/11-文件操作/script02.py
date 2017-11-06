'''
读取一个文件，并将内容写入到另外一个文件中
'''
# -*- coding = UTF-8 -*-

import os

os.chdir('../assets')

file = open('file.txt', encoding='utf-8')
target = open('target.txt', mode='w', encoding='utf-8')

for line in file:
    target.writelines(line)

file.close()
target.close()

target = open('target.txt', encoding='utf-8')

for line in target:
    print(line, end='')

target.close()