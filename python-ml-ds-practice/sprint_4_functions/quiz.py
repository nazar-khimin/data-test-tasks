# def function(item, list = []):
#     list.append(item)
#     print(list, end= " ")
#
# function(1)
# function(2)


# def outer():
#     message = 'Outer string variable'
#     def inner():
#         nonlocal message
#         message = "Inner string variable"
#     inner()
#     return message
#
# print(outer())


# def add_value(a):
#     a.append(3)
#
# b = [1, 2]
# add_value(b)
# print(b)

# def add_value(a):
#     a+=1
#     return a
#
# b=10
# add_value(b)
# print(b)

# def function(item, stuff = 5):
#     stuff +=item
#     print(stuff, end = " ")
#
# function(1)
# function(3)


# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)
#     return a
#
# result = outer(7, 10)
# print(result)

# def function(a):
#     a = [3, 4]
#     print(a, end=" ")
# a = [1, 2]
# function(a)
# print(a)

# def outer():
#     message = 'Outer string variable'
#     def inner():
#         global message
#         message = "Inner string variable"
#     inner()
#     return message
#
# print(outer())

# def outer(x):
#     return lambda : x**2
# print(outer(5))

def many(arg, *args, **kwargs):
    print(args, kwargs)

many(1, 2, 3, b=4, name="First name", job = "First Job")
