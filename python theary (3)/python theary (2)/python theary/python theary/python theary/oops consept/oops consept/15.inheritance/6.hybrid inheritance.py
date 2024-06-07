
class A:
    def displayA(self):
        print("class A")
class B(A):
    def displayB(self):
        print("class B")
class C(A):
    def displayC(self):
        print("class C")
class D(B,A):
    def displayD(self):
        print("class D")
class E(B,A):
    def displayE(self):
        print("class E")
class F(C,A):
    def displayF(self):
        print("class F")        

obj=D()
obj.displayA()
obj.displayB()
obj.displayD()
obj1=E()
obj1.displayA()
obj1.displayB()
obj1.displayE()
obj2=F()
obj2.displayA()
obj2.displayC()
obj2.displayF()
