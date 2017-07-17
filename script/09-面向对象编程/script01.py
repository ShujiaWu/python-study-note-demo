'''
面向对象编程
'''
# -*- coding = UTF-8 -*-

# class Person:
#   pass # 空对象要以pass结束

# p = Person()

# print(p)


# class Person:
#   def say_hi (self):
#     print('Hi')

# p = Person()

# p.say_hi()


class Person:
  nationality = '中国' # 类变量

  def say_hi (self):  # 对象方法
    print('Hi')

  def set_name (self, name):  # 对象方法
    self.name = name  # 对象变量

  @classmethod
  def get_nationality(cls): # 类方法
    print(cls.nationality)

p = Person()

p.say_hi()  # 调用对象方法

p.set_name('Wusj')  # 调用对象方法

print(p.name) # 对象变量

p.__class__.get_nationality() # 调用类方法
Person.get_nationality()      # 调用类方法
