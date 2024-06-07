
# print("hello")
# print("nilesh")

"""sjjkkl
jklsljlk
kjksj"""

# a=10

# print(a)


# a=10
# b=10.10
# c="nilesh"
# d=True
# e=None

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# a=int(input("Enter A Number : "))
# print(a)
# print(type(a))

# name="nilesh"
# age=22

# print(f"my name is {name} and my age is {age}")
# output = my name is nilesh and my age is 22

# output = nilesh 22

# print(name,age)
# print(name,end=" ")
# print(age)


# _a1_=10


# sum=0

# for i in range(1,11):
#     sum+=i
# print(sum)    

# odd=0

# for i in range(1,12):
#     if i%2==0:
#         pass
#     else:
#         odd+=1
# print(odd)


# for i in range(1,11):
#     for n in range(1,11):
#         print(f"{n}*{i}={n*i}")


# evan=0
# odd=0

# for i in range(1,11):
#     if i%2==0:
#         evan+=1
#     else:
#         odd+=1 

# print(evan)
# print(odd)

# num=1234567890

# num1=str(num)
# count=0
# for i in num1:
#     count+=1
# print(count)
    

# num="nil"

# num1=""

# for i in num: #
#     num1=i+num1


# if num==num1:
#     print("p")
# else:
#     print("n")


# num = input("Enter a number: ")

# if num == num[::-1]:
#     print("The number is a palindrome!")
# else:
#     print("The number is not a palindrome!")


# a=4*4*4
# b=7*7*7

# print(a+b)


# num=int(input("Enter A Number : "))
# sum=0
# temp=num

# while temp>0:
#     digit=temp%10
#     sum=sum+digit**3
#     temp=temp//10

# if num==sum:
#     print("armstonge number")

# else:
#     print("not a armstodg number") 



# start=int(input("Enter A Number : "))
# end=int(input("Enter A Number : "))



# for i in range(start,end):
#     for n in range(1,11):
#         print(f"{i}*{n}={n*i}")
#     print("\n")


# start=int(input("Enter A Number : "))
# end=int(input("Enter A Number : "))
# sum=0

# for i in range(start,end):
#     sum+=i
# print(sum)


# l1=[1,2,3,4,5,6,7]
# l1=[1,2,1.2,1.3,"nilesh",True,None]

# l1=[1,2,3,4,5,6,"nilesh",True]


# print(l1[-:1])
# print(l1[2:5:2])

# print(l1[::])

#  2 1

# l1=[10,2,4,19,57,8,3,6,7,8,1]  
# print(len(l1))

# print(sum(l1))

# print(max(l1))

# print(min(l1))

# print(l1[1][0])

# l1.sort(reverse=True)

# l1.append(90)
# l1.extend([20,31,90])
# l1.insert(1,11)
# print(l1)


# name='nilesh'
# name1="nilesh"
# name2="""nilesh
#     nilesh
# nilesh"""


# print(name)
# print(name1)
# print(name2)

# name="jadav nilesh jadav"

# print(len(name))

# print(name.capitalize())

# print(name.upper())

# print(name.lower())

# print(name.isupper())

# print(name.islower())

# print(name.find("J"))

# print(name.endswith("av"))

# print(name.replace("jadav","python"))

# print(name.split())


# name="nilesh"
# age=24

# print(f"my name is {name} and my age is {age}")
# output :  my name is nilesh and my age is 23


#================================ list===========================================
# 


# l1=[1,22,33,44,2,3,4,55,6,7,8,9,10]
# l1=[1,2,"nilesh",1.3,True,None,True]

# print(l1[2:4])

# print(l1[-1])

# print(len(l1))

# print(sum(l1))

# print(max(l1))

# print(min(l1))

# l1.sort()
# l1.reverse()

# l1.append(23)

# l1.extend([1,2,3,4,5,6])

# l1.insert(1,23)
# l1=[1,22,33,44,2,3,4,55,6,7,8,9,10]
# l1.pop(1)
# l1.pop()
# l1.clear()
# l1.remove(44)
# del l1
# l2=l1.copy()
# l3=l1.copy()
# print(l2)
# print(l3)
# ==================================

# l1= ["Apple", "Banana", "Car", "Dolphin" ]

# for i in l1:
#     for n in i:
#         print(n)
#     print("/////")
    
# name="nilesh12345"
# sum=0

# for i in name:
#     sum=sum+1

# print(sum)    
    
    

    # =================================================
# month=input("Enter  A Month : ")

# if month=="jan" or month=="mar":
#     print("31")
# elif month=="feb":
#     print("28")
# else:
#     print("30")    


# input password from user
# password = input()
 
# set up flags for each criteria
# of a valid password
# has_valid_length = False
# has_lower_case = False
# has_upper_case = False
# has_digits = False
# has_special_characters = False
 
 
# first verify if the length of password is
# higher or equal to 8 and lower or equal to 16
# if (len(password) >= 8) and (len(password)<=16):
 
#     has_valid_length = True
 
    # iterate through each characters
    # of the password
    # for i in password:
 
        # check if there are lowercase alphabets
        # if (i.islower()):
        #         has_lower_case = True                   
 
        # check if there are uppercase alphabets
        # if (i.isupper()):
        #         has_upper_case = True                   
 
        # check if the password has digits
        # if (i.isdigit()):
        #         has_digits = True                       
 
        # check if the password has special characters
#         if(i=="@" or i=="$" or i=="_"or i=="#" or i=="^" or i=="&" or i=="*"):
#                 has_special_characters = True           
 
 
# if (has_valid_length==True and has_lower_case ==True and has_upper_case == True and has_digits == True and has_special_characters == True):
#     print("Valid Password")
# else:
#         print("Invalid Password")

# ============================


# a=[1,2,3,4,5,6,7,8]

# print(a)


# output: [1,2,3,[1,2,3,4],4,5,6,[1,2,3,4,5],7,8,9,10,[1,2,3,4,3,2,1]]

# a.insert(3,[1,2,3,4])
# a.insert(7,[1,2,3,4,5])
# a.append(9)
# a.append(10)
# a.append([1,2,3,4,3,2,1])
# print(a)


# a=[1,2,3,4,5,6,7,8,[1,2,3,4,5,6]]

# a.pop(-1)

# a.remove(1)
# a.remove(2)
# a.clear()


# del a


# print(a)

# l1=["python","django","java"]

# for i in l1: #  python
#     for n in i: # p y t h o n  d j a n g o
#         print(n,end=" ") # pythondjango



# d1={
#     "name":"nilesh",
#     "age":23,
#     "subject":"python"

# }

# print(d1)
# print(type(d1))

# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1.update({"class":1})
# print(d1)

# ===============

# if condition:
#     code
# elif codition:
#     code
# elif condition:
#     code    
# else:
#     code    

# if condition:
#     if condition:
#         code


# a=111

# if a==11:
#     print("yes")

# elif a<20:
#     print("yes1")

# else:
#     print("no")

# a=int(input("Enter A number : "))

# if a%2==0:
#     print("evan  number")
# else:
#     print("odd number")     

# a=10

# if a==11:
#     if a<10:
#         print("yes") 
#     else:
#       print("no1")


# else:
#     print("no")        



# password=input("enter a password : ")

# len1=False
# up1=False
# lo=False
# di=False

# if len(password)>=8:
#     len1=True
#     for i in password:
#         if i.isupper():
#             up1=True
#         if i.islower():
#             lo=True
#         if i.isdigit():
#             di=True


# if len1==True and up1==True and lo==True and di==True:
#     print("Valid Password")
# else:
#     print("Envalid Password")
               
# n=12345
# a=str(n)
# c=0
# for i in a:
#     c+=1
# print(c)    
# e=0
# o=0

# for i in range(1,11):
#     if i%2==0:
#         e+=i # 2,4,6,8,10
#     else:
#         o+=i # 1,3,5,7,9  
# print(e)
# print(o)          

# num=1234567

# num=str(num)

# a=int(num[2])
# b=int(num[-1])
# print(len(num))
# print(a+b)


# a=[1,2,3,4,5,6]

# a[0],a[-1]=a[-1],a[0]

# print(a)




# def fun():
#     print("sagar")

# fun()    


# def fun(a,b,c):
#     print(a)
#     print(b)


# fun(10,20,30)


# def fun(a=10,b=20):
#     print(a)
#     print(b)

# fun()

# def fun(*args):
#     print(args)

# fun(1,2,3,4,5,6,7,8,9,10,11)    


# def fun(**kwargs):
#     print(kwargs)

# fun(name="sagar",age=32,python="django")    


# def fun(x):
#     if x==1:
#         return x 
#     else:
#         return x * fun(x-1)

# print(fun(5))

# def recursive_factorial(n):
#   if n == 1:
#       return n
#   else:
#       return n * recursive_factorial(n-1)

# print(recursive_factorial(4))



# def fun(x):
#     if x<12:
#         return x
#     else:    
#         return fun(x-1) #  11-1 9 
    

# print(fun(12))            

# a=lambda x,y:x*y

# print(a(10,20))

# l1=[1,2,3,4,5,6,7,8]


# def fun(l1):
#     print("hello")


# a=map(fun,l1)
# print(list(a))


# def fun():
#     print("hello")

# fun()
# fun()    

# l1=[1,2,3,4,5,6,7,8]


# def fun(l1):
#     if l1%2==0:
#         return l1



# a=filter(fun,l1)
# print(list(a))


# def fun():
#     print("hello")

# def fun1():
#     print("sagar")

# fun=fun1    

# fun()

# print(4/2)
# print(4//2)


# x  create
# r  read
# w  write
# a  append

# create file
# f=open("sagar.txt","x")
# f.close()


# read file

# f=open("sagar.txt","r") 
# print(f.read())
# f.close 

# f=open("sagar.txt","w")

# f.write("jdjkjs;")
# f.close()

    
# f=open("sagar.txt","a")
# f.write("\n\tnileshnilesjannnnanandkkkkkkd")
# f.close()


# with open("tushar1.txt","x") as f:
#     pass


# with open("tushar1.txt","r") as f:
#     print(f.read())

# with open("tushar1.txt","w") as f:
#     f.write("nilesh")

# with open("tushar1.txt","a") as f:
#     f.write("nilesh")

# l1=()
# l2=list(l1)
# for i in range(1,11):
#     l2.append(i)

# print(tuple(l2))    

# l1=(n for n in range(1,11))
# print(tuple(l1))

# l1=[i for i in range(1,11) if i%2==0]
# print(l1)

# l1={var:var**3 for var in range(1,6)}
# print(l1)

# l1=[1,2,3,4,5,6]
# l2=[10,20,30,40,50]

# a=zip(l1,l2)
# print(list(a))

# l3={k:y for k,y in zip(l1,l2)}
# print(l3)


# print(ord('a'))
# for i in range(ord('a'),ord('z')+1):
#     print(chr(i))



# a=1234321

# b=str(a)

# c=b[::-1]

# if b==c:
#     print("p")
# else:
#     print("np")    



# l1=[1,2,3,4,1,2,3,5,5,6,7,7]

# def fun():
#     print("pearl")


# import math


# print(math.pi)


# print(math.factorial(5))  # 5*4*3*2*1


# print(math.ceil(1.1))

# print(math.floor(1.1))

# print(math.pow(3,4))   # 3*3*3


# import random

# # print(random.random())

# # print(random.randint(1,100))

# # print(random.randrange(1,10))
# l1=[1,2,3,4,5,6,7,8,"sagar","python"]

# print(random.choice(l1))


# import datetime

# d=datetime.datetime.now()
# print(d)
# print(d.date())
# print(d.time())
# print(d.month)


# print(d.strftime("%A"))
# print(d.strftime("%a"))
# print(d.strftime("%B"))
# print(d.strftime("%b"))

# from diyak import *

# fun()
# fun1()

# l1=[i for i in range(1,11) if i%2==1]

# print(l1)


# try:
#     print(y)
# except:
#     print("Yes")  
# else:
#     print("yes1")      
# finally:
#     print("python")



# exam={
#     1:{
#         "Q":"Python ? ",
#          "A":"break",
#          "B":"continue",
#          "C":"pass",
#          "D":"else if",
          
        
#     },
#     2:{
#         "Q":"what is Python ? ",
#          "A":"break",
#          "B":"continue",
#          "C":"else if",
#          "D":"else",
          
        
#     }
# }

# number=int(input("Enter A Number : "))
# f1=exam[1]['D']
# f2=exam[2]['C']

# if exam[number].keys():
#     print("Your Question is : ",exam[number]["Q"])
#     ans=input("Enter A Ans : ")
#     if f1==ans or f2==ans:
#         print("Right Ans")
#     else:
#         print("Wrong Ans")   
# else:
#     print("Envalid Number : ")              

# d1={i:i*i for i in range(1,11)}

# print(d1)

# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# d1.update(d2)
# print(d1)



# class fun:
#     color="red"
#     subject="python"
#     std=2

# a=fun

# print(a.color)
# print(a.subject)
# print(a.std)


# class fun:
#     color="red"
#     subject="python"
#     std=2
    
#     def fun1(self):
#         print(self.color)
#         print(self.subject)
#         print(self.std)

# a=fun()
# a.fun1()        
# class fun():
#     def __init__(self,name,age,subject):

#         self.name=name
#         self.age=age
#         self.subject=subject

#     def display(self):
#         print(self.name)
#         print(self.age)    
#         print(self.subject)

# a=fun("nilesh",23,"python")

# a.display()

# class A():
#     def funA(self):
#         print("class A ")

# class B(A):
#     def funB(self):
#         print("class B ")
        

# b=B()
# b.funA()
# b.funB()


# class A():
#     def funA(self):
#         print("class A ")

# class B():
#     def funB(self):
#         print("class B ")
        
# class C(A,B):
#     def funC(self):
#         print("class C ")


# c=C()

# c.funA()
# c.funB()
# c.funC()


# class A():
#     def funA(self):
#         print("class A ")

# class B(A):
#     def funB(self):
#         print("class B ")
        
# class C(B):
#     def funC(self):
#         print("class C ")


# c=C()

# c.funA()
# c.funB()
# c.funC()


# class A():
#     def funA(self):
#         print("class A ")

# class B(A):
#     def funB(self):
#         print("class B ")
        
# class C(A):
#     def funC(self):
#         print("class C ")


# b=B()
# c=C()

# b.funA()
# b.funB()
# c.funA()
# c.funC()

# class A():
#     def funA(self):
#         print("class A ")

# class B(A):
#     def funB(self):
#         print("class B ")
        
# class C(B,A):
#     def funC(self):
#         print("class C ")


# b=B()
# c=C()
# b.funA()
# b.funB()
# c.funA()
# c.funB()
# c.funC()


# class sagar():
#     name="sbi"
#     age=23
#     subject="python"
#     atmpin=123456789
#     __accountno=1234567891011
   
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.subject)
#         print(self.atmpin)
#         print(self.__accountno)
#         print(self.__accountno)
         
# b=sagar()
# b.display()
# print(b.__accountno)


        
# polymorephism

# 2 types
# method overloding
# method overriding

# class A():
#     def display(self):
#         print("Class A")

# class B(A):
#     def display(self):
#         A.display(self)
#         print("Class B")

# b=B()
# b.display()




# print(len("sagar"))
# print(len(["sagar","python","django"]))


# print(10+20)
# a="python"
# b="django"
# print(a+" "+b)







# import requests

# response = requests.get("http://127.0.0.1:8000/")

# print(response.json())



# ==========================

# l1=[1,2,1.2,3,5,"nilesh","python",True,None]

# print(l1[1])

# print(len(l1))

# l1.pop(0)
# print(l1)



# x = 10
# # x = 10 * 2
# x *= 2
# print(x)


# x = 11
# # x = x % 5
# x %= 8
# print(x)




try:
    # print(a)
    # a="abc"
    # print(a+5)
    print(10/2)
    # n=input("Enter Number : ")
    # print(n)
except NameError:
    print("NameError")
    
except ValueError:
    print("ValueError")
    
except TypeError:
    print("TypeError")
    
except ZeroDivisionError:
    print("ZeroDivisionError")
    
finally:
    print("okkk")

    