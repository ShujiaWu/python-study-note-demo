'''
函数
'''
# -*- coding = UTF-8 -*-

def say_hello ():
  print('Hello World')

say_hello()

def func(a, b = 10, c = 20):
  print(a, b, c)

# 普通调用
func(1, 2, 3)
# 使用默认参数
func(1)
# 使用关键字
func(a = 30, b = 30)


def func1(a, *b, **c):
  print(a)

  # 遍历元组
  for item in b:
    print(item)
  
  # 遍历字典
  for part0, part1 in c.items():
    print(part0, '---', part1)


func1(1, 2, 2, 2, v0 = 'value0', v1 = 'value1', v2 = 'value2')
