# list=[11,33,444,5555,36663,1,33,45,545,4356,46,54,654,65,7]
# print(min(list))
# print(max(list))
# print(len(list))
# print(sum(list))
#----------------------

# list=[1,2,44,4,5435,True,False,None,"vidhi"]
# print(list)
#---------------
# list=[50,[50,"vv"],('gfdsh',"33"),{"vidhi",43,4.6},{"fruits":"abc"}]
# print(list[4])
# li=[1,2,[3,4,5,8888,999],[6,7,8,9]]
# print(li[3][3])
# print(li[3][:3])
# print(li[2][0:4])
# print(li[3][-1])
# #-----------
# li = [1,3.14,True,False,"vidhi",None]
# li[2]=44.4
# print(li)
# print(li[4])
# print(li[-4])
# print(li[:2])
# print(li[:])
# print(li[::-1])

#------------

# li=[1,2.4,'string','list',False,True,None,33]

# for add list
# li.append('xyz')
# li.insert(2,33)
# li.extend([44,44,55,44,33])
# print(li)


# for delete list
# li.pop(-5)
# li.remove(1)
# li.clear()
# del li
# print(li)


# li.reverse()
#--------
# l1=[1,2.4,'string','scjbd',False,True,None]
# l2=[33,66,7.7,True,False]

#l2.extend(l1)
#print(l2)

# l3=l1+l2
#print(l3)

# l=[5,4,3,1,45,2.5,2]
# l.sort()
# l.reverse()
# print(l)
#-----------
# li=['v','i','d','h','i']
# print(''.join(li))
#--------------
# a=int(input("Enter number : "))
# print(a)
#------------


#-------------------
#newList = [12, 35, 9, 56, 24] output: [24, 56, 9, 35, 12]

# list=[11,12,13,14,15]

# list[0],list[-1]=list[-1],list[0]
# print(list)
#=======================

#Python Program to count unique values inside a list

# list = [1,2,3,3,4,4,5,6]
# count = 0
# l1 = []

# for i in list:
#     if i not in l1:
#         count += 1
#         l1.append(i)
# print("Unique No. is : ",list)
#==================================

# Python program to print positive numbers and nagitive numbers in a list
# list1 = [12, -7, 5, 64, -14]
# for num in list1:
#     if num >= 0:
#         print(num, end = " ")
# list=[1,2,3,-5,-88]
# for num in list:
#     if num <= 0:
#         print(num,end=" ")

# #====================================

# loop through a tuple of mixed data type and extract only integer values
# mix_tuple = (1, 2.5, "hello", True, 3, 4.2, -5)
# int_list = []
# for item in mix_tuple:
#     if isinstance(item, int):
#         int_list.append(item)
# print("Integers in the tuple:", int_list)


# mixed_tuple = (1,2,3,-4,-6,"vidhi",True,3.77)
# int_list = []
# for item in mixed_tuple:
#     if isinstance(item,int):
#         int_list.append(item)
#==================================================

# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
          # output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# n = int(input("Enter Number : "))
# d = {}
# for x in range(1,n+1):
#     d[x] = x*x
# print(d)



# a = int(input("Enter Number : "))
# d = {}
# for i in range(1,a+1):
#     d[i] = i*i
# print(d)

# v = int(input("Enter Number : "))
# d = {}
# for i in range(1,v+1):
#     d[i] = i*i
# print(d)
#==================================================
#Output
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=" ")
#     print()


# for i in range(1,5):
#     for j in range(i):
#         print(i,end = " " )
#     print()
#===========================================
#output
#(6, 9, 8, 6)
# t1 = (1,2,3,4)
# t2 = (3,5,2,1)
# t3 = (2,2,3,1)

# result = tuple(map(sum,zip(t1,t2,t3)))

# print("sum of tuples : ")
# print(result)
#------------------------------------------
# Output
# sum of tuple (5, 9, 10, 6) 

# d1 = (1,2,3,4)
# d2 = (2,3,4,1)
# d3 = (2,4,3,1)

# result = tuple(map(sum,zip(d1,d2,d3)))

# print("sum of tuple",result)
#==========================================

# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# output = [C[i::3] for i in range(3)]
# print(output)

# C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# result = [C[i::3]for i in range(4)]
# print(result)
#============================================
#Write a Python program to insert a given string at the beginning of all items in a list.
# num=[1,2,3,4,5,6,7,8,9,10] 
# string = "student-"
# result = [string + str(i) for i in num[::-1]]
# print(result)
#-------------------------------------------
# num = [1,2,3,4,5]
# string = 'Student - '
# output = [string + str(i) for i in num[::-1]]
# print(output)
#=======================================================
# Write a Python script to concatenate the following dictionaries to create a new one. Sample Dictionary :
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}

# new_dict = {**dic1, **dic2, **dic3}
# print(new_dict)
#------------------------------
# dict1 = {1:10 , 2:20}
# dict2 = {3:30 , 4:40}
# dict3 = {5:50 , 6:60}

# new_dict = {**dict1 , **dict2 , **dict3}
# print(new_dict)
#===========================================
#Write a Python program to find the list in a list of lists whose sum of elements is the highest.

# num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# print(max(num, key=sum))

# # ---------------------
# num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# sum = 0
# max = 0

# for i in num(1,num+1):
#     new = max(num, key=sum)
#     if new:
#         print(new)
    
#----------------------
# num = [[1,2,3333],[4,5,6],[10,11,12],[7,8,9]]

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

#============================================







