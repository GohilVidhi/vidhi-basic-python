# a=50
# b=90
# if a<b:
#     print("b is max")

#-----

# a=60
# b=20
# if a>b:
#     print("a is max")
#     print("my name is fdf")
#--------

# a=51
# b=90
# if a > b:
#     print("a is max")
# else:
#     print("b is max")
#----------
# a=60
# b=5
# if a>b:print("a is max")
#-----------

# a=50
# b=50
# if a>=b:
#     print("a is max")
# elif a<=b:
#     print("b is max")
# elif a==b:
#     print("Both are equal")
# else:
#     print("Invalid number")
#----------
#logical operator

# a=50
# b=10
# c=70
# if a>b and c>a:
#     print("condition are True")
#---------------

# a = input('''1. for pizza \n2. for burger \n3. for panipuri \n4. for dabeli \n5. for dalbati \nEnter number : ''')

# if a == '1':
#     print('pizza')
# elif a == '2':
#     print('burger')
# elif a == '3':
#     print('panipuri')
# elif a == '4':
#     print('dabeli')
# elif a == '5':
#     print('dalbati')
# else:
#     print('Invalid Input')

# a=input('''1. for pizza \n2. for dalbati \n3. for panipuri \n4. maggie \n5. coc \nEnter number :''')

# if a == '1':
#     print('pizza')
# elif a == '2':
#     print('dalbati')
# elif a == '3':
#     print('panipuri')
# elif a == '4':
#     print('maggie')
# else:
#     print('invalid input')
#---------------------------------

# a=200
# b=44
# c=500
# if (a>b) or (c>a):
#     print("Both Condition are True") 

# a=300
# b=55
# c=400

# if a>b and c>a:
#     print(" True")
# else:
#     print("False")
#--------------------

# a = 300
# b = 44
# c = 600
# if (a > b) | (c > a):
#     print("At least one of the conditions is True")

#-------------
# a = int(input("Enter number : "))
# if a>5:
#     print('a is above 5 ')
#     if  a < 20:
#         print('a is between  5 to 20 ')
#     else:
#         print('a is above 20 ')
# else:
#     print('a is below 5 ')

# a = int(input("Enter Number : "))
# if a%2==0:
#     print("a is even")
# else:
#     print("a is odd")
#-------------

# a=20

# if a==21:
#     if a<20:
#         print('True')
#     else:
#         print('True1')
# else:
#     if a<=20:
#         print('True2')
#     else:
#         print('True3')
#     print('False')

# a = int(input("Enter the Year : "))
# if (a%4==0):
#     print(a,' is leap year ')
# else:
#     print(a,'is not leap year ')
#------------------

# x = float(input("Enter the Marks : "))
# if x<=100 and x>90:
#     print("A Grade")
# elif x<=90 and x>80:
#     print("B Grade")
# elif x<=80 and x>=60:
#     print("C Grade")
# elif x<=60 and x>=40:
#     print("D Grade")
# elif x<=40 and x>=0:
#     print("Fail")
# else:
#     ("Invalid")

# a=int(input("Enter number :"))
# b=int(input("Enter number :"))
# c=int(input('''1. press 1 for addition \n2. press 2 for substraction \n3. press 3 for multiplication \n4. press 4 for Division \nChoose number : '''))

# if c == 1:
#     print('Addition is :',a+b)
# elif c == 2:
#     print('substraction is :',a-b)
# elif c == 3:
#     print('multiplication is :',a*b)
# elif c == 4:
#     print('Division is :',a/b)
# else:
#     print('invalid input')

#----------------------

# x = input("enter character :")

# if x == 'A' or x == 'a':
#     print("You have Enter A ")
# elif x == 'B' or x == 'b':
#     print("You have Enter B")
# elif x == 'C' or x =='c':
#     print("You have Enter C")
# else:
#     print("Invalid character")

# a=100
# b=100
# if  a==b:
#     print("True")
# else:
#     print("false")

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
#     for k in range(2*(n-i-1)-1):
#         print("*",end=" ")
#     print() 

print("Welcome to my Distance Converter")

while True:
    choice = input("Would you like to convert miles or km (miles/km): ").lower()
    if choice not in ['miles', 'km']:
        print("Error: Selection must be either 'km' or 'miles'")
        continue

    distance_valid = False
    while not distance_valid:
        distance_input = input(f"How many {choice}?: ")
        if distance_input.isdigit() and int(distance_input) > 0:
            distance = int(distance_input)
            distance_valid = True
        else:
            print("Error: Please enter a valid positive integer")

    if choice == 'miles':
        converted_distance = round(distance * 1.60934, 2)
        unit = 'km'
    else:
        converted_distance = round(distance / 1.60934, 2)
        unit = 'miles'

    print(f"{distance} {choice} would be equivalent to {converted_distance} {unit}")

    another_conversion = input("Would you like to continue? (y/n): ").lower()
    if another_conversion != 'y':
        print("Goodbye")
        break
