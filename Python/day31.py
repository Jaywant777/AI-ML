# Decorator @
'''
def function1():
    def  inner():
         print("hello")
    return inner
x=function1()
print(x) # for checking address
x() # for print output
'''

'''
def decore(fun):
    def  inner(p,q):
         p=p+5
         q=q*2
         print(p,q)
    return inner
def add(x,y):
     print(x+y)
res=decore(add)
res(10,20)'''


'''
def decore(fun):
    def  inner(p,q):
         p=p+5
         q=q*2
         print(p,q)
    return inner
@decore
def add(x,y):
     print(x+y)
add(10,20)
'''

# code By sir (Success)

def decore(fun): # for odd number
    def inner(x):
        for i in range (1,x+1):
            print(2*i-1)
    return inner

@decore #combined, and change even to odd (use @)

def even(n): # for even number 
    for i in range(1,n+1):
        print(2*i)
n=int(input("Enter:"))
even(n)