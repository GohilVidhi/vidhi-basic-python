
class A:
    def displayA(self):
        print("class A")
class B:
    def displayB(self):
        print("class B")
class C(A,B):
    def displayC(self):
        print("class C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()  
obj.      