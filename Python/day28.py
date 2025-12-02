# map()
# filter()
# reduce()

# map()
'''
l1=eval(input("Enter:"))
def add(x,y,z):
    return x**2

res=map(add,l1)
print(res)
print(tuple(res))'''


# For square root,with map()
'''
l1=eval(input("Enter:"))
def add(x):
    return x**2

res=map(add,l1)
print(res)
print(tuple(res))'''

#   i don't know.
'''
l1=eval(input("Enter:"))
def add(x):
    return x**0.5

res=map(add,l1)
print(res)
print(tuple(res))'''

# find odd number with filter
l1=eval(input("Enter:"))
def greater(x):
    if x % 2 :
        return x
    
res=filter(greater,l1)
print(list(res))