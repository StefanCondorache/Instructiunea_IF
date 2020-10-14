#La ora de matematică Gigel este scos la tablă. Profesoara îi dictează trei numere şi îi cere să verifice dacă cele trei numere pot fi
# laturile unui triunghi. Ajutaţi-l pe Gigel să afle rezultatul. Scrieţi un program care primeşte numerele lui Gigel, care sunt mai mici
# ca 32000, şi returnează DA sau NU. Observaţie: Trei numere pot fi laturile unui triunghi numai dacă fiecare este mai mic ca
# suma celorlalte două. Exemple: Date de intrare 3 5 7 Date de ieşire Da Date de intrare 2 5 9 Date de ieşire Nu.

n1=int(input("n1="))
n2=int(input("n2="))
n3=int(input("n3="))
if ((n1<32000) and (n1>0)) and ((n2<32000) and (n2>0)) and ((n3<32000) and (n2>0)):
    if ((n1+n2)>=n3) and ((n1+n3)>=n2) and ((n2+n3)>=n1):
        print("DA")
    elif (n1+n2<n3) or (n1+n3<n2) or (n2+n3<n1):
        print("NU")
else:
     print("numar neaccesibil" )
