def calpay(r,h):
    if h>40:
        pay=r*40+r*1.5*(h-40)
    else:
        pay=r*h
    return pay

rate=input('enter rate')
hours=input('enter hours')

try:
    rate=float(rate)
    hours=float(hours)
except Exception as e:
    print('Bad input',e)
    exit()

print('pay',calpay(rate,hours))
