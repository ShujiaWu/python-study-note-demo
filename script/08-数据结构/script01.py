'''
数据结构
'''
# -*- coding = UTF-8 -*-

# 数组
arr = [1, 2, 3, 4]

for item in arr:
  print(item)

# 元组
zoo = ('cat', 'dog', 'python')

for item in zoo:
  print(item)

# 字典
dic = {
  'key1': 'value1',
  'key2': 'value2'
}

print(dic['key1'])

for key, value in dic.items():
  print(key, '---', value)