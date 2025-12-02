
n=int(input("Enter any value:"))
for i in range(1,n+1):
           print(i,end='')
           print()

n=int(input("Square  Pattern Enter Value:"))
for j in range(n):
    for j in range(1,n+1):
        print(j,end=(' '))
    print( )

n=int(input("Natural Num stair Enter:"))
for x in range(1,n+1):
    for i in range(1,x+1):
           print(i,end=' ')
    print()

n=int(input("Even Num stair Enter:"))
for x in range(1,n+1):
    for i in range(1,x+1):
           print(2*i,end=' ')
    print()


n=int(input("odd Num stair Enter:"))
for x in range(1,n+1):
    for i in range(1,x+1):
           print(2*i-1,end=' ')
    print()

# Prymaid Of 1234567890. (Task by sir,Failed!!!!!!!!!!)
n=int(input("Prymaid Enter:"))
for i in range(n):
    for j in range(n-i-1):
         print(" ",end="")
    for j in range(i+1):
         print(j+1,end="  ")
    print()
