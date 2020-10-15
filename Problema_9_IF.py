#Pe o masă de biliard sunt bile albe, roşii şi verzi. Din fiecare culoare sunt bile de două dimensiuni: mari şi mici. Să se afişeze
#câte bile sunt în total pe masa de biliard. Un jucător vrea să-i spuneţi care bile sunt mai multe , cele mici sau cele mari, afişând
#numărul lor. De ce culoare sunt bilele cele mai numeroase? Precizaţi numărul lor. Exemplu: Date de intrare Nr. bile albe mici: 2
#Nr. bile albe mari: 3 Nr. bile rosii mici: 1 Nr. bile rosii mari: 4 Nr. bile verzi mici: 3 Nr. bile verzi mari: 4 Date de ieşire Totalul
#bilelor: 17 Mari: 11 bile Verzi: 7 bile .
n1=int(input("Nr. bile albe mici:"))
n2=int(input("Nr. bile albe mari:"))
n3=int(input("Nr. bile rosii mici:"))
n4=int(input("Nr. bile rosii mari:"))
n5=int(input("Nr. bile verzi mici:"))
n6=int(input("Nr. bile verzi mari:"))
print("Totalul bilelor:",n1+n2+n3+n4+n5+n6)
if (n1+n3+n5)>(n2+n4+n6):
    print("Mici:",(n1+n3+n5),"bile")
elif (n1+n3+n5)<(n2+n4+n6):
    print("Mari:",(n2+n4+n6),"bile")
elif (n1+n3+n5)==(n2+n4+n6):
    print("bilele mari și mici sunt de un numar",(n1+n3+n5))
if (n1+n2)>(n3+n4) and (n1+n2)>(n5+n6):
    print("Albe:",(n1+n2),"bile")
elif (n1+n2)<(n3+n4) and (n3+n4)>(n5+n6):
    print("Rosii:",(n3+n4),"bile")
elif (n5+n6)>(n3+n4) and (n2+n1)<(n5+n6):
    print("Verzi:",(n5+n6),"bile")
elif (n1+n2)==(n3+n4) and (n1+n2)>(n5+n6):
    print("Albe și Roșii:",(n1+n2),(n3+n4),"bile")
elif (n1+n2)>(n3+n4) and (n1+n2)==(n5+n6):
    print("Albe și Verzi:",(n3+n4),(n5+n6),"bile")
elif (n5+n6)==(n3+n4) and (n2+n1)<(n5+n6):
    print("Verzi și Roșii:",(n5+n6),(n3+n4),"bile")
elif (n1+n2==n3+n4) and (n3+n4==n5+n6):
    print("toate bilele sunt de un numar",n1+n2)
