sc=-1.0
try:
    sc=float(input('input score'))
    if(sc>=0.0 and sc<=1.0):
        if sc>=0.9:
            print('A')
        elif sc>=0.8:
            print('B')
        elif sc>=0.7:
            print('C')
        elif sc>=0.6:
            print('D')
        else: print('F')
    else:
        print('Bad score')    
except Exception as e:
    print('Bad score')
