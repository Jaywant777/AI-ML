# Lambda

'''
x=lambda x,y,z:2*x+y+z
print(x(1,2,3))'''

'''
x=lambda x,y:x if x>y else y
print(x(50,10))
'''

'''
n=int(input('Enter'))
x=lambda age: 'child' if 0<age<18 else ('adult' if 17<age<60 else ('senior' if 59<age else 'invlaid'))
print(x(n))
'''

'''
n=int(input('Enter:'))
x= lambda n: n**2
print(x(n))
'''
# n=int(input('Enter:'))
# x=lambda n: [i for i in range(1,n+1)]
# print(x(n))


'''
n=int(input('Enter:'))
x=lambda n: [i for i in range(1,n+1) if i%2==0]
print(x(n))
'''
# l1=[1,2,3]
# l2=[4,5,6]
# l3=[7,8,9]
# print(list(map(lambda x,y,z:x*y*z,l1,l2,l2)))

'''
l=[1,2,3,4,5,6,7]
print(list(filter(lambda x:x%2==0,l)))'''

from functools import reduce
l=int(input('Enter:'))
print(list(reduce(lambda x:x%2==0,l)))