# i=int(input("Enter any value:"))
# while i>=10:
#     print(i)

'''i=int(input("Enter any value:"))
td=0
while i>0:
     td=td+1
     
     i=i//10
print("Total Digit",td)'''


n=153
m=p=n
td=sum=0
while n>0:
    td=td+1
    n=n//10
while m>0:
    id=m%10=1
    sum=sum+id**td
    m=m//10
if p==m:
    print(f'Given {p} is armstrong')
else:
    print(f'Given {p} is notarmstrong')