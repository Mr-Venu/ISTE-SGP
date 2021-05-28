#a python program to compute the element-wise sum of the given tuples
a=(1,2,3)
b=(5,6,7)
c=[]
for i in range(len(a)):
    x=a[i]+b[i]
    c.append(x)
print(tuple(c))
