#coding=utf-8
class A(object):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print 'A.__private()'

    def public(self):
        print 'A.public()'
    def test1(self):
        print "test1"
    def __test2(self):
        print "test2"


class B(A):
    def __private(self):
        print 'B.__private()'
    def public(self):
        print 'B.public()'


b = B()
b.test1()
#b.test2()    无法访问父类双下划线内容

#当实例化B的时候，由于没有定义__init__函数，将调用父类的__init__，但是由于双下划线的”混淆”效果，”self.__private()”将变成 “self._A__private()”。