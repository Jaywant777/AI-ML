# OOPS

'''
class student:
    ''This is class'' #  use triple  for working.
    pass
# print(dir(student))
print(student.__doc__) # __doc__ is a variable.'''



# class student:
#     '''This is called class'''
#     x=10
#     y=20
#     def show():
#         print("hello")
# # print(student.__dict__)
# # print(dir(student))
# print(id(student))
# obj=student
# print(id(obj))
# obj2=student
# obj3=student()
# print(id(obj2),id(obj3))



class student:
    def __init__(self):
        print("Constuctor called")
obj1=student
print(id(obj1),id(student))

obj2=student()
print(id(obj2),id(student))