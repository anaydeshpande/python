def reverse(x):
    # if length of the list is 1 then print as it is
    if len(x) == 1:
        return x
    # get the list and reverse it
    elif len(x)>1:
        return [x[-1]] + reverse( x[:-1] )

#testing program-Durgesh
list=[1,2,3,4,5,6,7,8,9,10]
y = reverse(list)
print(y)