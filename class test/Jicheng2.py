#coding=utf-8
#参考链接：http://python.jobbole.com/82308/?utm_source=blog.jobbole.com&utm_medium=relatedPosts

class Parent(object):
    '''
    parent class
    '''
    numList=[]
    #__slots__ = ("data")
    def __init__(self,data):
        self.data=data
        print "create an instance of:",self.__class__.__name__
        print "data attribute is:",self.data
    def numAdd(self,a,b):
        return a+b

class Child(Parent):
    def __init__(self):
        print "call __init__ from Child class"
        super(Child, self).__init__("data from Child")
    pass

if __name__ == '__main__':
    c=Child()
    #call __init__ from Child class
    #create an instance of: Child
    #data attribute is: data from Child
    Child.numList.append(range(10))
    print(Parent.numList)
    print Child.numList

    print "2+5=",c.numAdd(2,5)

    print issubclass(Child,Parent)
    print issubclass(Child,object)

    print Parent.__doc__   #parent class
    print Child.__doc__    #none  文档字符串对于类，函数/方法，以及模块来说是唯一的，也就是说__doc__属性是不能从父类中继承来的

    c.score=100
    print c.score