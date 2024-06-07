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

