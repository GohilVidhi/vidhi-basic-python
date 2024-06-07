# fruits=["apple","banana","cherry"]
# for i in fruits:
#     print(i)

# for i in range(-11,11):
#     print(i)

# for i in range(0,30,5):
#     print(i)

# numbers=[1,2,3,4,5]
# for i in numbers:
#     square=i**2
#     print(i,':',square)

# for i in range(1,11):
#     if i%2==0:
#         print("Even number",i)
#     else:
#         print("Odd number",i)

#---------------------------------

# Break Statment :
# for i in range(1,11):
#     if i==8:
#         break
#     else:
#         print(i)
#---------------------

#Continue statment : 
# for i in range(1,10):
#     if i == 8:
#         continue
#     else:
#         print(i)
#-------------------------

#Pass statment:
# num=[1,2,3,4,5,6]
# for i in num:
#     pass

#-----------------------
# a=int(input("Enter value :- "))
# for i in range(a):
#     for j in range(i+1):
#         print("*",end=" ")
#     print('')
# #--------------------------

#Exercise:
#1
#Print the first 10 natural numbers using for loop.

# for i in range(1,11):
#     print(i)
#=====================

#Exercise:
#2
#Python program to print all the even numbers within the given range.


# for i in range(1,21):
#     if i%2==0:
#         print(i)
#=====================

#Exercise:
#3
#Python program to calculate the sum of all numbers from 1 to a given number.

# number = int(input("Number: "))
# sum = 0
# for i in range(1,number + 1):
#     sum += i
#     print(sum)
#=========================

#Exercise:
#4
#Python program to calculate the sum of all the odd numbers within the given range.

# number=int(input("Enter Number : "))
# sum=0

# for number in range(1,number+1):
#     if number%2!=0:
#        print(number)
#        sum=sum+number
# print(sum)



# number=int(input("Enter number : "))
# sum=0
# for number in range(1,number+1):
#     if number%2!=0:
#         print(number)
#         sum=sum+number
# print(sum)
#------------
#no=int(input("Even no"))
# sum=0
# for i in range(1,10):
#     if i%2==0:
#         print(i)
#         sum=sum+i
# print(sum)
#===========================
#Exercise:
#5
#Python program to print a multiplication table of a given number
# number=int(input("Enter Number : "))

# for i in range(1,11):
#     d=number*i
#     print(number,'*',i ,'=',d)
#---------------------
# no=int(input("Enter number: "))
# for i in range(1,11):
#     print(no,'*',i,'=',no*i)
#==============================-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Exercise:
#6
#Python program to count the total number of digits in a number.


# n=58739999
# count=0
# for i in str(n):

#     count=count+1
# print(f"Total Number of Digits is :{count}")


#======================================
#Exercise:
#7
#Python program to count the number of even and odd numbers from a series of numbers

# number=[1,2,3,4,5,6,7,8,9]
# even_number=0
# odd_number=0
# for i in number:
#     if i%2==0:
#         even_number+=1
#     else:
#         odd_number+=1
# print("even number is : ",even_number)
# print("even number is : ",odd_number)
#----------
# number=[1,2,3]
# even=0
# odd=0
# for i in number:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("even no: ",even)
# print("odd no: ",odd)
#================================
#Exercise:
#8

# words=["apple","banana","cherry"]
# for word in words:
#     for latters in word:
#         print(latters)
#     print("////")

# a=["fr","dsfdsg","dsfgdg"]
# for ab in a:
#     for latter in ab:
#         print(latter)
#     print("////")

#===========================================
#Exercise:
#9
#Display numbers from -10 to -1 using for loop

# number=[]

# for num in range(-10,0):
#     number.append(num)
# print(number)
        
# num=[]
# for number in range(-10,0):
#     num.append(number)
#     print(num)

#====================================================
#Python program to convert the month name to a number of days. 

# print("jan","feb","march","april","may","june","july","august","sep","oct","nove","dece")
# month_name=input("Enter Month : ")

# if month_name == "feb":
#     print("numbers of days in feb 28/29..")
# elif month_name in ("april","june","sep","nove"):
#     print("numbers of days is 30..")
# elif month_name in ("jan","march","may","july","august","nove","dece"):
#     print("numbers of days is 31..")
# else:
#     print("Wrong input")
#-------------------------------------------------------------------------
# print("jan","feb","march","april","may","june","july","august","sep","oct","nove","dece")
# month=input("Enter Month : ")

# if month == "feb":
#     print("28/29 days of this month")
# elif month in ("april","june","sep","nove"):
#     print("numbers of days is 30")
# elif month in ("jan","march","may","july","august","nove","dece"):
#     print("numbers of days is 31")
# else:
#     print("you enter wrong month..")
#===============================================
#Exercise:
#10
#Python program to check the validity of password input by users

# p="V@3"
# l=0
# u=0
# d=0
# s=0

# for i in p:
#     if i.islower():
#         l+=1
#     if i.isupper():
#         u+=1
#     if i.isdigit():
#         d+=1
#     if i=="@" or i=="#" or i=="$":
#         s+=1
# if l>=1 and u>=1 and d>=1 and s>=1:
#     print("Valid Password")
# else:
#     print("Invalid Password")

#===========================================================
# p="vVidhi123"

# u=0
# l=0
# d=0
# s=0

# for i in p:
#     if i.isupper():
#         u+=1
#     if i.islower():
#         l+=1
#     if i.isdigit():
#         d+=1
#     if i=="@" or i=="#" or i=="$":
#         s+=1
# if u>=1 and l>=1 and d>=1 and s>=1:
#     print("valid password")
# else:
#     print("invalid password")


# for i in range(1,50):
#     if i%2==0:
#         if i==36:
#             continue
#         print(i)
   

#===========================================
#Exercise:
#11
#loop through a tuple of mixed data type and extract only integer values

# my_tuple=(1,2,3,4,"aaa",45,56,546,56,"bbdd")
# value=[i for i in my_tuple if isinstance(i,str)]
# value1=[i for i in my_tuple if isinstance(i,int)]
# print(value)
# print(value1)

# Tuple=[1,2,3,4,"fdgfdg","gfdgdf",54345]
# value=[i for i in Tuple if isinstance(i,int)]
# print(value)
#########################################
# i=1
# while i<11:
#     print(i)
#     i+=1

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i=1
# while i<10:
#     print(i)
#     i+=1
# else:
#     print("chsdb")

# for x in range(0, 30, 10):
#   print(x)
# for i in range(-10,0):
#     print(i)

# for i in range(1,10):
#     pass


# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()



# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i-1):
#         print("*",end=" ")
#     print()


# n = 5
# for i in range(n, 0, -1):
#     for j in range(n-i):
#         print(" ", end=" ")
#     for k in range(2*i-1):
#         print("*", end=" ")
#     print()



# n=58739999909
# count=0
# for i in str(n):

#     count+=1
# print(count)


# n=0
# while n<6:
#     n+=1
#     if n==3:
#         continue
#     print(n)

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")




