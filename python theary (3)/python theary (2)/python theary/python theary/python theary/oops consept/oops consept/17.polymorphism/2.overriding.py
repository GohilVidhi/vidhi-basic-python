
class A:
    def display(self):
        print("This Is Class A")

class B(A):
    def display(self):
        A.display(self)
        print("This Is Class B")

obj=B()
obj.display()








              