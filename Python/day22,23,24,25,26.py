# Function
# def add(a,b):
#     return a + b

# x = int(input('Enter:'))
# y =10

# result = add(x, y)
# print("Answer =", result)


'''home = work
with arguement
    with return
    without return


without aurgument 
     with return
     without return'''


# def factor(a):
#     ans=1
#     for i in range(1,a+1):
#         ans*=1
#     return ans

# num=int(input("Enter:"))
# answer= factor(num)
# print(answer)

# Day 23
# Fabonochi
'''
num=int(input("Enter:"))
a=0
b=1
print(a,b,end=" ")
for _ in range (num):
    c=a+b
    a=b
    b=c
    print(c,end=" ")'''


# Find a prime number with for loop
'''
num=int(input("Enter:"))

ans=True
for i in range(1,num+1):
    if num%i==0:
        print("not a prime number")
        ans=False
        break

if ans==True:
    print("prime")'''
    
# Day 24,Topic- Function

'''
def add(x,y,z):
    return x+y+z

p = int(input('Enter:'))
q= int(input('Enter:'))
r = int(input('Enter:'))
result = add(p,q,r)

# result = add(p)  ERROR TypeError: add() missing 2 required positional arguments: 'y' and 'z'
# result = add(p,q) ERROR TypeError: add() missing 1 required positional argument: 'z'
# result = add(p,q,r,5) ERROR TypeError: add() takes 3 positional arguments but 4 were given

print("Answer =", result)'''



'''def add(x=0,y=0,z=0):
    return x+y+z

result = add(10)
print(result)

result1 = add(10,20)
print(result)


result2 = add(10,20,30)
print(result)

# result3 = add(10,20,30,40)
# print(result)     ERROR !!!!!!!!!!!'''

# args, print & type.
'''def add(*args):
    print(args)
    print(type(args))
add(1,2,3,4,5,6,7,8,9,10)'''

'''def add(*args):
    sum=0
    for i in args:
        sum=sum+i
        return sum
x=(1,2,3,4,5,6,7,8,9,10)
print(x)'''

# Use args, input from user using 'eval function'
'''
def add(*args):
    print(args)
    print(type(args))
    sum=0
    for i in args:
        return sum
x=add(eval(input("enter:")))
print(x)'''

# tuple in tuple.
'''
def add(*args):
    print(args)
    print(type(args))
    sum=0
    for i in args:
        for j in i:
            sum=sum+j
    return sum
x=add(eval(input("Enter:")))
print(x)'''


# Pure tuple,unpack[]
'''
def add(*args):
    print(args)
    print(type(args))
    sum=0
    for i in args:
        # for j in i:
            sum=sum+i
    return sum
x=add(*eval(input("Enter:")))
print(x)'''

# day25

'''
def add(x,y,z):
    print(z)
    print(x)
    print(y)

p=int(input('Enter:'))
q=int(input('Enter:'))
r=int(input('Enter:'))

add(z=p,y=q,x=r)'''

'''
def add(x=0,y=0,z=0):
    print(z)
    print(x)
    print(y)

p=int(input('Enter:'))
q=int(input('Enter:'))
r=int(input('Enter:'))

add(z=p,x=q)'''



# def add(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
    

# add(x=10,y=20,z=30)



'''
def add(x,**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i,j in kwargs.items:
        print('key=',i,'value=',j)

add(10,20,30,40,p=5,r=1,s=2,t=3)
print(x)'''


# all six function summary
'''def add(x,y,*z,p,**q):
    print(x)
    print(y)
    print(z)
    print(p)
    print(q)

add(10,20,30,40,p=5,r=1,s=2,t=3)'''

'''
def add(x,*z,y=0,p,**q):
    print(x)
    print(y)
    print(z)
    print(p)
    print(q)

add(10,20,30,40,p=5,r=1,s=2,t=3)'''


# def natural(n):
#    sum=0
#    for i in range (1,n+1):
#       sum=sum+1
#    print(sum)
# n=int(input("Enter any value:"))
# natural(n)


'''num=int(input("Enter:"))

ans=True
for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        ans=False
        break

if ans==True:
    print("prime")
'''
