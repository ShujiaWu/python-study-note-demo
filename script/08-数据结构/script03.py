'''
数据结构
'''
# -*- coding = UTF-8 -*-

set0 = set(['value0', 'value1', 'value3'])

# 判断是否在集合中

print('value1' in set0) # True

# 集合复制
set1 = set0.copy()


# 集合添加元素
set1.add('value4')

print('value4' in set0) # False
print('value4' in set1) # True

# set1 是否是 set0 的超集
print(set1.issuperset(set0))  # True

# set0 是否是 set1 的子集
print(set0.issubset(set1)) # True

# 移除集合中的元素
set0.remove('value0')
print(set0)

# set0 和 set1 的交集
print(set0 & set1)
print(set0.intersection(set1))