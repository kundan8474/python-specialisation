import re
handle=open('actualdataweek2.txt')
lst=list()
for lines in handle:
    lines=lines.strip()
    l=re.findall('[0-9]+',lines)
    if len(l)>0:
        for x in l:
            lst.append(int(x))
print(sum(lst))
