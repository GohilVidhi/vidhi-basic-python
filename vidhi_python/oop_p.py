# Data member

# class fun():
#     name="abcd"
#     age=22
#     subject="oops"
#     print(name,age,subject)

# f=fun()
# print(f.name)
# print(f.age)
# print(f.subject)
#---------------------------

# Data member
# class abc():
#     name="vidhiiii"
#     age=23
#     city="rajkot"

# d=abc()
# print(d.name)
# print(d.age)
# print(d.city)

# ============================================================
# Data Function

# class abc():
#     name="vidhi"
#     age=22
#     city="baroda"

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.city)
# f=abc()
# f.display()

# --------------------------------------
# class abc():
#     name="hujejnv"
#     age=31
#     sub="english"

#     def abcd(self):
#         print(self.name)
#         print(self.age)
#         print(self.sub)

# d=abc()
# d.abcd()

# =================================================================

# class abc():
#     name="django"
# d=abc()

# d.name="python"
# print(d.name)

# class ab():
#     name="idhi"
# v=ab()
# v.name="vidhi"
# print(v.name)



#=======================================================

# class vehicle:
#     def __init__(self,name,model,price):
#         self.name=name
#         self.model=model
#         self.price=price

#         print(self.name)
#         print(self.model)
#         print(self.price)

# d=vehicle("activa","5G",70000)


# class car():
#     def __init__(self,name,model,price):
#         self.name=name
#         self.model=model
#         self.price=price

#         print(self.name)
#         print(self.model)
#         print(self.price)

# d=car("Audi",700,4000000)        
        
# class ca():
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city

#         print(self.name)
#         print(self.age)
#         print(self.city)

# d=ca("jbi",22,"ahmedabad")
# =========================================================

# class bank():
#     def __init__(self,name,age,pin):
#         self.name=name
#         self.age=age
#         self.pin=pin

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.pin)

# b=bank("vidhi",23,12345)
# b.display()
# print(b.pin)
    

# class abc():
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city

#     def abcd(self):
#         print(self.name)
#         print(self.age)
#         print(self.city)

# d=abc("jkdbcjkb",22,"ahmedabad")
# d.abcd()
# print(d.city)

# class fun():
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city

#     def ab(self):
#         print(self.name)
#         print(self.age)
#         print(self.city)

# d=fun("jcndj",22,"dj")
# d.ab()
# print(d.city)

# ======================================================================

# class xy():
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city

#     def ab(self):
#         print(self.name)
#         print(self.age)
#         print(self.city)

# d=xy("vidhiiii",22,"Ahmedabad")
# print(d.name)
# d.ab()

#========================================================

# class ab():
#     def __init__(self,name,model,price):
#         self.name=name
#         self.model=model
#         self.price=price
    
#     def abc(self):
#         print(self.name)
#         print(self.model)
#         print(self.price)

# d=ab("audi",700,4000000)
# d.abc()

#===========================================================

#Exersice:

# class python:
#     def display(self):
#         print("python method")

#     def display1(self):
#         print("python 2")

# class android:
#     def display(self):
#         print("android method")

# p=python()
# a=android()

# p.display()
# p.display1()
# a.display()

#----------------------------------------------------------

# class python:
#     def dis(self):
#         print("1")
#     def dis2(self):
#         print("2")

# class django:
#     def dj(self):
#         print("3")
    
# d=python()
# v=django()

# d.dis()
# d.dis2()
# v.dj()
#====================================================
#Access variable

# class car:
#     color="red"
#     brand="tata"

# c=car()
# print(c.color)
# print(c.brand)
#--------------
# class car:
#     color="black"
#     brand="tata"
# d=car()
# print(d.color)
# print(d.brand)
#--------------
# class car:
#     color="black"
#     brand="audi"
#     wheels=4

# d=car
# print(d.brand)
# print(d.color)
# print(d.wheels)
#------------------
# class bike:
#     color="blue"
#     brand="shine"
#     model=2023

# obj=bike
# print(obj.color)
# print(obj.brand)
# print(obj.model)


# ===========================================

# init Function

# class car:
#     def __init__(self,color,brand,wheels,model):
#         self.color=color
#         self.brand=brand
#         self.wheels=wheels
#         self.model=model
    
#     def abc(self):
#             print(self.color)
#             print(self.brand)
#             print(self.wheels)
#             print(self.model)

# obj=car("red","tata",4,2023)
# obj.abc()
#--------------------------------

# class bike:
#     def __init__(self,brand,model,price,color):
#         self.brand=brand
#         self.model=model
#         self.price=price
#         self.color=color
    
#     def ab(self):
#         print(self.brand)
#         print(self.model)
#         print(self.price)
#         print(self.color)

# a=bike("shine",2023,80000,"black")
# a.ab()        


#==================================================
#without Parameter:

# class mobile():
#     def __init__(self):
#         self.mobile="samsung"
#         print(self.mobile)

# d=mobile()
#=====================================================
# parameter constructor

# class mobile():
#     def __init__(self,r,m,v):
#         self.realme=r
#         self.mi=m
#         self.vivo=v
    
#     def display(self):
#         print(self.realme)
#         print(self.mi)
#         print(self.vivo)

# d=mobile("realme","Mi","vivo")
# d.display()
#-------------------------------


# class vidhi():
#     def __init__(self,name,age,subjet) -> None:
#         self.name=name
#         self.age=age
#         self.subject=subjet

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.subject)

# obj=vidhi("vidhi",23,"python")
# obj.display()

# class add:
#     def __init__(self,a1,a2):
#         self.a1=a1
#         self.a2=a2

#     def ab(self):
#         print(self.a1+self.a2)

# ob=add(100,200)
# ob.ab()
    
# ========#=====#////// ================================================
# student info 
# class student:
#     def vidhi():
#         name="vidhi gohil"
#         age=23
#         subject="python"
#         print(f"{name}\n{age}\n{subject}")

#     def nik():
#         name="nikhil gohil"
#         age=25
#         subject="php"
#         print(f"{name}\n{age}\n{subject}")        
    
#     def d():
#         name="ramm"
#         age=22
#         subject="java"
#         print(f"{name}\n{age}\n{subject}")

# obj=student
# obj.vidhi()
# obj.nik()
# obj.d()


# class student:
#     def details():
#         name="Names."
#         age="Age."
#         sub="Subjects."
#         print(f"{name}\t{age}\t{sub}")

#     def vidhi():
#         name="vidhi"
#         age=23
#         sub="python"
#         print(f"{name}\t{age}\t{sub}")
    
#     def nikhil():
#         name="nikhil"
#         age=25
#         sub="php"
#         print(f"{name}\t{age}\t{sub}")

#     def r():
#         name="ram"
#         age=25
#         sub="java"
#         print(f"{name}\t{age}\t{sub}")

# ab=student
# ab.details()
# ab.vidhi()
# ab.nikhil()
# ab.r()
#===============================================================

# class n():
#     def ab():
#         print("monkey not patching")

# obj=n()
# n.ab()

# def abc():
#     print("this is monkey patching")

# n.ab=abc
# print("after monkey patching")
# n.ab()    

#================================================================

# class AA:
#     a=10
#     b=10.0
#     c="vidhiii"

# obj=AA
# print(obj.a)
# print(obj.b)
# print(obj.c)
# ============================================================

# class A:
#     a=100
#     b=11.11
#     c="vidhi"

#     def display(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)

# obj=A()
# obj.display()


#==============================================================

# class a():
#     print("V")

# class b():
#     print("D")

# a=b
# abj=a()
#===========================================================

# class A():
#     def __init__(self,a,b,c):
#         self.a=a 
#         self.b=b
#         self.c=c  
#     def display(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
# obj=A(10,10.11,"vidhi")
# obj.display()

#------------------------------------------

# class A():
#     def __init__(self,a,b,c):
#         self.a=a 
#         self.b=b
#         self.c=c
#     def display(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)

# obj=A(10,10.11,"sdkdsnv")
# obj.display()
    

# class A():
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#     def display(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
# p1=A(1,2,"df")
# p1.display()


