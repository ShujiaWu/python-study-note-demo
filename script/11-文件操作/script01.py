'''
从文件中按行读取文件的内容
'''
# -*- coding = UTF-8 -*-

import os

# 打印当前的工作区间
print(os.getcwd())

# 切换工作区间
os.chdir('../assets')
print(os.getcwd())

# 打开文件
data = open('file.txt', encoding = 'utf-8')  # 读取文件报编码错误的时候需要制定编码格式

print(data.readline(), end='')
print(data.readline(), end='')

# 返回文件的起始位置
data.seek(0)

# 打印所有的段落
for line in data:
    print(line, end='')

# 关闭文件
data.close()