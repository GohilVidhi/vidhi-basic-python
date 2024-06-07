
class A:
    def displayA(self):
        print("class A")
class B(A):
    def displayB(self):
        print("class B")
class C(A):
    def displayC(self):
        print("class C")
class D(A):
    def displayB(self):
        print("class B")
class E(A):
    def displayC(self):
        print("class C")


obj=B()
obj.displayA()
obj.displayB()
obj1=C()
obj1.displayA()
obj1.displayC()








