sum=0
avg=0.0
count=0
str='Enter a number '

while True:
    i=input(str )
    if i =='done':
        break
    else:
        try:
            i=int(i)
        except Exception as e:
            print('Bad input\n')
            continue
        sum=sum+i;
        count=count+1
if count>0:
    print(sum,sum/count)
