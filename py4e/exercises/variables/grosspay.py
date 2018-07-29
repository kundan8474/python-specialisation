hours=input('input time in hours\n\n')
rate=input('\ninput rate\n')

try:
    hours=float(hours)
    rate=float(rate)
    pay=hours*rate
    print('gross pay for',hours,'hours','at the rate',rate,'is',pay)
except Exception as e:
    print('error',e)
