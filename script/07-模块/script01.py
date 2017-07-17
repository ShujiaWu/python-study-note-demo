'''
模块
'''
# -*- coding = UTF-8 -*-

import sys

# 获取脚本启动参数
print('脚本启动参数：')

for arg in sys.argv:
  print(arg)

# 打印Python的Path路径
print('Python的Path路径为：')
print(sys.path)