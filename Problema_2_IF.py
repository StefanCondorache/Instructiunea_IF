n1=int(input("n1="))
n2=int(input("n2="))
n3=int(input("n3="))
if ((n1<32000) and (n1>0)) and ((n2<32000) and (n2>0)) and ((n3<32000) and (n2>0)):
    if (n1+n2>=n3) or (n1+n3>=n2) or (n2+n3>=n1):
        print("DA")
    elif (n1+n2<n3) or (n1+n3<n2) or (n2+n3<n1):
        print("NU")
else:
     print("numar neaccesibil" )