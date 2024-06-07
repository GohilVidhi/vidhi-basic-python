
# Default Function
# len()
# sum()
# max()
# min()                 

# import keyword
# print(keyword.kwlist)


# def fun():
#     print("my name is vidhi")

# fun()

# def fun1():
#     print("python")

# def fun2():
#     print("Django")

# def fun5():
#     for i in range(1,11):
#         if i%2==0:
#             print(i)

# fun5()

# fun2()
# fun4()
# fun5()
#*********************
# Paramiter Function

# def fun(num,num1,num3):
#     print(num,num1,num3)
    
# fun(1,2,5)

# def fun(name):
#     print("my name is "+name)
# fun("vidhi")
# fun("python")
# fun("jcb")
#*********************
# Default Paramiter function
# def fun1(name="vidhi",age="23",city="ahmedabad"):
#     print(name,age,city)
# fun1()

# def abc(name="ram",age="22",city="ahmedabad"):
#     print(name)
#     print(age)
#     print(city)
# abc()

# def func(name="niki",age="24",city="ahmedabad"):
#     print(name,age,city)
# func()

# def func(name="python",age=33):
#     print(name,age)
# func("django",8)



#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#*Args:-----

# def fun(*name):
#     print(name)
# fun(11,4,5,6)

# def fun1(*args):
#     print(args)
# fun1("vidhi","python","abcd",23,22)


#-----------------------------------
# Kwargs:------

# def fun(**kwargs):
#     print(kwargs)
# fun(name="vaidehi",age=23,city="ahmedabad")

# def fun(**kwargs):
#     print(kwargs)
# fun(name="sd",name1="fds",name2="fwsfwe")


#=========================================


# global variable:---
# find function out

# a=100       #<-----------
# b=200000
# def fun():
#     a=200 
#     print(a)

# def fun1():
#     print(a)

# def fun2():
#     print(a+b)

# def fun3():
#     print(b)


# fun3()
# fun1()
# fun()
# fun2()

#*************************
# local variable
# find function under



# def fun():
#     a = 20  # <------------
#     print(a)

# def fun1():
#     print(a)
# fun()
# fun1()

#-----------
# def fun():
#     a = 21
#     print(a)
# fun()


# def my_decorator(func):
#     def wrapper():
#         print("Something.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello = my_decorator(say_hello)

# say_hello()



# =====================================================

l = True
pin = 1234
balance = 15000

while l:
    number=int(input(
    """     
(Press (1) for PIN ) : -
(Press (2) for Check Balance ) : -
(Press (3) for Cash Withdrow ) : -
(Press (4) for Add Cash ) : - 
Enter Number: - """))
    if number == 1:
        pin1=int(input("Enter PIN : - "))
        if pin == pin1:
            print("Your ATM PIN is ")
        else:
            print("You Enter Wrong PIN Number ")
        
    elif number == 2:
         pin1=int(input("Enter PIN : - "))
         if pin==pin1:
              print("Your Balance is :- ",balance)
              print(balance)
         else:
            print("Invalid PIN ")


    elif number == 3:
        pin1=int(input("Enter PIN : - "))
        if pin==pin1:
             amount=int(input("Enter Amount for Withdrow Cash : - "))
             balance=balance-amount
             print("Your Balance is : - ",balance)
        else :
            print("Invalid PIN")



    elif number == 4:
         pin1=int(input("Enter PIN : - "))
         if pin==pin1:
              amount=int(input("Enter amount for Add Cash : - "))
              balance=balance+amount
              print("Your Balance is : - ",balance)
         else:
              print("Invalid PIN")


    
    i = input("Enter 'y', for Continue & Enter 'n' , for break : -  ")
    if i=='y':
        l=True
    elif i=='n':
        l=False
    else:
        l=False
#=================================
# lambda
# z = lambda a:a*10
# print(z(25))

# a = lambda a:a+10
# print(a(20))

# a = lambda a:a-10
# print(a(20))

# l = lambda a,b,c : a+b-c
# print(l(2,3,4))

# l = lambda a,b:a*b
# print(l(2,4))


# ===============================================


# def abc():
#     print("Hello worldddddddddddddd")
# def ab():
#     print("Helloo")





# for i in name:
#     if i.isupper():
#         name1+=i
#     elif i==" ":
#         name1+=" "    
#     else:    
#         name1+=chr(ord(i)-32)
    
# print(name1)
