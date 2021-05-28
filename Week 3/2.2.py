#Finding all occurrences of ‘are’ in any string entered by the user and updating the counter each time
a=str(input('Type some sentences: '))
b=a.split()
n=0
for i in b:
    if(i=='are'):
        n=n+1
print('Frequency of \'are\' in your sentences is ',n)        
