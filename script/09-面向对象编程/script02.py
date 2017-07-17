'''
面向对象编程
'''
# -*- coding = UTF-8 -*-

class SchoolMember:
  ''' 父类，包含基础信息 '''
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def tell(self):
    print('Name:{} Age:{}'.format(self.name, self.age))

class Teacher(SchoolMember):
  ''' 子类 '''
  def __init__(self, name, age, salary):
    SchoolMember.__init__(self, name, age)
    self.salary = salary
  def tell(self):
    print('Name:{} Age:{} Salary:{}'.format(self.name, self.age, self.salary))

class Student(SchoolMember):
  ''' 子类 '''
  def __init__(self, name, age, marks):
    SchoolMember.__init__(self,name, age)
    self.marks = marks
  def tell(self):
    SchoolMember.tell(self)
    print('Marks:{}'.format(self.marks))

t = Teacher('Wusj', 27, 10000)
s = Student('Hzz', 27, 90)

t.tell()
s.tell()