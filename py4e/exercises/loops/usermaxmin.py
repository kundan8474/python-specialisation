l=None
s=None
str="Input number  "

while True:
    i=input(str)
    if i != 'done':
        try:
            i=int(i)
        except Exception as e:
            print("Bad input")
            continue
        if l is None:
            l=i
        elif i>l:
            l=i
        if s is None:
            s=i
        elif i<s:
            s=i
    else:break
print('smallest',s)
print('largest',l)
