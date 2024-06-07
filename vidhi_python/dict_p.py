#Dictionary

# a={'a':123,'b':23, 44:'xyz'}
# print(a)

# a = {1:[1,2,3],'b':(1,2,3),'c':{1,2,3}}
# print(a)
#-----

# a={'vidhi':{'height':187,'weight':70},'dp':{'height':160, 'weight':86}}
# print(a['dp'])

# dict={'abc':{'height':160,'weight':80},'xyz':{'height':166,'weight':80}}
# print(dict['xyz']['height'])
#--------------
# d={'a':123,'b':33,44:44}
# print(d['a'])
# print(d['b'])
# d[46]='Ram'
# d[33]='abc'
# print(d)




# x={'a':111,'b':333,'c':444}
# print(x['a'])
# print(x['b'])
# print(x['c'])
# x['d']='555'
# x['e']='666'
# print(x)

a = {'vidhi':{'height':186,'weight':57},'ram':{'height':167,'weight':90}}
# print(a['vidhi']['weight'])
# a['vidhi']['height']=199
a['shyam']={'height':169,'weight':80}
# a['reem']={'height':170,'weight':99}
# a['ved']={'height':166,'weight':88}
# a['zen']={'height':177,'weight':90}
print(a)



#===================================================
# a = {'a1':111,'b1':222,'c1':333}
# print(a.keys())
# print(a.items())
# print(a.values())

# a.update({'d1':444})
# print(a)

# a.popitem()
# print(a)

# a.clear()
# print(a)
#==================================================

# name = {'vidhi','abc','www'}
# age = 22

# d = dict.fromkeys(name,age)
# print(dict(d))
#----
# d=dict.fromkeys(name,age)
# print(d)
# name = {'vidhi','gohil','abc'}
# age = {22,23,11}
# d = dict.fromkeys(name,age)
# print(d)
#-----------------

# d1={
#     'name':"vidhi",
#     'age':23,
#     "subject":"python"
# }

# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d1.items())

# d1.update({'std':11})
# d1.update({'std':'dhdd'})
# print(d1)

#===================================

# Print the value of key ‘history’ from the below dict
# sampledict={
#     "class":{
#         "student":{
#             "Name":"Vidhi",
#             "Marks":{
#                 "Maths":77,
#                 "History":80
#             }
#         }
#     }
# }
# print(sampledict["class"]["student"]["Marks"]["History"])

# sampledict = {
#     "class":{
#         "student":{
#             "name":"vidhi",
#             "marks":{
#                 "maths":77,
#                 "history":90,
#                 "sci":70
#             }
#         }
#     }
# }
# print(sampledict["class"]["student"]["marks"])

#===============================================

# Check if a value exists in a dictionary

# dict = {'a':10,'b':20,'c':30,'d':40}

# if 10 in dict.values():
#     print("Present in dict")
# else:
#     print("Not present in dict")

#=============================

#Change value of a key in a nested dictionary
# sample = {
#           'employee1':{'name':'vidhi','age':23,'salary':10000},
#           'employee2':{'name':'dp','age':24,'salary':20000},
#           'employee3':{'name':'ddd','age':25,'salary':30000}
#            }

# sample['employee1']['salary']=21000
# print(sample)
#============================================

# sample = {
#     'sub1':{'name':'English','time':'10pm'},
#     'sub2':{'name':'Hindi','time':'11pm'},
#     'sub3':{'name':'Physics','time':'12pm'},
#     'sub4':{'name':'Maths','time':'01pm'}
# }
# sample['sub1']['name']='Gujrati'
# print(sample)
#============================================

# numbers = [12, 75, 150, 180, -145, 525, 50]

# for l in [2,3,-1]:
#     print(numbers[l])
#============================================

#Write a program to print the cube of all numbers from 1 to a given number

# n = int(input("Enter a number: "))
# cubes = []

# for i in range(1, n+1):
#     cubes.append(i**3)

# print("The cubes of numbers from 1 to", n, "are:")
# for cube in cubes:
#     print(cube)
#-------------------------------------------------
# n = int(input("Enter Number : "))
# cubes = []
# for i in range(1, n+1):
#     cubes.append(i**3)

# print("the Cubes of 1 to " , n , "are : ")
# for cube in cubes:
#     print(cube)
#=============================================

#total sum of some marks : 

# marks = {'a':90 , 'b':88 , 'c':98 , 'd':99 , 'e':89}
# total = sum(marks.values())
# print(total)

# marks = {'x':80 , 'y':99 , 'z':98 , 'q':77}
# total = sum(marks.values())
# print("The Total Marks Of Sum is = " , total)
# lower_marks = min(marks.values())
# print("Lower marks is : ", lower_marks)
# high_marks = max(marks.values())
# print("High marks is : ", high_marks)




# d1={"name":"Vidhi","age":23,"city":"Ahmedabad"}

# print(d1)
# print(type(d1))

# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1.update({"abc":2})

# print(d1)

# d1.pop("age")
# print(d1)

# del d1
# print(d1)

# d1.clear()
# print(d1)

# for i in d1.keys():
#     print(i)

# for i in d1.values():
#     print(i)



# for i in d1.items():
#     print(i)


# d1= {
#     1:{
#         "name":"vidhi",
#         "age":{
#             "v":22,
#             "a":21,
#         }

#     },
#     2:{"name":"abc",
#        "subject":{
           
#        "sub1":"python",
#        "sub2":"java"}

#     }
# }
# print(d1[1]["age"]["a"])
# print(d1[2]["subject"]["sub2"])
# a = { 'Divyesh':{'hight' : 168, 'weight':58} , 'Sahil':{'hight' : 195, 'weight':58}}
# print(a['Sahil']["hight"])

# a={'1':11,'1':11,'2':22}
# print(a)




# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020,
#   "year": 1964,
# }
# print(thisdict)