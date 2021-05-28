#program to check if the elements of a given list are unique or not, by looping over the list
a=[1,2,3,4,3,10]
n=0
for i in range (len(a)):
    for j in range (i+1,len(a)):
        if(a[i] == a[j]):
            n=1

if(n==1):
    print('False')
else:
    print('True')
