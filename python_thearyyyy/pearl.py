
# t1=(1,2,3,4,5,6,7,8,9,10,1,1,1,1,1,1)

# print(type(t1))
# print(t1)

# print(t1.count(1))

# print(t1.index(3))

# t2=list(t1)

# t2.append(11)
# t2.extend([1,2,3,4,5,6])

# print(tuple(t2))

# ==============================================================================

# s1={}
# s2=list(s1)
# print(type(s1))
# print(s1)

# s1.add(12)
# s1.add(112)
# s1.pop()
# s1.remove(3)
# s1.clear()
# s2.append(10)
# print(s2)

# ============================================

# d1={
#     "name":"nilesh",
#     "age":23,
#     "subject":"python",
#     "student":{
#         "name":"pearl",
#         "number":1234567890
#     }

# }

# print(type(d1))
# print(d1)

# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1.update({"roll number":2})
# d1.update({"roll number1":1})
# print(d1["student"]["number"])
# print(d1)

# ==========================================================

# one condition : 

# a=11

# if a>10:
#     print("True")


# 2 condition

# a=11

# if a>10:
#     print("nilesh")
# else:
#     print("pearl")    

# 3 condition

# a=16

# if a==11:
#     print("yes")
# elif a<15:
#     print("yes1")
# elif a>=16:
#     print("yes2")    
# else:
#     print("no")        

# nested condition

# a=10

# if a==10:
#     print("yes")
#     if a<5:
#         print("yes2")
#     else:
#         print("no1")    
# else:
#     print("no")    

# ======================


# a=11

# if a%2==0:
#     print("evan number")
# else:
#     print("odd number")


# eng=int(input("Enter A Marks : "))
# maths=int(input("Enter A Marks : "))
# sci=int(input("Enter A Marks : "))
# guj=int(input("Enter A Marks : "))
# hindi=int(input("Enter A Marks : "))

# total=eng+maths+sci+guj+hindi
# print(total)

# pr=total/5
# print(pr)

# 90 to 100 =A+
# 80 to 90 = A
# 70 to 80 = B+
# 60 to 70 = B
# 50 to 60 = C
# 33 to 50 = D
# 33 to low =fail

# if pr>=90 and pr<=100:
#     print("A+")
# elif pr>=80 and pr<=90:
#     print("A")
# elif pr>=70 and pr<=80:
#     print("B+")
# elif pr>=60 and pr<=70:
#     print("B")        
# elif pr>=50 and pr<=60:
#     print("C")
# elif pr>=33 and pr<=50:
#     print("D")
# else:
#     print("fail")        

# a=10,20,30,40,50

# if 11 in a:
#     print("yes")
# else:
#     print("no")    

# 1 = python
# 2 = java
# 3 = c
# 4 = c++
# 5 = django


# num=int(input("Enter A Number : "))

# if num==1:
#     print("python")
# elif num==2:
#     print("java")
# elif num==3:
#     print("c")
# elif num==4:
#     print("c++")
# elif num==5:
#     print("django")
# else:
#     print("invalid number")


# ==================================================

# for n in range(1,12):
#     print(n)

# for a in range(1,31):
#     if a%2==0:
#         pass
#     else:
#         print(a)

# break
# continue
# pass

# for i in range(1,11):
#     if i==7:
#         break
#     print(i)


# for i in range(1,11):
#     if i==1:
#         continue
#     print(i)


# for i in range(1,11):
#     # if i==2:
#     #    pass
#     # print(i)
#     pass

# l1=("nilesh","pearl","django","python")

# nilesh
# pearl
# django
# python
# print(l1[0])
# print(l1[1])
# print(l1[2])
# print(l1[3])


# for i in l1:
#     print(i)

# 1 to 10

# Start=int(input("Enter A Start Number : "))
# End=int(input("Enter A End Number : "))

# for i in range(Start,End):
#     for n in range(1,11):
#         print(f"{i}*{n}={n*i}")
#     print("\n")

# for i in range(1,4):
#     for n in range(1,6):
#         print(n,end=" ")
#     print("\n")    

# i=10

# while i>=1:
#     if i==5:
#         break
#     print(i)
#     i-=1

# i=1

# while i<=11:
#     if i==5:
#         pass
#     print(i)
#     i+=1


# ==========================================


# def fun():
#     print("pearl")
#     print("python")

# fun()    # call 


# def pearl():
#     name="pearl"
#     age=23
#     subject="python"
#     print(name)
#     print(age)
#     print(subject)

# def nilesh():
#     name="nilesh"
#     age=23
#     subject="python-django"
#     print(name)
#     print(age)
#     print(subject)    
    
# def tushar():
#     name="tushar"
#     age=23
#     subject="php"
#     print(name)
#     print(age)
#     print(subject)    

# pearl()    


# def evan():
#     for i in range(1,11):
#         print(i)

# def evan1():
#     for i in range(11,0,-1):
#         print(i)        

# evan()

# def add():
#     num1=int(input("Enter a number : "))
#     num2=int(input("Enter a number : "))
#     print(num1+num2)

# def sub():
#     num1=int(input("Enter a number : "))
#     num2=int(input("Enter a number : "))
#     print(num1-num2)

# def multi():
#     num1=int(input("Enter a number : "))
#     num2=int(input("Enter a number : "))
#     print(num1*num2)
# def div():
#     num1=int(input("Enter a number : "))
#     num2=int(input("Enter a number : "))
#     print(num1/num2)


# number=int(input("Enter A             Number : "))

# if number==1:
#     add()
# elif number==2:
#     sub()
# elif number==3:
#     multi()
# elif number==4:
#     div()
# else:
#     print("invalid number")


# def fun():
#     a=10
#     b=20
#     print(a+b)


# fun()    



# def fun(a,b,c):
#     print(a+b-c)
# fun(10,20,30)    


# def fun(a,b=10):
#     print(a)
#     print(b)
# fun(12,34)    

# def student(name,age,subject,std=12):
#     print(name)
#     print(age)
#     print(subject)
#     print(std)

# student("pearl",23,"python","bca")    
    
# def student(*args):
#     print(args)

# student(1,2,3,4,5,6,7,8,9,11,2,3,4,5,56,6)    


# def student(**kwargs):
#     print(kwargs)

# student(name="nilesh",age=23,subject="python")


# a=lambda x:print(x)

# a(10)

# a=lambda x,y:print(x*y)

# a(10,20)

# map function


# l1=[1,2,3,4,5,6,7]

# def fun(l1):
#     return l1+l1

# a=map(fun,l1) 
# print(list(a)) 


# l1=[1,2,3,4,5,6,7]

# def fun(l1):
#     if l1%2==0:
#         return l1

# a=filter(fun,l1)
# print(list(a))


# l1=[x for x in range(1,11)]

# print(l1)

# l=[1,2,3,4,5,6,7,8,9,10]

# l1=[i for i in l if i%2==0 ]

# print(l1)

# file hendling

#  "x" create mood
#  "r" read mood
#  "w" write mood
#  "a" append mood

# create mood
# f=open("python.txt","x")
# f.close()

# read mood
# f=open("python.txt","r")
# print(f.read())
# f.close()

# write mood
# f=open("python.txt","w")
# f.write("""kjlajkkjljaklkjl
# jkal
# klka""")
# f.close()

# append mood

# f=open("python.txt","a")

# f.write("pearl")
# f.close()

# for i in range(1,6):
#     for n in range(1,i+1):
#         print(n,end=" ")
#     print("")    


# math module

# import math

# print(math.pi)

# print(math.ceil(1.5))

# print(math.floor(1.9))

# print(math.pow(3,3)) # 3*3*3 3**3

# print(math.factorial(6)) # 6*5*4*3*2*1

# datetime module

# import datetime
# d=datetime.datetime.now()
# print(d)
# print(d.date())
# print(d.time())


# print(d.strftime("%A"))
# print(d.strftime("%a"))
# print(d.strftime("%B"))
# print(d.strftime("%b"))
# print(d.strftime("%c"))
# print(d.strftime("%d"))
# print(d.strftime("%D"))

# import random

# # a=random.random()
# # a=random.randint(1,20)
# # print(a)
# # a=random.randrange(1,10,2)
# l1=[1,2,3,4,"pearl","python","django"]
# # random.shuffle(l1)
# # print(l1)
# l=random.choice(l1)

# print(l)


# from s import*

# fun()
# print(l1)



# l1=[1,2,3,4,5,1,2,3,4,5,7,8,9,10]
# l2=[]
# # c=0


# for i in l1:
#     if l1.count(i)<=1:    
#         if i not in l2:
#             l2.append(i)
    

# print(l2)
# print(len(l2))



















































