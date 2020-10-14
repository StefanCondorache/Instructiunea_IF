# Se dau trei numere. Să se afişeze aceste numere unul sub altul, afişând în dreptul fiecăruia unul dintre cuvintele PAR sau
# IMPAR. Exemplu : Date de intrare : 45 3 24 Date de ieşire : 45 impar 3 impar 24 par.
n1=int(input("n1="))
n2=int(input("n2="))
n3=int(input("n3="))
if n1%2==0:
    print(n1,"par")
else:
    print(n1,"impar")
if n2%2==0:
    print(n2,"par")
else:
    print(n2,"impar")
if n3%2==0:
    print(n3,"par")
else:
    print(n3,"impar")