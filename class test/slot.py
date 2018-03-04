#coding=utf-8
#from types import MethodType
'''
给类绑定动态方法methodType
class Student(object):
    pass

def set_score(self,score):
    self.score=score

if __name__ == '__main__':
    Student.set_score=MethodType(set_score,None,Student)
    s=Student()
    s.score="99"
    print s.score
'''

'''
限制class属性，只允许对student实例添加name和age属性
但是不影响继承的子类
class Student(object):
    __slots__ = ("name","age")
    pass

class GraduateStudent(Student):
    pass
    
if __name__ == '__main__':
    s = Student()
    s.name = "Michael"
    s.age = "28"
    s.score = "99" #会报错
    gs=GraduateStudent()
    gs.score="90"  #正确
'''

