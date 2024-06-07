
# class nilesh():
#     def __init__(self):
#         self.__n=123
#         self._m=321
#         self.u=456
#     def display(self):
#         print(self.n)
#         print(self.m)

# R=nilesh()   
# print(R._m)


# class A():
#     def __init__(self):
#         self.a=123
#         self.__b=123
#     def display(self):
#         print(self.a)
#         # print(self.__b)

# a=A()
# print(a.a)
# print(a.__b)
   
# =========================================================================

# class bank:

#     def __init__(self):
#         self.a=10
#         self._a=20
#         self.__a=30

#     def display(self):
#         print(self.__a)

# obj=bank()
# obj.display()  
# print(obj.__a) 



 
# ==========================================================================
#polymorphism
# types:
# 1.method overloading <-- no used in python
# 2.method overriding 


# 2.method overriding 
# name="python"

# l1=["python","django"]


# print(len(name))
# print(len(l1))



# class A():
#     def display(self):
#         print("class A")

# class B(A):
#     def display(self):
#         A.display(self)
#         print("class B")       


# b=B()

# b.display()

# ==========================================

#Abstraction 

# from abc import ABC,abstractmethod

# class RBI(ABC):
#     # @abstractmethod
#     def display(self):
#         print("Class A")

# class SBI(RBI):
#     def display(self):
#         # RBI.display(self)
#         print("Class B")

# class BOI(RBI):
#     def display(self):
#         # RBI.display(self)
#         print("Class C")


# sbi=SBI()
# boi=BOI()
# rbi=RBI()
# rbi.display()
# sbi.display()

# boi.display()


# ==================================================
#Aggrigation
# class salary():
#     def __init__(self,e_salary,bonus):
#         self.e_salary=e_salary
#         self.bonus=bonus
    
#     def a_salary(self):
#         return self.e_salary*12+self.bonus
#     def display(self):
#         print("hello python")

# class employee():
#     def __init__(self,name,age,sal):
#         self.name=name
#         self.age=age 
#         self.sal=sal  
    
#     def total_salary(self):
#         return self.sal.a_salary()
#     def display1(self):
#         return self.sal.display()

# sal=salary(10000,2000)
# emp=employee("python",23,sal)

# # print(sal.a_salary())
# print(emp.total_salary())
# emp.display1()

# class salary ():
#     def __init__(self,e_salary,bonus):
#         self.e_salary=e_salary
#         self.bonus=bonus

#     def a_salary(self):
#         return self.e_salary*12+self.bonus
#     def display(self):
#         print("hello python")
# class employee():
#     def __init__(self,name,age,sal):
#         self.name=name
#         self.age=age
#         self.sal=sal
#     def total_salary(self):
#         return self.sal.a_salary()
#     def display(self):
#         return self.sal.display()
    

# sal=salary(100000,2000)
# emp=employee("python",23,sal)

# print(sal.a_salary())
# print(emp.total_salary())
# emp.display()


class salary():
    def __init__(self,e_salary,bonus):
        self.e_salary=e_salary
        self.bonus=bonus
    def a_salary(self):
        return self.e_salary*12+self.bonus
    def display(self):
        print("hello")


class employee():
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def total_Salary(self):
        return self.sal.a_salary()
    def display(self):
        return self.sal.display()

sal=salary(10000,2000)
ab=employee("abcd",23,sal)
print(sal.a_salary())


ab.display()



