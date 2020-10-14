# Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
# exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. 
# Exemplu : Date de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani. 
print("data curenta")
anul1=int(input("anul="))
luna1=int(input("luna="))
ziua1=int(input("ziua="))
print("data nasterii")
anul2=int(input("anul="))
luna2=int(input("luna="))
ziua2=int(input("ziua="))
if (anul2>anul1) or (ziua1>31) or (ziua2>31) or (luna1>12) or (luna2>12):
    print("IMPOSIBIL")
    del(anul1,anul2)
if (luna1>=luna2):
    if (ziua1<ziua2):
        print((anul1-anul2)-1,"ani")
    elif (ziua1>=ziua2):
        print(anul1-anul2,"ani")
elif (luna1<luna2):
    print((anul1-anul2)-1,"ani")
    
