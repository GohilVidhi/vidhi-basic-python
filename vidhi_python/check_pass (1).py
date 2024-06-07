password = input("Enter the password : ")
special_lst = ["$","@","&","%","#","!","*","?","<",">","_","+","-","^"]
ch_sp = False
upper_alfabet = False
num = False

if (len(password)>=8):
    for i in password:
        if i in special_lst:
            ch_sp = True
        if i.isupper():
            upper_alfabet = True
        if i.isnumeric():
            num = True
        
if(ch_sp == True and upper_alfabet == True and num == True):
    print("Password valid..!")     
else:
    print("Invalid Password..!")