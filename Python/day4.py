# x=10.5
# y=int(x)
# print(y)
# z=float(y)
# print(z)

# p=complex(z)
# print(p)

# # q=str(p)
# # print(q)

l=[10,20,30,40,50]
t=tuple(l)
print(t)
# (10, 20, 30, 40, 50)

l1=list(t)
print(l1)
# [10, 20, 30, 40, 50]

st=set(t)
print(st)
# {40, 10, 50, 20, 30}

fs=frozenset(st)
print(fs)
# frozenset({50, 20, 40, 10, 30})

# print(sep='',end='\n')
print("Hello",end='+')  
print("Welcome")

# print("Hello",end='+',sep=",")  
# print("Welcome")

x=input("enter any value:")
print(x)
print(type(x))
# enter any value:500
# 500
# <class 'str'>

# used to give datatype of user in run time, like str,int,list,tuple, 
y=eval(input("enter any value:"))
print(y)
print(type(y))


# NEXT "CONTROL STATEMENT"

