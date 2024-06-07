
# name="python django"
# print(name[::-1])
# print(len(name))

# print(name.upper())

# print(name.isupper())

# print(name.islower())

# print(name.capitalize())

# print(name.replace("python","java"))

# print(name.endswith("r"))


# l1=[1,2,3,4,5,1,2,3,40]
# l2=[1,2,3,4]
# l1.append(l2)
# l1.extend(l2)
# l1.insert(1,[23,34])
# l1.pop(1)
# l1.remove(3)
# l1.clear()
# del l1
# print(l1)


# t1=(1,2,1,21,2,3,43,4,4,4,4,4,43,4,5,6,7,8)

# print(type(t1))

# print(t1.count(4))

# print(t1.index(4))

# m=set(t1)
# print(m)


# t1=[1,2,1,21,2,3,43,4,4,4,4,4,43,4,5,6,7,8]
# count=0

# t2=set(t1)
# print(list(t2))

# for i in t2:
#     count+=1
# print(count)
# print(len(t2))

# l1=[12,23,34,45,56]

# l1[0],l1[-1]=l1[-1],l1[0]

# print(l1)


# def fun():
#     print("nilesh")
# fun()    


# def fun(num,num1):
#     print(num,num1)

# fun(1,2)    


# def fun(num=1,num1=2):
#     print(num)
#     print(num1)

# fun(23,34)    


# def fun(*args):
#     print(args)

# fun(1,2,3,4,5,6,7,8)

# def fun(**kwargs):
#     print(kwargs)

# fun(name="nilesh",age=23,subject="python")    



# def doc():
#     name="""
#         kslksl
#         kdklkd
#         klskl
#         klsks
#         kslks
#         skl
#         lks
#     """

#     print(name)

# doc()


# a=10

# if a<20:
#     if a==110:
#         print("yes")
#     else:
#         print("no1")
# else:
#     print("no")

# a=110
# b=22220
# c=30
# d=1000000

# if a>b and a>c and a>d:
#     print(a)
# elif b>a and b>c and b>d:
#     print(b)
# elif c>a and c>b and c>d:
#     print(c)             
# else:
#     print(d)           


# a=11

# if a%2==0:
#     print("even")
# else:
#     print("odd")

# 1 python
# 2 java
# 3 django
# 4 php
# 5 c
# 6 C++

# num=int(input("Enter A Number : "))

# if num>=6:
#     if num==1:
#         print("Python")

#     elif num==2:
#         print("java")

#     elif num==3:
#         print("django")
#     elif num==4:
#         print("php") 
#     elif num==5:
#         print("c")
#     elif num==6:
#         print("c++") 
# else:
#     print("invalid number ")


# num=input("Enter A Number : ")

# if num=="A":
#     print("Python")
# elif num=="B":
#     print("java")
# elif num=="C":
#     print("django")
# elif num=="D":
#     print("php") 
# elif num=="E":
#     print("c")
# elif num=="F":
#     print("c++") 
# else:
#     print("invalid number ")

# loop    

# syntax:

# for variable_name in range(1,11):
#     code

# for a in range(1,11):
#     print(a,end=" ")
# print("\n")    


# for i in range(1,11):
#     if i%2==0:
#         print(i)
#     else:
#         print(i)
     

# for i in range(2,11,1):
#     print(i)

# a=1,2,3,4,5,6,7

# for i in a:
#     print(a)


# a=5
# for i in range(1,11):
#     print(f"{a} * {i} = {a*i}")



# c=0
# for i in range(1,6):
#     num=int(input("Enter A number : "))
#     c+=num

# print(c)    

# name="my subject is pythonyuiuyiuyi ! "

# # print(len(name))
# c=0
# for i in name:
#     c+=1

# print(c)    

# print(7^3)

# ===============================

# pin1=123
# balance=100
# l=True


# while l:
#     num=int(input("Press 1 for Generete Your PIN ,\nPress 2 for Check Your Balance,\nPress 3 for Deposit amount,\nPress 4 for Withdrow Amount, \nEnter Number:: "))

#     if num==1:
#         pin=int(input("Enter A Pin : "))
#         pin1=pin
#         print("Your pin is ",pin1)
#     elif num==2:
#         pin=int(input("Enter A Pin : "))
#         if pin1==pin:
#             print("Your Balance Is : ",balance)
#         else:
#             print("Envalid Pin")
#     elif num==3:
#         pin=int(input("Enter A Pin : "))
#         if pin1==pin:
#             amount=int(input("Enter A Amount For deposit : "))
#             balance=balance+amount
#             print("Your Balance Is : ",balance)
#         else:
#             print("Envalid Pin")

#     elif num==4:
#         pin=int(input("Enter A Pin : "))
#         if pin1==pin:
#             amount=int(input("Enter A Amount For Withdrow : "))
#             balance=balance-amount
#             print("Your Balance Is : ",balance)
#         else:
#             print("Envalid Pin")
#     else:
#         print("Envalid Number")    

#     chioce=input("Enter (Y) for Re-Enter pin And Enter (N) For Stop Proccess : ")

#     if chioce=='y':
#         l=True
#     else:
#         l=False    

# ==========================================


# import random

# computer=random.randint(1,20)

# s=True

# while s:
#     for i in range(1,11):
#         user=int(input("Enter A Number : "))

#         if user>computer:
#             print("lower number")
#         elif user<computer:
#             print("upper number")
#         else:
#             print("you win")
#             break        
#         s=False
#     else:
        # print("Game Over")


# =========================================================


# menu=[["what is  80*3"],["what is 800-450"],["what is 8*3/2"],["what is 46/2"],["what is 60*3/2"],
# ["what is 80/2*5"],["what is 100*2-100"],["what is 50+100*4"],["what is 100-100/2"],["what is 2*5+50"]]

# print(menu)
# l=True

# num=int(input("Enter A Number : "))
# while l:
#     if num==1:
#         print(menu[0])
#         l1={"A":240,"B":340}
#         print(l1)
#         ans=int(input("Enter A Answer : "))
#         if l1["A"]==ans:
#             print("R")
#         else:
#             print("W")
#     elif num==2:
#         print(menu[1])
#         l1={"A":240,"B":350}
#         print(l1)
#         ans=int(input("Enter A Answer : "))
#         if l1["B"]==ans:
#             print("R")
#         else:
#             print("W")
#     elif num==3:
#         print(menu[2])
#         l1={"A":24,"B":12}
#         print(l1)
#         ans=int(input("Enter A Answer : "))
#         if l1["B"]==ans:
#             print("R")
#         else:
#             print("W")        
    
#     else:
#         print("Envalid Number ")
   
#     ch=input("Enter A 'y' for yes and 'n' for no : ")
#     if ch=="y":
#         l=True
#     else:
#         l=False



# =====================================


# l1=["h","he"]
# l2=["ii","llo"]
# l3=[]
# a=l1[0]+l2[0]
# b=l1[1]+l2[1]
# l3.append(a)
# l3.append(b)

# print(l3)

# a="123"
# a1='nilesh'
# a2="""nilesh""" 
# print(type(a2))
# a="hello world"
# print(len(a))
# print(a[0:11:3])
# print(a[0::2])
# print(a[0:2])
# print(a[5:8])
# print(a[0:])
# print(a[-6:])
# print(a[::-6])

# b="ello"
# print(b.islower())

# a="she is my sister"
# print(a.replace("she","nimi"))

# a="she is my sister"
# print(a.split(','))


# a="she is my sister"
# b=" "
# print(" ".join(a))
# print(b.join(a))

# a="vidhi"
# b="my name is " +a
# print(b)


# name="vidhi"
# age=23

# print("my name is {} and my age is {}".format(name,age))
# print("my name",name)


# a="my \\t\\t name is vidhi"
# print(a)


# a=1
# b=1
# if a>=b:
#     print("a is max")
# elif a<=b:
#     print("b is max")
# elif a==b:
#     print("both are equal")
# else:
#     print("invalid number")

# x = float(input("Enter the Marks: "))
# if x<=100 and x>90:
#     print("A Grade")
# elif x<=90 and x>80:
#     print("B Grade")
# elif x<=80 and x>60:
#     print("C Grade")
# elif x<=60 and x>=40:
#     print("D Grade")
# elif x<40 and x>=0:
#     print("Fail")
# else:
#     print("Invalid")


# dictionary:

# method:
# 1.keys
# 2.values
# 3.items
# 4.popitem
# 5.update
# 6.clear

# d={'a':1,'b':2,'c':3}
# print(type(d))
# print(d)

# d={"name":"vidhi","subject":"python","age":23}
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# d.popitem()
# print(d)
# d.update({"city":"ahmedabad"})
# print(d)
# d.clear()
# print(d)


# d={"vidhi":{"height":5.5,"weight":60},"hetal":{"height":5.8,"weight":55}}
# print(d)
# print(d["hetal"]["weight"])
# d["hetal"]={"height":5.1,"weight":66}
# d["hetal"]["height"]=5

# print(d)

# d={"vidhi":{"height":5.5,"weight":60},
#    "hetal":{"height":5.8,"weight":55},
#    1:[1,2,3],
#    2:(1,2,3),
#    3:{1,2,3}}

# d={"vidhi","hetal","raam"}
# age=21
# print(dict.fromkeys(d,age))

# Dictionary
# define dictionary using key & values
# duplication not allow
# indexing allow
# Method
# 1.key
# 2.values
# 3.items
# 4.popitems
# 5.update
# 6.clear

# d={"name":"hetal","age":27}

# print(d.keys())
# print(d.items())
# print(d.popitem())
# d.popitem()
# print(d)
# d.update({"city":"rajula"})
# print(d)
# d.clear()
# print(d)

# d={"hetal":{"age":27,"height":5.0,"weight":55},"vidhi":{"age":23,"height":5.5,"weight":55},1:[1,2,3],2:(4,6,7),3:{8,7,9}}
# print(d)
# print(d["hetal"]["height"])
# d["hetal"]={"height":5.1}
# print(d)
# d["hetal"]["height"]=5.5
# print(d)
# d={1:11,2:22,1:11,2:55}
# print(d)
# print(d[2][2])
# d={"hetal"}
# d1={"vidhi"}
# age=21
# age1=23
# print(dict.fromkeys(d,age))
# print(dict.fromkeys(d1,age1))

# a = '6'
# b = '6'
# if a > b:
#     print("a is max")
# elif a < b:
#     print("b is max")
# elif a==b:
#     print("equal number")
# else:
#     print("INVALID NUM")



# for i in range(1,7):
#     for n in range(1,11):
#         # if n==6:
#         #     print("*",end=" ") 
#         if i==1 and n==6:
#             print("*",end=" ") 
#         elif i==2 and n==5 or i==2 and n==7:
#             print("*",end=" ") 
#         elif i==3 and n==6:
#             print("*",end=" ") 
#         elif i==3 and n==4 or i==3 and n==8 :
#             print("*",end=" ") 
#         elif i==4 and n==3 or i==4 and n==9:
#             print("*",end=" ") 
#         elif i==5 and n==2 or i==5 and n==10:
#             print("*",end=" ")     
#         else:
#             print(" ",end=" ")    
#     print()








# class Employee:
#     def __init__(self, name, salary): 
#         self.name = name    # public data member        
#         self.__salary = salary    # private member
        
# emp = Employee('Ashish', 10000)  # creating object of a class
# print('Salary:', emp.__salary)


# class Bank:
#         name="vidhi"
#         __ac=3456666
        
#         def dispaly(self):
#                 print(self.name)
#                 print(self.__ac)
                
# d=Bank()
# # d.dispaly()
# print(d.name)
# print(d.__ac)




# class Bank:
#         def __init__ (self,name,_ac):
#                 self.name=name
#                 self._ac=_ac
                
#         # def dispaly(self):
#         #         print(self.name)
#         #         print(self._ac)
                
# d=Bank("a",3423)
# # d.dispaly()
# print(d.name)
# print(d._ac)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
print(p1)

