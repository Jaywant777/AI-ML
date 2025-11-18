# ******** Pattern

# For print 12345678........ 
'''n=int(input("enter any value:"))
for j in range(n):
    for j in range(1,n+1):
        print(j,end=(' '))
    print( )'''



'''n=int(input("enter any value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=(' '))
    print( )'''

'''n=int(input("enter any value:"))
for i in range(1,n+1):
    print(''*(n-i)+'* '*i)
for i in range(n-1,0,-1):
    print(''*(n-i)+'* '*i)'''

'''n=int(input("enter any value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(''*(n-i)+'* '*i)
    print( )'''

# 1234567
'''n=int(input("enter any value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(2*j-1,end=(' '))
        # print(2*j,end=(' '))   for even 
        # print(2*j-1,end=(' '))   for odd
    print( )'''

# x='A'
# print(ord(x))

# x='A'
# print(chr(ord(x)+1))

# x=x+1
# ch=chr(ord(x)+1) 




# range abcdefg......
'''n=int(input("enter any value:"))
ch=input("enter any Alphabates:")
for i in range(n):
    print(ch)
    ch=chr(ord(ch)+1)'''


''' Print abcdef
          abcdef
          abcdef
          abcdef'''

n=int(input("Enter any value:"))
ch=input("Enter any Alphabates:")
for i in range(n):
    ch='A'
    for i in range(n):
        print(ch,end=(' '))
        ch=chr(ord(ch)+1)
    print( )


