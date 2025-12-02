# Generator

'''
x=range(1,100)
print(list(x))
print(id(list(x)))
'''

'''
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i==1 or i==2:
        print(i)
print('Hello')
print('welcome')
for i in l:
    if i==3 or i==4:
        print(i)'''


'''
def natural_no(n):
    i=1
    while i<=n:
        yield i 
        i=i+1
x=int(input("enter:"))
res=natural_no(x)
print(res)

# for i in res:
#     print(i)

# print(next(res))
# print(next(res))

for _ in range(2):
    print(next(res))

for _ in range(3):
    print(next(res))'''



def natural_no(n):
    i=1
    while i<=n:
        yield i 
        i=i+1
x=int(input("enter:"))
res=natural_no(x)
print(res)

# for i in res:
#     print(i)

# print(next(res))
# print(next(res))

for _ in range(10):
    try:
        print(next(res))
    except StopIteration:
        print("all elements are itreated i.e. collection is empty")
        break


l=[1,2,3,4,5]
print(l)

x=iter(l)
print(x)