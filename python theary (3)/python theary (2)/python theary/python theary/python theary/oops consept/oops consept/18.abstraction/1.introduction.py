
"""
Abstraction:
===========

==> which is represent only few infomation not allocated background information

==> if we want to achieve abstraction need to use abstract class

"""
from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def display(self):
        print("Class A")
class B(A):
    def display(self):
        A.display(self)
        print("Class B")
class C(A):
    def display(self):
        A.display(self)
        print("Class C")    
# a=A()
b=B()
c=C()

# a.classA()
# b.display()
# b.display()
# c.display()
# c.display()

