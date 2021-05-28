a='An apple a day keeps doctor away'
b='water'
c=0
for j in range(len(b)):
    for i in range(len(a)):
        if(a[i]==b[j]):
            c=1
            print(a[:i])  
            break
    if(c==1):
        break