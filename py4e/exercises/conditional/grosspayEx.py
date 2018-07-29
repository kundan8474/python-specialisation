h=r=-1
try:
    h=int(input('enter hours'))
    r=int(input('enter rate'))
    pay=-1

    if h>10:
        pay=h*r
    else:
        pay=h*r
    print(pay)

except Exception as e:
    print('Error, please enter numeric input')
