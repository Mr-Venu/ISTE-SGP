# a code which returns the first m multiples of a natural number n, without using any loop
print('Printing first m multiples of n')
m=int(input('Enter m '))
n=int(input('Enter n '))
i=range(n,m*n+1,n)
print(list(i))
