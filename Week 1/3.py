#Printing the factorial of a user input number
n=int(input('Enter a number '))
t=n
f=1
while(n>1):
    f=f*n
    n=n-1
print('Factorial of',t,'is',f)
