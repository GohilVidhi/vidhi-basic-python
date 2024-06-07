
"""
Encapsulation:
=============

==> one class can contain different different properties at single location it called encpsulation.

==> e.g
    ===

class <classname>
    
    element
    method


"""

class A:
    def student(self):
        self.name="um"
        self.age=23
        self.subject="python"

    def display(self):
        print(self.name)
        print(self.age)
        print(self.subject)

a=A() 

a.student()
a.display()








































