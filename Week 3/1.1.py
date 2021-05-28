a={'A':'apple' , 'B':'Ball' , 'C':'cat' , 'D':'Dog'}
b={'D':'Door' ,  'E':'Eagle' , 'F':'Fish' , 'G':'Gun'}
c={}
c.update(a)
c.update(b)
for i,j in a.items():
    for p,q in b.items():
        if(i==p):
            c[i]=j+q
print(c)    
    