import re
lst=list()
sum1=0
lst=re.findall('[0-9]+',open('actualdataweek2.txt').read())
for i in lst:
    sum1=sum1+int(i)
print(sum)
