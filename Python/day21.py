# Control statement
# 1.Continue - To skip current itreation.
# 2.Break - to treminate current loop.
# 3.Pass - to skip current block.

n=int(input("1Enter any value:"))
i=1
while i<=n:
    print(i)
    i=i+1


'''n=int(input("2Enter any value:"))
i=1
while i<=n:
    if i==5:
        continue
    else:
      print(i)
    i=i+1'''

# Infinite!!!!!!!
'''
n=int(input("3Enter any value:"))
i=1
while i<=n:
    if i==5:
        print("hello")
        continue
    else:
      print(i)
    i=i+1'''


n=int(input("4Enter any value:"))
i=1
while i<=n:
    if i==5:
       pass
    else:
      print(i)
    i=i+1


n=int(input("5Enter any value:"))
i=1
for i in range(1,n+1):
    if i==5:
       continue
    else:
      print(i)


n=int(input("6Enter any value:"))
i=1
while i<=n:
    if i==5:
       i=i+1
       continue
    else:
      print(i)
    i=i+1

'''
x=10
if x%2==0:
   pass'''

n=int(input("7Enter any value:"))
i=1
while i<=n:
   if i==5:
      break
   else:
      print(i)
      i=i+1
print("hello")