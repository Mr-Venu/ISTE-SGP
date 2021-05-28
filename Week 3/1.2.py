#A program to print the total number of occurrences(frequency) of every character in a string
using python dictionaries
a='abbcccddddeeeeeffffff'
b={}
for i in range(len(a)):
    n=0
    for j in range(len(a)):
        if(a[j]==a[i]):
            n=n+1
        b.update({a[i]:n})        
print(dict(b))
