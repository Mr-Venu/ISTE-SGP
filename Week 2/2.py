#n program to check if the elements of a given list are unique or not, by using the set data structure
a=[1,2,3,4,10]
b=set(a)
if(len(a)==len(b)):
    print('All elements are unique')
else:
    print('There are repeating elements')
