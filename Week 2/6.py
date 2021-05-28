# a python program to convert a given tuple of positive integers into an integer
a=(25,2,10)
b=""
for i in range(len(a)):
    b=b+str(a[i])
b=int(b)
print(b)
print(type(b))
