
class robot():
    def __init__(self):
        self.a=123
        self._b=1234
        self.__c=1235
    def display(self):
        print(self.a)  
        print(self._b)
        print(self.__c)  

# class robot1(robot):
#     def __int__(self):
#         self.a

obj=robot()
print(obj.a)
print(obj._b)
# print(obj.__c)

obj.display()

# a=10
# __a=10
# _a=10

