# square pattern in star
n=int(input("enter any value:"))
for i in range(1,6):
    print('* '*n)

# left side pattern in star
n=int(input("enter any value:"))
for i in range(1,n+1):
    print(' '*(n-1)+'* '*i)

# Prymaid pattern in star
n=int(input("enter any value:"))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*i)

# left side pattern in star
n=int(input("enter any value:"))
for i in range(1,n+1):
    print('* '*i)

# upside down,left side pattern in star
n=int(input("enter any value:"))
for i in range(1,n+1):
    # print(''*i+'* '*(n-i))
    print(''*i+'* '*(n-i))


# success , But by sir semi left side dimoand.
n=int(input("enter any value:"))
for i in range(1,n+1):
    print(''*(n-i)+'* '*i)
for i in range(n-1,0,-1):
    print(''*(n-i)+'* '*i)
