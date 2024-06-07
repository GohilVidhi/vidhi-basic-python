

# Example 1:
# Print the first 10 natural numbers using for loop.

# for i in range(1,11):
#     print(i)


#***********************************************************************************************************
# Example 2:
# Python program to print all the even numbers within the given range.

# n=int(input("Enter Number : "))
# for i in range(n):
#     if i%2==0:
#         print(i)
# #-----------------------------
# for i in range(1,21):
#     if i%2==0:
#         print(i)


#*********************************************************************************************************
# Example 3:
# Python program to calculate the sum of all numbers from 1 to a given number.

# num=int(input("enter number : "))
# sum=0
# for i in range(1,num+1):
#     sum+=i
# print("sum of 1 to", num)
# print("Total sum : ",sum)


#**********************************************************************************************************************************
# Example 4:
# Python program to calculate the sum of all the odd numbers within the given range.

# a=int(input("enter 1st number : "))
# b=int(input("enter last number : "))
# sum=0
# for i in range(1,b+1):
#     if i%2!=0:
#         sum+=i
#         print(i)

# print("sum of all odd number ")
# print("total sum ",sum)


#********************************************************************************************************************
# Example 5:
# python program to print a multiplication table of a given number
# 1.
# num1=int(input("Enter number : "))
# num2=int(input("Enter last num : "))
# for i in range(num1,num2+1):
#     for a in range(1,11):
#         b=i*a
#         print(i,"*",a,":",b)
#     print(" ")

# n=int(input("Enter num "))
# for i in range(1,n+1):
#     for a in range(1,11):
#         b=i*a
#         print(i,"*",a,":",b)
#     print(" ")




# n=int(input("Enter num "))

# for a in range(1,11):
#         b=n*a
#         print(n,"*",a,":",b)
   
#--------------------------------------------------------
# 2.
# num1=int(input("Enter number : "))
# num2=int(input("Enter number : "))

# for i in range(num1,num2+1):
#     for a in range(1,11):
#         print(i,"*",a,":",i*a)
#     print(" ")
#--------------------------------------------------------
# 3.
# num1=int(input("Enter A Number : "))
# num2=int(input("Enter A Number : "))

# for i in range(num1,num2+1):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print(" ")



#********************************************************************************************************    
# Example 6:
# Python program to count the total number of digits in a number.
# num=12034
# count = 0
# for i in str(num):
#     count += 1
# print(count)


#**********************************************************************************************************
# Example 7:
# Python program to count the number of even and odd numbers from a series of numbers.

# num=int(input("Enter numbers : "))
# even=0
# odd=0
# for i in range(1,num+1):
#     if i%2==0:
#         even+=1
        
#     else:
#         odd+=1
#     print(i)      
# print("Even number is ",even)
# print("odd number is ",odd)


# ****************************************************************************************************
# Example 8:
# Python program to display all numbers within a range except the prime numbers

# n=int(input("Enter number : "))
# c=0

# for i in range(1,n+1):
#     if n%i==0:     # 10%1==0  10%2==0 10%5==0 10%10==0
#         c+=1
# if c==2:
#     print(i, "prime number")    
# else:
#     print(i, "not a prime number") 


# ************************************************************************
# Example 9: 
# Python program that accepts a string and calculates the number of digits and letters.
# 1.
# name="python12345"
# d=0
# a=0
# for i in name:
#     if i.isdigit():
#         d+=1
#     if i.isalpha():
#         a+=1
# print(d)
# print(a)
#---------------------------------------------

# 2.
# name="vidhi1234"
# digit=0
# alpha=0
# for i in name:
#     if i.isdigit():
#         digit+=1
#     else:
#         alpha+=1
# print(digit)
# print(alpha)
# ***************************************************************************

# *************************************************************************
# A:
# Q : 1 ==>  words= ["Apple", "Banana", "Car", "Dolphin" ]
#            output : A
#                     p
#                     p
#                     l
#                     e
#                     /////
#                     B
#                     a
#                     n
#                     a
#                     n
#                     a
#                     /////
#                     C
#                     a
#                     r
#                     /////
#                     D
#                     o
#                     l
#                     p
#                     h
#                     i
#                     n
#                     /////

# Answer :->
# words= ["Apple", "Banana", "Car", "Dolphin" ]

# for i in words:
#     for l in i:
#         print(l)
#     print("////")


# ****************************************************************************************************
# Q : 2 ==>  
# Count the total number of digits in a number:

# n=123
# count=0
# for i in str(n):
#     count+=1
# print(count)


# ************************************************
# Q : 3
# Display numbers from -10 to -1 using for loop:

#using for loop:
# for i in range(10,0,-1):
#     print(i)

#-----------------------------
#using while loop:
# i=10
# while i>=1:
#     print(i)
#     i-=1

# *****************************************************************************
# Q : 4 ==>  
# Python program to check the validity of password input by users:

# pas="Vid12@"

# lower=0
# upper=0
# digit=0
# special=0

# for i in pas:
#     if i.islower():
#         lower+=1
#     if i.isupper():
#         upper+=1
#     if i.isdigit():
#         digit+=1
#     if i=="@" or i=="#" or i=="&" or i=="$":
#         special+=1
# if lower>=1 and upper>=1 and digit>=1 and special>=1:
#     print("Valid password")
# else:
#     print("Invalid Password")

# ****************************************************************************
# Q : 5 ==>  
# Python program to convert the month name to a number of days. 

# print('jan','feb','march','april','may','june','july','august','sep','oct','nove','dec')

# month=input("Enter Month : ")
# if month == "feb":
#     print("28/29 days")
# elif month in ('april','june','sep','nove'):
#     print("30 days ")
# elif month in ('jan','march', 'may','july','august','oct','dec'):
#     print("31 days")
# else:
#     print("Enter wrong month")


# ****************************************************************************************************
# Q : 6 ==>  
# loop through a tuple of mixed data type and extract only integer values

# 1.
# tup = (1,2,3,4 ,'abc',5,'red',6,'blue')
# tup2=[]
# for i in tup:
#     if type(i)==str:
#         tup2.append(i)
# print(tup2)
#--------------------

# 2.
# tup = (1,2,3,4 ,'abc',5,'red',6,'blue')

# tup2=[i for i in tup if isinstance(i,int)]
# print(tup2)

#-----------------------

# 3.
# l1=[1,2,3,"python","django",1.5,3.6]
# l2=[]

# for i in l1:
#     if type(i)==int:
#         l2.append(i)
# print(l2)

# ******************************************************************************

# B:
# Q : 1 ==>  
# newList = [12, 35, 9, 56, 24] #output: [24, 35, 9, 56, 12]

# 1.
# newList = [12, 35, 9, 56, 24]
# newList[0], newList[-1] = newList[-1], newList[0]
# print(newList)



# 2.
# newList = [12, 35, 9, 56, 24]
# for i in range(len(newList)):
#     if i==0:
#         newList[i], newList[-1] = newList[-1], newList[i]
#         break
# print(newList) 

# l1=[1,2,3,4,5]
# l1[0],l1[-1]=l1[-1],l1[0]
# print(l1)

# *************************************************************************
# Q : 2 ==> 
#  Addition of first and last digit of the number ==> number = 12475 ==> output=6

# digit=12475
# num=str(digit)
# first_digit=int(digit[0])
# last_digit=int(digit[-1])

# sums=first_digit+last_digit
# print("last number is",sums)

 
# **************************************************************
# Q : 3 ==> 
# Python program to print positive numbers and nagitive numbers in a list

# l1=[1,2,3,4,5,-1,-2,-3,-4,-5,0,0,0]
# a2 = []
# n2 = []
# for i in l1:
#     if i>=0:
#         a2.append(i)
#     elif i<=-1:
#         n2.append(i)
# print("Negative No.-",n2)
# print("Positive No.-" , a2)




# ****************************************************************************

# Q : 4 ==>  
# Python Program to count unique values inside a list
# l1=[1,2,3,4,5,1,2,3,4,5,6,7,8,1,2,3,4,5,6]
# l2=[]

# for i in l1:
#     if l1.count(i)<=1:
#         if i not in l2:
#             l2.append(i)

# print(l2)        

# l1=[1,2,3,4,5,6,1,2,3,4,5,6,7]
# l2=[]
# for i in l1:
#     if l1.count(i)<=1:
#         if i not in l2:
#             l2.append(i)
# print(l2)
# ******************************************************************************
# Q : 5 ==> 
# Count the vowels in a string
# aeiou

# name="my name is vidhi"
# a="aeiou"
# count = 0

# for n in name:
#     if n in a:
#         count=count+1

# print(count)


# ****************************************************************************

# C:
# Q : 1 ==> 
# Print the value of key ‘history’ from the below dict:
# dict1 = {
#                 "class": {
#                     "student": {
#                         "name": "vidhi",
#                         "mark": {
#                             "physics": 60,
#                             "history": 77
#                         }
#                     }
#                 }
#             }

# dict2 = dict1["class"]["student"]["mark"]["history"]

# print(dict2)

# **********************************************************************************

# Q : 2 ==> 
# Check if a value exists in a dictionary
# dict = {'a': 100, 'b': 200, 'c': 300} 

# if 100 in dict.values():
#     print("Present in dict")
# else:
#     print("Not present in dict")


# *******************************************************************************

# Q : 3 ==>  
#  Change value of a key in a nested dictionary
# sample_dict = {
#                 'emp1': {'name': 'Jhon', 'salary': 7500},
#                 'emp2': {'name': 'Emma', 'salary': 8000},
#                 'emp3': {'name': 'Brad', 'salary': 500}
#             }       


# sample_dict['emp1']['name']='helli'
# sample_dict['emp2']['salary']=10000
# print(sample_dict)


# ****************************************************************************************************


# D:
# Q : 1 ==> 
# l1=["python"," ", " "," ","java"] 

# Answer:-

# l2=[]
# for i in l1:
#     if i == " ":
#         pass
#     else:
#         l2.append(i)
# print(l2)


# ****************************************************************************************************

# Q : 2 ==> 
# numbers = [12, 75, 150, 180, 145, 525, 50] using for loop
#           output =  75
#                     150
#                     145

# Answer :-

# numbers = [12, 75, 150, 180, 145, 525, 50]
# num=[1,2,4]
# for i in num:
#     print(numbers[i])


# *************************************************************************

# Q : 3 ==> 
# Write a program to print the cube of all numbers from 1 to a given number
# 1.:

#  only CUBES :
# n=int(input("Enter number : "))
# cubes=[]
# for i in range(1,n+1):
#     cubes.append(i**3)

# for cube in cubes:
#     print(cube)
#--------------------

# 2.
# Only EVEN numbers cube :-
# n=int(input("Enter number : "))
# cubes=[]
# for i in range(1,n+1):
#     if i%2==0:
#         cubes.append(i**3)
# for c in cubes:
#     print(c)
#---------------------

# 3.
# SQUARE :.
# n=int(input("Enter number"))
# sq=[]
# for i in range(1,n+1):
#     sq.append(i*2)
# for s in sq:
#     print(s)

#----------------------
# Only Odd Number SQUARE : -

# n=int(input("Enter number : - "))
# sq=[]
# for i in range(1,n+1):
#     if i%2==0:
#         pass
#     else:
#         sq.append(i**2)
# print(sq)

# ****************************************************************************************************

# Q : 4 ==> 

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
# output = Given list: [10,20, 30, 40, 10]
#                      result is True

#          numbers_y = [75, 65, 35, 75, 30]
#                       result is False

# Answer : -

# l1= [10, 20, 30, 40, 10]

# 1.
# if l1[0]==l1[-1]:
#     print("True") 
# else:
#     print("False") 
#--------------------

# 2.

# l1= [10, 20, 30, 40, 10]
# l2 = [75, 65, 35, 75,30]

# if l1[0]==l1[-1]:
#     print("True")
# if l2[0]==l2[-1]:
#     print("True")
# else:
#     print("False")


# ****************************************************************************************************

# Q : 5 ==> 
# marks={"m1":92 , "m2":56 , "m3":88 , "m4":97 , "m5":89}
    #   ==> output: Sum of Values : 422 

# Answer : 

# marks={'m1':92,'m2':56,'m3':88,'m4':97,'m5':89}
# sum=sum(marks.values())
# print(sum)

# ****************************************************************************************************

# Q : 6 ==> 
# marks={"m1":78 , "m2":89 , "m3":64 , "m4":35 , "m5":71}
    #    Maximum : 89
    #    Minimum : 35

# Answer:

# marks={"m1":78 , "m2":89 , "m3":64 , "m4":35 , "m5":71}
# Maximum=max(marks.values())
# Minimum=min(marks.values())
# print("Maximum : ",Maximum)
# print("Minimum : ",Minimum)


# ****************************************************************************************************

# Q : 7 ==> 
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
        #   output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#Answer :
# n = int(input("Enter Number : "))
# d = {}
# for x in range(1,n+1):
#     d[x] = x*x
# print(d)


# ****************************************************************************************************

# Q : 8 ==>
# output : 
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5  

# Answer :

# for i in range(1,6):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# *****************************************************************************

# ******************************************************************************
# E:
# Q : 1 ==>
# Write a Python program to compute the element-wise sum of given tuples.
        #   Original lists:
        #   (1, 2, 3, 4)
        #   (3, 5, 2, 1)
        #   (2, 2, 3, 1)
        #   Element-wise sum of the said tuples:
        #   (6, 9, 8, 6)

# Answer :
# a=(1, 2, 3, 4)
# b=(3, 5, 2, 1)
# c=(2, 2, 3, 1) 

# a1=a[0]+b[0]+c[0]
# b1=a[1]+b[1]+c[1]
# c1=a[2]+b[2]+c[2]
# d1=a[3]+b[3]+c[3]

# num=a1,b1,c1,d1
# print(tuple(num))


# *********************************************************************

# Q : 2 ==> 
# # Write a Python program to check if a list is empty or not.
# l=[1]

# Answer :
 
# if not l:
#     print("The list is empty")

# else:
#     print("The list is not empty")


# *******************************************************************************
# Q : 3 ==> 
# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


# Answer :

# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new = [C[i::3] for i in range(3)]
# print(new)
# new=[C[i::3] for i in range(3)]
# print(new)

# ***************************************************************************

# Q : 4 ==> Write a Python program to insert a given string at the beginning of all items in a list.
#           num=[1,2,3,4,5,6,7,8,9,10]  
#           output: [student-10] [student-9] [student-8] [student-7] [student-6] [student-5] [student-4] [student-3] [student-2] [student-1]  


# Answer :

# num=[1,2,3,4,5,6,7,8,9,10] 
# string = "student-"
# result = [string + str(i) for i in num[::-1]]
# print(result)


# *************************************************************************
# Q : 5 ==>  
# Write a Python script to concatenate  the following dictionaries to create a new one.
# concatenate -> join

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Answer : -
# new_dict={**dic1,**dic2,**dic3}
# print(new_dict)


# **********************************************************************

# Q : 6 ==> 
# Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]


#Answer : 
# 1.
# num = [[1,2,3], [4,5,6], [10,11,12], [7,8,900]]
# print(max(num, key=sum))
# print(max(num,key=sum))
#------------------------------------
# 2.
# num = [[1,2,33],[4,5,6],[10,11,12],[7,8,9]]

# a=sum(num[0])
# b=sum(num[1])
# c=sum(num[2])
# d=sum(num[3])

# print(a)
# print(b)
# print(c)
# print(d)

# if a>b and a>c and a>d:
#     print(num[0])
# elif b>a and b>c and b>d:
#     print(num[1])    
# elif c>a and c>b and c>d:
#     print(num[2])
# else:
#     print(num[3])

#------------------------------------
# 3.
# num = [[1,2,33],[4,5,6],[10,111,12],[7,8,9]]
# l1=[]
# for i in num:
#     a=sum(i)
#     l1.append(a)
    
# i=max(l1)
# ab=l1.index(i)
# print(num[ab])


# *****************************************************************************

# Q : 6 ==> 
# l1=[1,2,3,4,1,2,3,4,5,6,7]
#           output: [5,6,7]
#                   3

# Answer : -
# 1.
# l1 = [1,2,3,4,1,2,3,4,5,6,7]
# l2 = l1[8:]
# print(l2)

#---------
# 2.

# l1=[1,2,3,4,1,2,3,4,5,6,7,8,]
# l2=[]
# l3=[]

# for i in l1:
#     if l1.count(i)<=1:
#         if i not in l2:
#             l2.append(i)

#     else:
#         if i not in l3:
#             l3.append(i)

# print(l2)
# print(len(l2))
# print(l3)
# print(len(l3))


#-----------------


# l1=[1,2,3,4,1,2,3,4,5,6,7]
# l2=[]
# for i in l1:
#     if l1.count(i)<=1:
#         if i not in l2:
#             l2.append(i)
# print(len(l2))
# print(l2)

# for row in range(1,6):
#     for col in range(1,11):
#         if row==1 and col==1:
#             print("*",end=" ")
#         elif row==2 and col==1:
#             print("*",end=" ")
#         elif row==3 and col==1:
#             print("*",end=" ")
#         elif ((row==1 or row==5) and col==20) or ((row==2 or row==3 or row==4) and col==21) or ((row==1 or row==5) and col==19) :
#             print("*",end=" ")
#         elif row==5 and col==1:
#             print("*",end=" ")
#         elif row==6 and col==1:
#             print("*",end=" ")
#         elif row==7 and col==1:
#             print("*",end=" ")
#         elif row==8 and col==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for row in range(10):
#     for col in range(1,37):
#         if (row==1 and col==1)or (row==1 and col==9)or (row==1 and col==11)or (row==1 and col==12)or (row==1 and col==13)or (row==1 and col==15)or (row==1 and col==16)or (row==1 and col==17)or (row==1 and col==18)or (row==1 and col==19)or (row==1 and col==20)or (row==1 and col==23)or (row==1 and col==24)or (row==1 and col==25)or (row==1 and col==29)or (row==1 and col==30)or (row==1 and col==31):
#             print("*",end="&")
#         elif (row==2 and col==1)or(row==2 and col==9)or (row==2 and col==12)or (row==2 and col==16)or (row==2 and col==21)or (row==2 and col==24)or (row==2 and col==30)or (row==1 and col==33)or (row==1 and col==34)or (row==1 and col==35)or (row==2 and col==34):
#             print("*",end="&")
#         elif (row==3 and col==1)or(row==3 and col==9)or (row==3 and col==12)or (row==3 and col==16)or (row==3 and col==21)or (row==3 and col==24)or (row==3 and col==30)or (row==3 and col==34):
#             print("*",end="&")
#         elif (row==4 and col==1)or(row==4 and col==9)or (row==4 and col==12)or (row==4 and col==16)or (row==4 and col==21)or (row==4 and col==24)or (row==4 and col==30)or (row==4 and col==34):
#             print("*",end="&")
#         elif (row==5 and col==2)or(row==5 and col==8)or (row==5 and col==12)or (row==5 and col==16)or (row==5 and col==21)or (row==5 and col==24)or (row==5 and col==25)or (row==5 and col==26)or (row==5 and col==27)or (row==5 and col==28)or (row==5 and col==29)or (row==5 and col==30)or (row==5 and col==34):
#             print("*",end="&")
#         elif (row==6 and col==3)or(row==6 and col==7)or (row==6 and col==12)or (row==6 and col==16)or (row==6 and col==21)or (row==6 and col==24)or (row==6 and col==30)or (row==6 and col==34):
#             print("*",end="&")
#         elif (row==7 and col==4)or (row==7 and col==6)or (row==7 and col==12)or (row==7 and col==16)or (row==7 and col==21)or (row==7 and col==24)or (row==7 and col==30)or (row==7 and col==34):
#             print("*",end="&")
#         elif (row==8 and col==5)or (row==8 and col==11)or (row==8 and col==12)or (row==8 and col==12)or (row==8 and col==13)or (row==8 and col==15)or (row==8 and col==16)or (row==8 and col==17)or (row==8 and col==18)or (row==8 and col==19)or (row==8 and col==20)or (row==8 and col==23)or (row==8 and col==24)or (row==8 and col==25)or (row==8 and col==29)or (row==8 and col==30)or (row==8 and col==31)or (row==8 and col==33)or (row==8 and col==34)or (row==8 and col==35):
#             print("*",end="&")
#         else:
#             print(" ",end=" ")
#     print()


#============

# for row in range(1,11):
#     for col in range(1,20):
#         if row==1 and col==1 or row==1 and col==7:
#             print("*",end=" ")
#         elif row==2 and col==1 or row==2 and col==7:
#             print("*",end=" ")
#         elif row==3 and col==1 or row==3 and col==7:
#             print("*",end=" ")
#         elif row==4 and col==1 or row==4 and col==7:
#             print("*",end=" ")
#         elif row==5 and col==2 or row==5 and col==6:
#             print("*",end=" ")
#         elif row==6 and col==3  or row==6 and col==5:
#             print("*",end=" ")
#         elif row==7 and col==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
 





# for row in range(1,11):
#     for col in range(1,40):
#         if row==1 and col==1 or row==1 and col==2 or row==1 and col==12:
#             print("*",end=" ")
#         elif row==2 and col==1 or row==2 and col==3 or row==2 and col==11:
#             print("*",end=" ")
#         elif row==3 and col==1 or row==3 and col==4 or row==3 and col==10:
#             print("*",end=" ")
#         elif row==4 and col==1 or row==4 and col==5 or row==4 and col==9:
#             print("*",end=" ")
#         elif row==5 and col==1 or row==5 and col==6 or row==5 and col==8:
#             print("*",end=" ")
#         elif row==6 and col==1  or row==6 and col==7 :
#             print("*",end=" ")
#         elif row==7 and col==1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
 

        
# -=============


# def generate_triangle_pattern(num_rows):
#     for i in range(num_rows):
#         spaces = ' ' * (num_rows - i - 1)
#         asterisks = '*' * (2 * i + 1)
#         print(spaces + asterisks)

# # Adjust the number of rows as needed
# num_rows = 5
# generate_triangle_pattern(num_rows)





# Take user input for the name
# name = input("Enter your name: ")

# # Reverse the name by joining reversed characters
# reversed_name = ''.join(reversed(name))

# # Print the reversed name
# print("Reversed name:", reversed_name)




# name = input("Enter your name: ")


# reversed_name = name[::-1]


# print("Reversed name:", reversed_name)








# Take user input for the name
# name = input("Enter your name: ")

# # Initialize an empty string to store the reversed name
# reversed_name = ""

# # Iterate through the characters of the name using a for loop
# for char in name:
#     # Prepend each character to the beginning of the reversed_name string
#     reversed_name = char + reversed_name

# # Print the reversed name
# print("Reversed name:", reversed_name)


# name=input("Enter Name : ")
# reve=""
# for i in name:
#     reve=i+reve
    
# print(reve) 




# name=input("Enter number : ")
# rev=name[::-1]
# print(rev)


# rev=" ".join(reversed(name))
# print(rev)
# reve=""
# for i in name:
#     reve=i+reve
    
# print(reve)




# a = [1,2,3,4,5,6,7,8]

# odd = list(map(lambda x : x if x%2==0 else 't',a))

# print(odd)



# name="my name is python"
# l1=name.split()
# name1=""  

# for i in l1:
#     name1+=i[0]
# print(name1[:2])    





# name="my name is python"

# name1=name[0]
# for i in range(len(name)):
#     if name[i] == " ":
#         name1+=name[i+1]
# print(name1[:2])        






# name="my name is python"
# name1=""
# # print(name.upper())
# # upper=[]
# name1=name[:]
# print(name1.title())


# for i in range(65,91):
#     print(chr(i),chr(i+32))    



# for i in name:
#     if i.isupper():
#         name1+=i
#     elif i==" ":
#         name1+=" "    
#     else:    
#         name1+=chr(ord(i)-32)
    
# print(name1)





# for i in name:
#     print(ord(i),end=" ")
    
# print()



