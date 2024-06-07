
from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def display(self):
        print("hello")

class SBI(RBI):
    def display(self):
        print("SBI CLASS")
        RBI.display(self)
        # return super().display()


# sbi=SBI()
rbi=RBI()


# sbi.display()
rbi.display()

# from abc import ABC,abstractmethod 

# class A(ABC):
#     @abstractmethod
#     def display(self):
#         print("A")
# class B(A):
#     def display(self):
#         print("B")
#         A.display(self)
#         return super().display()
        
# class C(A):
#     def display(self):
#         print("C")

# # a=A()
# b=B()
# c=C()

# b.display()
# c.display()
# # a.display()

# from abc import ABC,abstractmethod

# class rbi(ABC):
#     @abstractmethod
#     def display(self):
#         print("rbi class")

# class sbi(rbi):
#     def display(self):
#         print("sbi class")
#         rbi.display(self)

# class hdfc(rbi):
#     def display(self):
#         print("hdfc class")
#         rbi.display(self)

# s=sbi()
# s.display()
# h=hdfc()
# h.display()
# r=rbi()
# r.display()

