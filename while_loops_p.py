#While Loops:-

# a=0
# while a<10:
#     print(a)
#     a+=1


#---------

# count=0
# number=180
# while number>10:
#     number=number/3 # 180/3= 60  60/3=20  20/3=6
#     count=count+1
# print('Total iteration required : ',count)
#---------------------------

# count=0
# number=1000
# while number>10:
#     number=number/5
#     count=count+1

# print("Total iteration required : ",number)

#--------------------
#while in if else statment

# n=int(input("Enter Number : "))
# while n > 1:
#     if n % 2 == 0:
#         print(n,"is Even Number..")
#     else:
#         print(n,"is Odd Number..")
#     n = n - 1 

# n = int(input("Enter No.-"))
# while n>0:

#     if n % 2 == 0:
#         print(n,"Even")
#     else:
#         print(n,"Odd")
#     n=n-1
#---------------------------
#Else in while loops:
# i=1
# while i < 5:
#     print(i)
#     i +=1

# i=1
# while i<10:
#     print(i)
#     i=i+1

#-----------------
#While Loops Break Statments:


# i=0
# while i<15:
#     print(i)  
#     i+=1



# i=1
# while i<=10:
#     print(i)
#     if i == 5:
#         break
   
#     i+=1

# i=1
# while i<=10:
#     print(i)
#     if i == 5:
#         break
#     i+=1

#------------------
#continue statment while loops
# i=0
# while i < 7:
#     i += 1
#     if i == 4:
#         continue
    
#     print(i)

 # i=0
# while i<10:
#     i +=1
#     if i == 5:
#         continue
#     print(i)
#-----------------------------
#pass Statment
# n = 4
# while n > 0:
#     n = n - 1
#     pass
#------------
# i = 1
# while i < 6:
#     j = 0
#     while j < i:
#         print('*',end=' ')
#         j = j + 1
#     print('')
#     i = i + 1

# i=1
# while i<6:
#     j=0
#     while j<i:
#         print('*',end=' ')
#         j=j+1
#     print('')
#     i=i+1
#-----------------
# a=12
# i=(a // 2)-1
# while i !=0:
#     j = 1
#     while j<=(a-2):
#         print(' ' * i,end='')
#         print('_' * j,end='')
#         print(' ' * i,end='\n')
#         i-=1
#         j+=2

# a=12
# i=(a//2)-1
# while i !=0:
#     j=1
#     while j<=(a-2):
#         print('*' * i,end='')
#         print('-' * j,end='')
#         print('*' * i,end='\n')
#         i-=1
#         j+=2
#-----------------------

# x = int(input("Enter a Number : "))
# for i in range(2,x):
#     if x%i==0:
#         print(" Not Prime ")
#         break
# else:
#     print(" Prime ")

# x=int(input("Enter No : "))
# for i in range(2,x):
#     if x%i==0:
#         print("Not Prime ")
#         break
# else:
#     print("Prime")
#----------------------
# size=6
# for i in range(size):
#     for j in range(1, size -i):
#         print(" ", end=" ")
#     for k in range(0, i + 1):
#         print("*", end=" ")
#     print()


# size=7
# for i in range(size):
#     for j in range(1,size -i):
#         print(" ", end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()
#------------------------------

# n=6
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for k in range(2 * i - 1):
#         print('*', end=' ')
#     print()

# n=7
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(' ',end=' ')
#     for k in range(2*i-1):
#         print('*',end=' ')
#     print()
#---------------------------------

# n=3
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for j in range(2*i+1):
#         print('*',end=' ')
#     print()

# for i in range(n-1):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(2*(n-i-1)-1):
#         print('*',end=' ')
#     print()

#-----------------

# for i in range(1,7):
#     for n in range(1,i+1):
#         print('*',end=" ")
#     print("\n")
#----------------------------------

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# for i in range(n-1):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(2*(n-i-1)-1):
#         print('*',end=' ')
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i-1):
#         print("*",end=" ")
#     print()
#--------------------------
# n=4
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(2*(n-i-1)-1):
#         print("*",end=" ")
#     print()



# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"


# while True:

#     user_input = int(input("Enter a number (enter 0 to exit): "))
    
#     if user_input == 0:
#         break 

#     result = check_even_odd(user_input)
#     print(f"The number {user_input} is {result}.")




# i=5
# while i<10:
#     if i%2==0:
#         print(i,"Even")
#     else:
#         print(i,"odd")
#     i+=1
