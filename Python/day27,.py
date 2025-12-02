# Topic - Variable scope

# local 
# globals
# non-local


'''
def display():
    x=10
    print(x)
display()
# print(x) NameError: name 'x' is not defined'''


'''
def display():
    global x
    x=10
    print(x)
display()
print(x)''' 



# Globals
'''
x=10
def display():
    global x
    print(x)
display()
print(x)''' 


'''
x=10
def display():
    # print(x) This give error
    x=20
    print(x)
display()
print(x)''' 

# For accessing global from local.
'''
x=100
def show():
    x=200
    print(globals()['x'])
show()
print(x)'''




# nonlocal 
'''
def show():

    x=200
    def display():
        nonlocal x
        x=x+5
        print(x)
    display()

show()'''




# calculator , adhi nahi hua hai
while (True):
    print("1.add\n2.sub\n3.div\n4.multi\n5.Exit")
    n=int(input('Enter above value:'))
    if n in (1,2,3,4,5):
        if n in (1,2,3,4):
             if n==1:
                 number=int(input('How many number want to add:'))
                 l=[]
                 for i in range (1,n+1):
                     value=int(int(input(f'Enter  number')))
                     l.append(value)
                     sum=0
                 for i in l:
                     sum=sum+i

print('Please Enter valid value')


