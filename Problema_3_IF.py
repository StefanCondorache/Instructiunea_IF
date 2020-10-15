# Să se verifice dacă o literă introdusă este vocală sau consoană. 
# Exemplu : Date de intrare a Date de ieşire vocala.
l=input("litera ")
list1=["a","e","i","o","u","ă","î","â","A","E","I","O","U","Ă","Î","Â"]
list2=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','ș','t','ț','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','Ș','T','Ț','V','W','X','Y','Z']
if l in list1:
    print("vocală")
elif l in list2:
    print("consoană")
else:
    print("caracter greșit")
