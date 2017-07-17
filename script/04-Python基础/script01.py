'''
Python 基础
'''
# -*- coding = UTF-8 -*-

# 单引号、双引号、三引号

print('Hello World')

print("Hello World")

print('''
Hello World
''')

# 三引号可以进行多行输出，注意下面的输出结果：前后是有两个空行的
print('''
Hello World 0
Hello World 1
''')

# 转义字符
print("带转义字符\tO(∩_∩)O哈哈哈~")

# 双引号中可以使用单引号，而不需转义
print("双引号中带单引号 '")

# 单引号中可以使用双引号，而不需转义
print('单引号中带双引号 "')

# 换行输入，单行输出
print('单行显示单行显示单行显示单行显示\
单行显示单行显示单行显示单行显示单行显示')

# 原始字符串输出
print(r'原始输出字符串\t')

# 字符串格式化
name = '小明'
age = 20

print('{0} 今年 {1} 岁'.format(name, age))

print('{0:.3f}'.format(1.0/3))

print('{0:_^11}'.format('Hello'))

print('{name} 今年 {age} 岁'.format(name="小明", age=20))

# 改变print()函数的结束符
print('Hello', end='')

print('World', end='')