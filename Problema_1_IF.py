# Se introduc trei date de forma număr curent elev, punctaj. 
# Afişaţi numărul elevului cu cel mai mare punctaj. Exemplu : Date de
# intrare nr crt 7 punctaj 120 nr crt 3 punctaj 100 nr crt 4 punctaj 119 
# Date de ieşire punctaj maxim are elevul cu nr crt 7.

n1=int(input("nr crt "))
p1=int(input("punctaj"))
n2=int(input("nr crt"))
p2=int(input("punctaj"))
n3=int(input("nr crt"))
p3=int(input("punctaj"))
if (p1>0) and (p2>0) and (p3>0):
    if (p1>p2) and (p1>p3):
        print("punctaj maxim are nr crt",n1)
    elif (p2>p1) and (p2>p3):
        print("punctaj maxim are nr crt",n2)
    elif (p3>p1) and (p3>p2):
        print("punctaj maxim are nr crt",n3)
    elif (p1==p2) and (p1>p3):
        print("punctaj maxim are nr crt",n1,n2)
    elif (p1==p3) and (p1>p2):
        print("punctaj maxim are nr crt",n1,n3)
    elif (p3==p2) and (p3>p1):
        print("punctaj maxim are nr crt",n2,n3)
else: 
    print("punctaj negativ")
