# # List comprehensions
# l=[i for i in range(1,11) if i%2==0]
# print(l)


# # tuple comprehensions
# l=(i for i in range (1,11))
# print(tuple(l))

# # set comprehensions
# l={i for i in range(1,16)}
# print(set(l))

# # Dictionary comprehensions
# l = {i:i*2 for i in range(1,7) if i%2==0}
# print(l)

# =================================================================================
# b=[i for i in range(1,40,2)]
# print(b)


# state=['maharashtra','gujrat','rajasthan']
# city=['pune','anand','jodhpur']

# dict={key:value for (key,value) in zip(state,city)}
# print(dict)

# x = {1,2,3,4,5,6,7,8}

# s = {v**2 for v in x}
# print(s)

x={1,2,3,4,5,6,7,8}
s={v**2 for v in x}
print(s)






















