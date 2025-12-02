'''import functools
n=int(input('Enter:'))
x=lambda n: [i for i in range(1,n+1) if i%2==0]
print(x(n))
def sum (x,y):
    return x+y
res=functools.reduce(sum,l)
print(res)'''

# from functools import reduce 
# l=eval(input("Enter:"))
# def max (x,y):
#     if  x>y:
#         return x
#     else:
#         return y
# res=reduce(max,l)
# print(res)

from functools import reduce
l=eval(input("Enter:"))
def sqr (x,y):
    return x+y**2
res=reduce(sqr,l,0) # Alwyas use ineclization from 0 or use any number.
print(res)