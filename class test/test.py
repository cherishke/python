#coding=utf-8

#参考博客：http://python.jobbole.com/82297/

class Student(object):
    count=0
    books=[]
    #实例方法（第一个参数必须是self）
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__address="Shanghai"
    def printInstanceInfo(self):
        print "%s is %s years old" %(self.name,self.age)

    #类方法（以cls作为第一个参数，cls表示类本身，定义时使用@classmethod装饰器。通过cls可以访问类的相关属性。）
    @classmethod
    def printClassInfo(cls):
        print(cls.__name__)
        print(dir(cls))

    #静态方法（静态方法没有参数限制，既不需要实例参数，也不需要类参数，定义的时候使用@staticmethod装饰器。）
    @staticmethod
    def printClassAttr():
        print Student.count
        print Student.books
    pass


if __name__ == '__main__':
    Student.books.extend(["python","java"])
    print "Student books list:%s" %Student.books
    Student.hobbies=["reading","jogging","swimming"]
    print("Student hobby list:%s"%Student.hobbies)
    print dir(Student)

    wilber=Student("wilber",28)
    print wilber._Student__address   #私有化属性访问方式
    wilber.printInstanceInfo()
    print "%s is %d years old" %(wilber.name,wilber.age)
    #类方法可以通过实例访问，也可以通过类名访问
    Student.printClassInfo()
    wilber.printClassInfo()
    #静态方法可以通过实例访问，也可以通过类名访问
    Student.printClassAttr()
    wilber.printClassAttr()

    wilber.books.append("C#")
    wilber.books=["c#"]
    #如果是append，把类中的books也变了，其他实例的books也被改变
    #如果是赋值=，则只改变当前实例的books
    wilber.score=90
    print wilber.books
    print wilber.score

    will=Student("will",27)
    print will.books
    will.count=1
    print "student.count is wilber.count:",Student.count is will.count
    del will.count
    print "student.count is wilber.count:", Student.count is will.count

