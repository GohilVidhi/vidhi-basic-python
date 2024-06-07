

# for i in range(0,12):
#     print(i)

# for i in range(1,11):
#     if i==7:
#         break
#     print(i)

# for i in range(1,11):
# if i==7:
#     pass
# print(i)
# pass

# for i in range(1,100):
#     if i%2==0:
#         print("evan number : ",i)
#     else:

#         print("odd number : ",i)
# for i in range(1,11):
#     pass


# for i in range(1,3):
#     for n in range(1,6):
#         print("sagar",end=" ")
#     print("\n")

# l1=[1,2,3,4,5,6]

# for i in l1:
#     print(i)

# i=10

# while i>=-11:
#     print(i)
#     i=i-1

# ===============================
# i=10

# if i%2==0:
#     print("evan number ")
# else:
#     print("odd number  ")


# i=input("Enter number :")

# if i%2==0:
#     print("evan number ")
# else:
#     print("odd number  ")

# ===================================


# def fun():
#     print("def")

# fun()


# def addition():
#     a=int(input("Enter A First Number : "))
#     b=int(input("Enter A second Number : "))
#     print(a+b)
# def sub():
#     a=int(input("Enter A First Number : "))
#     b=int(input("Enter A second Number : "))
#     print(a-b)
# def multi():
#     a=int(input("Enter A First Number : "))
#     b=int(input("Enter A second Number : "))
#     print(a*b)
# def div():
#     a=int(input("Enter A First Number : "))
#     b=int(input("Enter A second Number : "))
#     print(a/b)

# addition()
# sub()
# multi()
# div()
# num=int(input("Enter A Number : "))

# if num==1:
#     print("Addition")
#     addition()
# elif num==2:
#     print("sub")
#     sub()
# elif num==3:
#     print("multi")
#     multi()
# elif  num==4:
#     print("div")
#     div()
# else:
#     print("Invalid Number")


# def if_else():
#     for i in range(1,11):
#         if i%2==0:
#            print("Evan Number",i)
#         else:
#             print("Odd Number",i)
# def for_loop():
#     for i in range(1,11):
#         print(i)

# # if_else()
# for_loop()


# l1=[1,2,3,43,1,2,3,4,1,1,1,1,2]
# l2=[]


# for i in l1:
#     if i not in l2:
#         l2.append(i)
# print(l2)


# t1=(1,2,3,4,5,6,7,1,1,1,1,1,1,1,1)

# print(type(t1))

# print(list(t1))

# print(t1.count(1))

# print(t1.index(1))


# print(len(t1))
# print(sum(t1))
# print(max(t1))
# print(min(t1))


# t1=()
# ([1,2,[3,4],5,6,5,4,[3,2,1],0],)

# t2=list(t1)

# t2.extend([[1,2,[3,4],5,6,5,4,[3,2,1],0]],)


# print(t2)


# s1={1,2,3,4,1,2,3,4,5}


# print(type(s1))

# print(s1)

# l1=[1,2,3,4,5,5,4,3,2,1,0]

# l2=set(l1)

# print(list(l2))


# s1={1,2,3,4,1,2,3,4,5}

# print(len(s1))
# print(sum(s1))
# print(min(s1))
# print(max(s1))

# s1={1,6,2,3,4,5}

# s1.add(6)
# s1.add(7)

# l2=list(s1)
# l2.sort(reverse=True)
# # s1.pop()

# s1.remove(5)

# s1.clear()
# del s1
# s1=10
# l3=set(l2)
# print(l3)

# l1="abcdefghijklmnopqrstuvwxyzaaaaaa"

# a=l1.count("a")
# b=l1.count("e")
# c=l1.count("i")
# d=l1.count("o")
# e=l1.count("u")

# print(a+b+c+d+e)
# my_set = {1, 2, 3, 4, 5}
# s1=set()
# reversed_list = list(my_set)[::-1]
# reversed_set = set(reversed_list)

# print()


# s1={1,2,3,4,5,6}

# s2=list(s1)[::-1]
# s3=set(s2)

# print(s3)

# name="jadav niles"
# count=0   


# for i in name:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         count+=1

# print(count)


# t1=(1,)

# print(type(t1))


# name="abcdefghijklmnopqr"
#

# a e i o u

# l1=()
# l2=list(l1)
# for i in name:
#     if i=="a" or i=="e":

#         l2.append(i)

# print(tuple(l2))


# name="abcdefghijklmnopqrstuvwxyz"

# count=0
# count1=0

# for i in name:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         count+=1
#     else:
#         count1+=1
# print(count)
# print(count1)

# name="abcdefghijklmnopqrstuvwxyz"

# output=("a","e","i","o","u")

# l1=()
# l2=list(l1)
# l3=()
# l4=list(l3)
# l2=[]
# l4=[]
# for i in name:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         l2.append(i)
#     else:
#         l4.append(i)
# print(tuple(l2))
# print(tuple(l4))


# l1=["nil",""," ","nilu"]
# c=0
# for i in l1:
#     if i in " ":
#         c+=1

# print(c)

# d1 = {
#                 'emp1': {'name': 'Jhon', 'salary': 7500},
#                 'emp2': {'name': 'Emma', 'salary': 8000},
#                 'emp3': {'name': 'Brad', 'salary': 500}
#             }


# d1['emp1']['name']="nilesh"
# print(d1)


# d1={
#     'name':"nilesh",
#     "age":24
# }


# # for i in d1.keys():
# #     if i in "age":
# #         print(i)

# if 'name1' in d1.keys():
#     print("yes")

# else:
#     print("no")


# l1=[12,3,4,4,5,4,4,4,4,5]

# print(l1.count(4))


# l1=["python"," "," ","java"," "]

# c=0
# for i in l1:
#     if i in " ":
#         c+=1
# print(c)
"""
75
150
145
"""


# l1=[12, 75, 150, 180, 145, 525, 50]

# for i in l1:
#     if i > 500:
#         break
#     elif i > 150:
#         continue
#     elif i%5==0:
#         print(i)


# d1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# a=dict()

# for i in d1:
#     a[i]=i*i

# print(a)

# marks={"m1":78 , "m2":89 , "m3":64 , "m4":35 , "m5":71}

# m=marks.values()

# print(max(m))
# print(min(m))
# print(sum(m))

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# n=numbers_y[0]
# m=numbers_y[-1]

# if n==m:
#     print("True")
# # else:
# #     print("Flase")

# a=2
# for i in range(1,5):
#     print(f"{i}=={i**a}")


# t1=[1,2,3,4,5,6,7,8,9,10]
# t2=[11,12,13,14,15,16,17,18,19,20]

# t1[0],t1[-1]=t2[0],t2[-1]
# print(t1)
# t2[0],t2[-1]=t1[0],t1[-1]

# print(t2)

# for i in range(1,6):
#     for n in range(1,i+1):
#         print(i,end=" ")
#     print()

# fectrorial number
# n=5
# for i in range(1,n):
#     n=n*i

# print(n)

# num=121
# temp=num
# rev=0

# while num>0:
#     v=num%10
#     rev=rev*10+v
#     num=num//10

# if temp==rev:
#     print("p")
# else:
#     print("np")

# num=121

# num=str(num)

# num1=num[::-1]
# print(num1)
# if  num==num1:
#     print("p")
# else:
#     print("np")

# num=0
# num1=1

# for i in range(1,11):bbbbb
#     print(num,end=" ")
#     f=num+num1
#     num=num1
#     num1=f


# num=153

# n=len(str(num))
# sum=0
# temp=num

# while temp>0:
#     d=temp%10
#     sum=sum+d**n
#     temp=temp//10

# if num==sum:
#     print("a")
# else:
#     print("na")


# n=5
# d=dict()

# for i in range(1,n+1):
#     d[i]=i*i
# print(d)


# n=int(input("Enter A Number : "))
# d=dict()

# for i in range(1,n+1):
#     d[i]=i*i
# print(d)


# l1=["python"," ","  ","java","django","  ","  "]
# s1=0
# s2=0
# for i in l1:
#     if " " in i:
#         if i==" ":
#             s1+=1
#         elif i=="  ":
#             s2+=1
# print(s1)
# print(s2)


# =============================function===============================

# def fun():
#     print("hello python")

# fun()


# def fun():
#     for i in range(1,11):
#         if i%2==0:
#             # i-=1
#             # print(i)
#             # pass
#             continue
#         else:
#             print(i)


# fun()


# def student():
#     name="python"
#     print(name)

# def student1():
#     print("java")

# def student2():
#     print("php")

# def student3():

#     print("django")

# student()

# ===============================
# t1=((1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1))

# a=t1[0][0]+t1[1][0]+t1[2][0]
# b=t1[0][1]+t1[1][1]+t1[2][1]
# c=t1[0][2]+t1[1][2]+t1[2][2]
# d=t1[0][3]+t1[1][3]+t1[2][3]

# print(tuple([a,b,c,d]))

# l1=[]

# l2=len(l1)
# if l2<=0:
#     print("Empty list")
# else:
#     print("not ")

# l1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# # [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

# a=l1[::3]
# b=l1[1::3]
# c=l1[2::3]
# print(list([a,b,c]))


# num=[1,2,3,4]
# num.sort(reverse=True)
# for i in num:
#     print(f"[emp{i}]",end= ",")

# l1=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6,1, 8, 9, 4, 4]
# l2=[]
# for i in l1:
#     if i==0:
#         a=l2.append(i)
#     elif i==1:
#         b=l2.append(i)
#     elif i==3:
#         c=l2.append(i)
# l2.extend([a,b,c])

# print(l2)


# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}

# for d in dic1,dic2,dic3:
#     dic4.update(d)

# print(dic4)


# num = [[11111,22,31], [4443444,5,6], [10,112222221,12], [7777,8,9]]

# a=num[0][0]+num[0][1]+num[0][2]
# b=num[1][0]+num[1][1]+num[1][2]
# c=num[2][0]+num[2][1]+num[2][2]
# d=num[3][0]+num[3][1]+num[3][2]

# if a>b and a>c and a>d:
#     print(num[0])
# elif b>a and b>c and a>d:
#     print(num[1])
# elif c>a and c>b and c>d:
#     print(num[2])
# else:
#     print(num[3])


# ==============================================


# l1=[1,2,3,4,1,2,3,4,5,6,7]
# l2=[]
# l3=[]
# print(len(l1))
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



# num=370

# sum=0
# temp=num

# while temp>0:
#     d=temp%10
#     sum=sum+d**3
#     temp=temp//10

# if num==sum:
#     print("a")
# else:
#     print("np")


# num = (1, 2, 3, 4, 5, 6, 7)

# def fun(num):
#     return num+num+num

# a=map(fun,num)

# print(list(a))


# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# nums3 = [7, 8, 9]


# def fun(num1,num2,num3):
#     return num1+num2+num3

# a=map(fun,nums1,nums2,nums3)
# print(tuple(a))


# color = ['Red', 'Blue', 'Black', 'White', 'Pink']


# a=map(list,color)

# print(list(a))

# num = [10.0,20.0, 30.0, 40.0, 50.9, 60.8, 70.7, 80.6, 90.5, 100.4]

# a=map(int,num)

# print(list(a))


# num = [10.0,20.0, 30.0, 40.0, 50.9, 60.8, 70.7, 80.6, 90.5, 100.4]
# num1=[]

# for i in num:
#     n=int(i)
#     num1.append(n)
# print(num1)

# print(int(num[0]))

# def fun():
#     print("python")

# def fun1():
#     print("django")


# try:
#     a=int(input("E"))

# except NameError:
#     print("yes")

# except ZeroDivisionError:
#     print("yes1")

# except TypeError:
#     print("yes2")

# except ValueError:
#     print("yes3")


# name='THe quick Brow Fox'

# u=0
# l=0
# for i in name:
#     if i.isupper():
#         u+=1

#     else:
#         l+=1


# print(u)
# print(l)

# try:
#     a=10+'n'
# except ValueError:
#     print("valueerror")
# except ZeroDivisionError:
#     print("zero")
# except TypeError:
#     print("type")


# a='1212'

# a1=a[::-1]


# if a==a1:
#     print("p")
# else:
#     print("np")
# ==================================ATM TASK===============================
l=True
pin=123
b=100

while l:
    num=int(input("Enter A Number \n(1 for pin)\n(2 for balance check)\n(3 for add amount)\n(4 for withdrow)  : "))
    if num==1:
        pin1=int(input("Enter A Pin : "))
        pin=pin1
        print(pin)
    elif num==2:
        pin1=int(input("Enter A Pin : "))
        if pin==pin1:
            print("your balance is ",b)
            print(b)
        else:
            print("Envalid Pin")
    elif num==3:
        pin1=int(input("Enter A Pin : "))
        if pin==pin1:
            amount=int(input("Enter A Amount : "))
            b=b+amount
            print("your balance is ",b)
        else:
            print("Envalid Pin")
    elif num==4:
        pin1=int(input("Enter A Pin : "))
        if pin==pin1:
            amount=int(input("Enter A Amount Withdrow : "))
            b=b-amount
            print("your balance is ",b)
        else:
            print("Envalid Pin")
    i=input("Enter A 'y' for continue and 'n' for break :")
    if i=='y':
        l=True
    elif i=='n':
        l=False
    else:
        l=False



# class ATM:
#     def __init__(self, pin, balance=100):
#         self.pin = pin
#         self.balance = balance

#     def check_balance(self):
#         return f"Your balance is ${self.balance}"

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"${amount} has been deposited. Your new balance is ${self.balance}"
#         else:
#             return "Invalid deposit amount."

#     def withdraw(self, amount):
#         if amount > 0:
#             if amount <= self.balance:
#                 self.balance -= amount
#                 return f"${amount} has been withdrawn. Your new balance is ${self.balance}"
#             else:
#                 return "Insufficient funds. Withdrawal denied."
#         else:
#             return "Invalid withdrawal amount."

# def main():
#     pin = int(input("Set your PIN: "))
#     atm = ATM(pin)

#     for _ in range(3):
#         entered_pin = int(input("Enter your PIN: "))
#         if entered_pin == atm.pin:
#             print("PIN accepted. Welcome to the ATM.")
#             break
#         else:
#             print("Incorrect PIN. Please try again.")
#     else:
#         print("Too many incorrect attempts. Exiting.")
#         return

#     while True:
#         print("\nATM Menu:")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         try:
#             choice = int(input("Enter your choice (1-4): "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == 1:
#             print(atm.check_balance())
#         elif choice == 2:
#             try:
#                 amount = float(input("Enter the amount to deposit: $"))
#             except ValueError:
#                 print("Invalid input. Please enter a valid amount.")
#                 continue
#             print(atm.deposit(amount))
#         elif choice == 3:
#             try:
#                 amount = float(input("Enter the amount to withdraw: $"))
#             except ValueError:
#                 print("Invalid input. Please enter a valid amount.")
#                 continue
#             print(atm.withdraw(amount))
#         elif choice == 4:
#             print("Thank you for using the ATM. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")

# if __name__ == "__main__":
#     main()

# ===========================que================


# menu=[["what is  80*3"],["what is 800-450"],["what is 8*3/2"],["what is 46/2"],["what is 60*3/2"],
# ["what is 80/2*5"],["what is 100*2-100"],["what is 50+100*4"],["what is 100-100/2"],["what is 2*5+50"]]
# print(menu)

# marks=0
# r=0
# w=0
# i=1

# l=True
# while l:
#     while i<=3:
#         ch=int(input("Enter A Number : "))
#         if i==3:
#             l=False
#             print("Right Answer is : ",r)
#             print("Wrong Answer is : ",w)
#             print("Your Total Marks : ",marks)
#         elif ch==1:
#             print("     Question 1",menu[0])
#             l1={"A":240,"B":340,"C":180}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["A"]==ans:
#                 marks+=10
#                 r+=1
#                 print("R")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 i+=1
#         elif ch==2:
#             print("     Question 2",menu[1])
#             l1={"A":340,"B":350,"C":400}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["B"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1

#         elif ch==3:
#             print("     Question 3",menu[2])
#             l1={"A":14,"B":15,"C":12}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["C"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
                 
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1

#         elif ch==4:
#             print("     Question 4",menu[3])
#             l1={"A":32,"B":15,"C":23}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["C"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#         elif ch==5:
#             print("     Question 5",menu[4])
#             l1={"A":90,"B":180,"C":95}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["A"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#         elif ch==6:
#             print("     Question 6",menu[5])
#             l1={"A":150,"B":100,"C":230}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["B"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#         elif ch==7:
#             print("     Question 7",menu[6])
#             l1={"A":100,"B":150,"C":200}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["A"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#         elif ch==8:
#             print("     Question 8",menu[7])
#             l1={"A":0,"B":10,"C":20}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["B"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#         elif ch==9:
#             print("     Question 9",menu[8])
#             l1={"A":10,"B":160,"C":60}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["C"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#         elif ch==10:
#             print("     Question 10",menu[9])
#             l1={"A":80,"B":160,"C":60}
#             print(l1)
#             ans=int(input("Enter A Answer : "))
#             if l1["A"]==ans:
#                 marks+=10
#                 r+=1
#                 print("Right Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1
#             else:
#                 marks-=10
#                 w+=1
#                 print("Wrong Answer")
#                 print("Your Marks IS : ",marks)
#                 i+=1      
#         else:
#             print("Envalid Number ")            

#         cho=input("Enter A Y : ")
#         if cho=="y":
#             l=True
#         else:
#             l=False
#             print("Right Answer is : ",r)
#             print("Wrong Answer is : ",w)
#             print("Your Total Marks : ",marks)
          



# l1=["python"," "," ","django","php","java"," ","nilesh"]
# l2=[]


# for i in l1:
#     if i==" ":
#         pass
#     else:
#         l2.append(i)

# print(l2)

"""Write a Python program that iterates the integers from 1 to 10. For multiples of 
three print "Fizz" instead of the number and for multiples of five print "Buzz". 
For numbers that are multiples of three and five, print "FizzBuzz"."""


# for i in range(1,11):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")    
#     elif i%5==0:
#         print("Buzz")    
#     else:
#         print(i)   
# 



# import random
# computer=random.randint(1,100)
# s=True
# while s:
#     for i in range(1,11):
#         num=int(input("Enter A Number : " ))
#         if num>computer:
#             print("less the number ")
#         elif num<computer:
#             print("gretar the number")
#         else:
#             print("win")
#             break
#         s=False    


# s="google.com"
# l1=[]

# a=s.count("g")
# b=s.count("o")
# c=s.count("l")
# d=s.count("e")    
# e=s.count(".")    
# f=s.count("c")    
# g=s.count("m")

# l1.extend([a,b,c,d,e,f,g])
# print(l1)


# s="google.com"
# l1={}


# for i in s:
#     if i in l1:
#         l1[i]+=1
#     else:
#         l1[i]=1

# print(l1)
# ======================


# a="restart"

# char=a[0]
# char1=a[-2]              # r
# a=a.replace(char,"$")  # $esta$t
# a=char+a[1:]+char1           # resta$t

# print(a)


# for i in range(6,0,-1):
#     for n in range(1,i+1):
#         print("*",end=" ")
#     print("\n")    



# for i in range(1,6):
#     for n in range(1,i+1):
#         print(n,end=" ")
#     print("\n")    

# ======================

# num = (1, 2, 3, 4, 5, 6, 7)

# num=list(num)

# num.reverse()

# print(num)


# def fun(num):
#     return num*num


# a=map(fun,num)

# print(list(a))

# ======================


# name = "hello, and welcome to my world."

# print(name)


# def fun():
#     print("hello python")

# def fun1():
#     print("hello")    
    
#===============================












