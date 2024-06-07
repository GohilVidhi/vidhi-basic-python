
# class salary:
#     def __init__(self,currentsalary,bonus):
#         self.currentsalary=currentsalary
#         self.bonus=bonus

#     def annualsalary(self):
#         return self.currentsalary*12 + self.bonus

# class employee:
#     def __init__(self,name,depart,sal):
#         self.name=name
#         self.depart=depart
#         self.main_salary=sal

#     def total_sal(self):
#         return self.main_salary.annualsalary()

# sal=salary(10000,2000)
# emp=employee("nilesh","IT",sal)
# print(emp.total_sal())  

class salary:
    def __init__(self,currentsalary,bonus):
        self.currentsalary=currentsalary
        self.bonus=bonus
    def annualsalary(self):
        return self.currentsalary*12  + self.bonus
    def nil(self):
        print("nilesh")    

class employee:
    def __init__(self,name,depart,sal):
        self.name=name 
        self.depart=depart
        self.main_salary=sal 

    def total_Sal(self):                                                                              
        return self.main_salary.annualsalary()                                                                              
    def display(self):
        return self.main_salary.nil()                                                                                  
    
sal=salary(10000,2000)                                                                              
emp=employee("nilesh","it",sal)                                                                              
emp.display()                                                                              
print(emp.total_Sal())                                                                              