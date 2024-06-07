# my_object=["vidhi","gohil","niki"]
# my_object="vidhi"

# iter_obj=iter(my_object)
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))





my_object=[1,2,3,4,5,6,7]

# for i in my_object:
    
#     print(i)



my_obj=[1,22,34,5]
iter_obj=iter(my_obj)

while True:
    try:
        element=next(iter_obj)
        print(element)
    except StopIteration:
            break





# class example:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=2
#         return x
    
# itr=example()
# my_iter=iter(itr)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))




# class inifinite:
#     def __iter__(self):
#         self.num=1
#         return self
    
#     def __next__(self):
#         num=self.num
#         self.num+=5
#         return num
        
# myclass=inifinite()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))





