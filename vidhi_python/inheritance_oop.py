"""Inheritance:
===========

==> one class derived properties of another class

==> inheritance

class A
   |
   V
class B   

types of inheritnance:
===== == ============

1. ==> single inheritance

2. ==> multiple inheritance

3. ==> multi-level inheritance

4. ==> hierachical inheritance

5. ==> hybrid inheritance

"""

# single inheritance
# class A:
#     def displayA(self):
#         print("A class is here")

# class B(A):
#     def displayB(self):
#         print("B class is here")

# b=B()

# b.displayA()
# b.displayB()

#====================================

# multi level inheritance


# class A:
#     def display(self):
#         print("A")

# class B(A):
#     def display1(self):
#         print("B")
    
# class C(B):
#     def display2(self):
#         print("C")

# c=C()

# c.display()
# c.display1()
# c.display2()

#===========================================
# multiple inheritance
# class A():
#     def display(self):
#         print("A")

# class B():
#     def display1(self):
#         print("B")

# class C():
#     def display2(self):
#         print("C")

# class D(A,B,C):
#     def display3(self):
#         print("D")

# d=D()

# d.display()
# d.display1()
# d.display2()
# d.display3()
#==============================================
# Hierarchical inheritance

# class A():
#     def dis(self):
#         print("Aaaa")

# class B(A):
#     def dis2(self):
#         print("Bbb")

# class C(A):
#     def dis3(self):
#         print("Ccc")

# class D(A):
#     def dis4(self):
#         print("Ddd")

# b=B()
# c=C()
# d=D()

# b.dis()
# b.dis2()
# c.dis()
# c.dis3()
# d.dis()
# d.dis4()


#==============================================================

# Hybrid inheritance
# class A():
#     def dis(self):
#         print("A ")

# class B(A):
#     def dis1(self):
#         print("B")

# class C(B,A):
#     def dis2(self):   
#         print("C")

# b=B()
# c=C()
# b.dis()
# b.dis1()
# c.dis()
# c.dis1()
# c.dis2()

# class car():
#     def d1(self):
#         print("1")
# class car1(car):
#     def d2(self):
#         print("2")
# class car2(car1,car):
#     def d3(self):
#       print("333")

# a1=car1()
# a2=car2()

# a1.d1()
# a1.d2()
# a2.d1()
# a2.d2()
# a2.d3()
#===============================================================


