# class A():
#     name="vidhi"                       #<-  public method
#     age=23                             #<-  public method
#     pin=1234                           #<-  public method
#     __account=905409800                #<-  private __  method

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.pin)
#         # print(self.__account)

# d=A()
# d.display()

# print(d.name)
# print(d.age)

# print(d.pin)
# print(d.__account) #Error

# ==================================================
# class bank():
#     def __init__(self):
#         self.a=123
#         self._b=1234
#         self.__c=12345
#     def display(self):
#         print(self.a)
#         print(self._b)
#         print(self.__c)

# obj=bank()
# print(obj.a)
# print(obj._b)
# print(obj.__c)


# obj.display()


#========================================

# class bank():
#     def __init__(self):
#         self.a=12
#         self._a=13
#         self.__a=14
    
#     def display(self):
#         print(self.__a)
#         print(self._a)
#         print(self.a)
    
# obj=bank()
# obj.display()
# print(obj.__a)

#========================================

# class bank():
#     def __init__(self):
#         self.a=1
#         self._a=2
#         self.__a=3

#     def display(self):
#         print(self.a)
#         print(self._a)
#         print(self.__a)

# obj=bank()
# obj.display()



# class bank():
#     def __init__(self):
#         self.__name="vidhi"
#         self.age=23
#         self.pin=1234
#         self.ac=546546546

#     def show(self):
#         print(self.__name)
#         print(self.age)
#         print(self.pin)
#         print(self.ac)













# b=bank()
# print(b.show())
# print(b.__name)
# b.show(b.name)



