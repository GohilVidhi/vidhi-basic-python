# sub1=int(input("Enter marks : "))
# sub2=int(input("Enter marks : "))
# sub3=int(input("Enter marks : "))
# sub4=int(input("Enter marks : "))
# sub5=int(input("Enter marks : "))
# sub6=int(input("Enter marks : "))

# total=sub1+sub2+sub3+sub4+sub5+sub6
# print(total)

# pr=total//6
# print(pr,"%")

# if pr>=90 and pr<=100:
#     print("Outstanding Performance")
# elif pr>=80 and pr<=89.99:
#     print("B Grade")
# elif pr>=70 and pr<=79.99:
#     print("C Grade")
# elif pr>=60 and pr<=69.99:
#     print("D Grade")
# else:
#     print("Below 60")



#---------

# amount=int(input("Enter amount : "))

# if amount<50:
#     discount=0
# elif amount<100:
#     discount=0.10    
# elif amount<200:
#     discount=0.15
# else:
#     discount=0.20

# discount=amount*discount
# total=amount-discount

# print("amount : ",amount)
# print("discount : ",discount)
# print("total amount : ",total)


"""
Optimizing Online Shopping Discounts: If Else

Suppose you are working on a program that calculates discounts for an online shopping platform. The platform offers different types of discounts based on the total purchase amount. Your task is to create a program that takes the user's total purchase amount as input and calculates the final amount they need to pay after applying the appropriate discount.

Here's the breakdown of the discount tiers:

If the total purchase amount is less than $50, no discount is applied.
If the total purchase amount is between $50 (inclusive) and $100 (exclusive), a 10% discount is applied.
If the total purchase amount is between $100 (inclusive) and $200 (exclusive), a 15% discount is applied.
If the total purchase amount is $200 or more, a 20% discount is applied.

"""

# amount=int(input("Enter amount : "))

# if amount<50:
#     print("No Discount")
# elif amount>=50 and amount<=100:
#     a=amount/100*10
#     print(amount-a)
# elif amount>=100 and amount<=200:
#     a=amount/100*15
#     print(amount-a)
# else:
#     a=amount/100*20
#     print(amount-a)



# amount=int(input("Enter amount : "))

# if amount<50:
#     print("No Discount")
# elif amount>=50 and amount<=100:
#     a=amount/100*10
#     print(a)
#     print(amount-a)
# elif amount>=100 and amount<=200:
#     a=amount/100*15
#     print(amount-a)
# else:
#     a=amount/100*20
#     print(amount-a)



# age = int(input("Enter age: "))
# show_time = int(input("Enter show time (Enter time by 24 hour formate) : "))



# if age >= 0 and age <= 12:
#     ticket_price = 5
# elif age >= 13 and age <= 17:
#     ticket_price = 7
# elif age >= 18 and age <= 64:
#     # Split the show_time string by the colon character and convert to integers
#     # show_time_parts = show_time.split(":")
#     # hour = int(show_time_parts[0])
#     # minute = int(show_time_parts[1])
    
#     if show_time < 17 :# Matinee show (before 5:00 PM)
#         ticket_price = 10
#     else:  # Evening show (after 5:00 PM)
#         ticket_price = 15
# elif age >= 65:
#     ticket_price = 8
# else:
#     print("ticket_price ")
    
# print("Ticket price is Rs.",ticket_price)
# if ticket_price != "Invalid age":
#     print("Ticket price: ", ticket_price)
# else:   
#     print("Invalid age. Please enter a valid age.")




# print("Welcome to my Distance Converter")

# while True:
#     select = input("Would you like to convert miles or km (miles/km): ")
   
#     if select not in ["miles", "km"]:
#         print("Selection must be either 'km' or 'miles'")
#         continue
       
#     distance = float(input(f"How many {select}?: "))
    
#     if distance <= 0:
#         print("Distance must be greater than zero")
#         continue

#     if select == 'miles':
#         convert = round(distance * 1.60934, 2)
#         print(f"{distance} miles is {convert} km.")
#     elif select == 'km':
#         convert = round(distance * 0.621371, 2)
#         print(f"{distance} km is {convert} miles.")
    
#     a = input("Would you like to continue? Press 'y' to continue or 'n' to exit: ")
#     if a == 'y':
#         continue
#     else:
#         print("Goodbye")
#         break


# num=int(input("Enter Number : "))

# for i in range(num<=0):
#     if i<=num:
        
#         print(i)





# num = int(input("Enter Number: "))

# for i in range(1,1000000000000000000000):
#     if len(str(i)) == num:    
#         print(i)

# name="my name is vidhiii"
# name1=name.split()
# n1=name=[0]
# n2=name[-1]
# # count=0
# if n1==n2:
#     count=n1.count()
#     print("sc")

# else:
#     print("rb")
  
  
# name="myvidhi" 

# name1=name.split()
# l1=name1[0]
# l2=name1[-1]

# if len(l1)>0 and len(l2)>0:
    
#     print(len(l1))
#     print(len(l2))
# elif name1==0:
#     print("Invalid") 
  
# l="python django"
# print(l[1::4])
  