class A(object):
    @classmethod
    def do_your_stuff(cls):
        print ('This is A')

class B(A):
    @classmethod
    def do_your_stuff(cls):
        super(B, cls).do_your_stuff()

B.do_your_stuff()
