print("ATM System")

ch = 'y'
pin = "2208"
amount = 15000

while(ch=='y'):
    print("")
    print("1.ATM Pin")
    print("2.Check Balance")
    print("3.Withdraw")
    print("4.Deposite")
    
    uin = int(input("Enter the choice : "))
    
    if uin==1:
        print("Your pin : ",pin)       
    elif uin==2:
        print("Current balance is : ",amount)
    elif uin==3:
        withdraw = int(input("Enter the amount for withdraw : "))
        if(withdraw < amount):
            amount -= withdraw
            print("Withdraw success..!")
        else:
            print("Your balance is low compare to withdraw amount..!!!")
        
    elif uin ==4:
        deposite = int(input("Enter the deposite amount : "))
        amount += deposite
        print("Deposite success..!")
    else:
        print("Enter valid choice..!!!")
        
    ch = input("Are you want continue..?(y/n)")