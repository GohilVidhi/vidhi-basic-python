

# l = lambda a,b:print(a+b)
# l(20,30)

# l = lambda a,b:print(a-b)
# l(50,30)

# l = lambda a,b:print(a*b)
# l(60,10)

# l = lambda a,b:print(a/b)
# l(10,2)

# l=lambda a,b:print(a+b)
# l(100,200)

#=================
# a=lambda b,c,d,e:(b+c+d+e)
# print(a(3,3,4,3))

# a=lambda x,y,z,w:(x-y-z-w)
# print(a(3,4,3,2))

# a=lambda o,p,q,r:(o*p*q*r)
# print(a(2,3,2,2))

# l=lambda a,b,c,d:(a-b/c-d)
# print(40/30/40/10)


# l = lambda a:f"Even number {a}" if a%2==0 else f"Odd Number {a}"
# print(l(2232))

# l=lambda a:f"Even number {a}" if a%2==0 else f"Odd number {a}"
# print(l(22))


# ==========================================
#           Map Function

# l=[1,2,3,4,5,6,7,8,9,10]
# def abc(l):
#     if l%2==0:
#         return l*l
    
# a=map(abc,l)
# print(list(a))

# l=[1,2,3,4,5,6]
# def abc(l):
#     if l%2==0:
#         return l*l
# a=map(abc,l)
# print(list(a))


# a = [1,2,3,4,5,6,7,8]

# odd = list(map(lambda x : x if x%2 != 0 else 'h',a))

# print(odd)

# a = [1,2,3,4,5,6,7,8]

# odd = list(filter(lambda x : x if x%2 != 0 else 'h',a))

# print(odd)
#======
# a = [1,2,3,4,5,6]

# b = list(map(lambda x :x*2,a))
# print(b)

# a = [1,2,3,4,5,6,7,8]

# odd = list(filter(lambda x : x if x%2!=0 else '',a))

# print(odd)

# a=[1,2,3,4,5,6,7,8]
# odd=list(filter(lambda x:x if x%2!=0 else '',a))
# print(odd)


#===========================================
# l=[1,2,3,4,5,6]
# def fun(l):
#     if l%2==0:
#         return l*l

# a=map(fun,l)
# print(list(a))
#===========================================

# l=[1,2,3,4,5,6,7,8]
# def abc(l):
#     return l*l
# a=map(abc,l)
# print(list(a))
# ===========================================

# l=[1,2,3,4,5,6]
# def a(l):
#     return l*l
# b=map(a,l)
# print(list(b))

# l1=[1,2,3,4,5,6,7,8,9,10]
# def multi(l1):
#     return l1


# a=map(multi,l1)

# print(list(a))

# ===========================================

#           Filter Function

# l1=[1,2,3,4,5,6,7,8,9,10]
# def abc(l1):
#     if l1%2==0:
#         return l1

# v=filter(abc,l1)
# print(list(v))

# l1=[1,2,3,4,5,6,7,8]
# def abc(l1):
#     if l1%2==0:
#         return l1
# b=filter(abc,l1)
# print(list(b))



# a = lambda a:[print(i)for i in range(1,a+1)]
# a(21)

# a=lambda a:[print(i)for i in range(1,a+1)]
# a(20)
#============================================



# def abc():
#     print("my name is vidhi")

# def abcd():
#     print("hello")


# abcd()