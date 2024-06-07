
"""
polymorphism:
============

==> poly means many and morphism menas forms

==> one named method has different different forms its called polymorphism

==> there are 2 types of polymorphism

1 : method overloading :
    =================

    ==> one class can contain same name method with different signature(parameters)

    ==> note : in python this is not supported
        ====

2 : method overriding : 
    ====== ==========

    ==> two class have same name method with same parameters

"""

# class nilesh():
#     def jaydip(self):
#         print("my name is jadav jaydip ramjibhai")

# class mital(nilesh):
#     def jaydip(self) :
#         nilesh.jaydip(self)
#         print("my name is jadav urvashi ramjibhai")

# obj1=mital()               
# obj1.jaydip()

# class nilesh:
#     def display(self):
#         print("nilesh")

# class jaydip(nilesh):
#     def display(self):
#         nilesh.display(self)
#         print("jaydip")        


# j=jaydip()

# j.display()
# j.display()


class student1:
    def display():
        print("student 1 display")

class student2:
    def display():
        print("student 2 display")        

class student3(student1,student2):
    def display():
        student1.display()
        student2.display()
        print("student 3 dispalay")

# s1=student1
s3=student3

# s1.display()
s3.display()
# s2.display()















