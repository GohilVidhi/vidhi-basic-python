
from abc import ABC, abstractmethod

class SBI(ABC):
    @abstractmethod
    def display(self):
        print("sbi class ")
class BOI(SBI):
    def display(self):
        # SBI.display(self)
        print("boi class")
class hdfc(SBI):
    def display(self):
        print("hdfc class")



obj=BOI()
obj1=hdfc()
obj.display()
obj1.display()


# from abc import ABC,abstractmethod

# class RBI(ABC):
#     @abstractmethod
#     def display(self):
#         print("RBI bank")

# class SBI(RBI):
#     def display(self):
#         RBI.display(self)
#         print("SBI bank")

# class BOI():
#     def display(self):
#         RBI.display(self)
#         print("BOI")

# sbi=SBI()
# boi=BOI()

# sbi.display()
# boi.display()
# # abstract base clas 

# from abc import ABC,abstractmethod

# class RBI(ABC):
#     @abstractmethod 
#     def display(self):
#         print("RBI Class" )

# class SBI(RBI):
#     def display(self) :
#         RBI.display(self)
#         print("SBI Class") 

# class BOI(RBI):
#     def display(self) :
#         RBI.display(self)
#         print("BOI Class")        

# # rbi=RBI( 
# sbi=SBI()
# boi=BOI()

# sbi.display()
# boi.display()
# # rbi.display( 

















