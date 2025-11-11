# Control statement


# # if statement
a=int(input("Enter any value:"))
if a>=1:
    print("Given number is Positive")


# # if else statement
b=int(input("Enter any value:"))
if b>=1:
    print("Given number is Positive")
else:
    print(f'Given number {b} is zero or negetive')


# # if elif statement
c=int(input("Enter any value:"))
if c>=1:
    print("Given number is Positive")
elif c==0:
    print(f'Given number {c} is zero')


# # if elif else 
d=int(input("Enter any value:"))
if d>=1:
    print("Given number is Positive")
elif d==0:
    print(f'Given number {d} is zero')
else:
    print(f'Given number {d} negetive')





# Make a program to print kid,adult and senoir citizon according to age.
age=int(input("Enter your age:"))
if 0<age<18:
    print("You are a kid")
elif 17<age<60:
    print(f'You are an adult')
elif 59<age<100:
    print(f'Your are an senoir citizon')
else:
    print(f'Given number is invalid')






# Make a program to print a student ,is either Fail or pass.

h=int(input("Enter your Hindi mark:"))
if 0<=h<=100:
    e=int(input("Enter your English mark:"))
    if 0<=e<=100:
        m=int(input("Enter your Maths mark:"))
        if 0<=m<=100:
            avg=((h+e+m)/3)
            if 0<=avg<=34:
               print('Fail')
            elif 35<=avg<=44:
               print('3rd Division')
            elif 45<=avg<=59:
               print('2nd Division')
            else:
               print('1st Division')

   