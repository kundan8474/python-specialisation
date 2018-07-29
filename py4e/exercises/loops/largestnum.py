print('list is [-8,-4,-6]')
print('before using None')
larg=-1
small=1000000000000000000000000
for i in [-8,-4,-6]:
    if i>larg:
        larg=i
    if i<small:
        small=i
print('largest',larg)
print('smallest',small)

#while the above written code works just fine it also contains some flow in it
# if we do not know what values are here in the list
# e.g. if list is [-8,-4,-6] then the larget among them is -4 but our code returns -1
# then we can never figure out what should be the starting point of loop
# because we have been comparing the list values with -1 and if it was greater than -1
# then we say that number is the largest one


# hence we should use a more general approach using flag variable as "None"
# None represents that no values have been seen yet
print('\n after using None')
l=None
s=None
for i in [-8,-4,-6]:
    if l is None:
        l=i
    elif l<i:
        l=i
    if s is None:
        s=i
    elif i<s:
        s=i
print('largest',l)
print('smallest',s)

#output

#   list is [-8,-4,-6]
#   before using None
#   largest -1
#   smallest -8

#   after using None
#   largest -4
#   smallest -8
#
