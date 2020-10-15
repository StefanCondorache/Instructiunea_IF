# La ferma de găini Copanul este democraţie. Fiecare găină primeşte exact acelaşi număr de boabe de porumb. Cele care nu pot
# fi împărţite vor fi primite de curcanul Clapon. Să se spună cine a primit mai multe boabe şi cu cât. În caz de egalitate, se va
# afişa numărul de boabe primite şi cuvântul "egalitate". Datele se vor citi în următoarea ordine: numărul de găini, iar dupa aceea
# numărul de boabe de porumb. Exemplu: Date de intrare 100 4050 Date de ieşire: Curcanul mai mult cu 10 boabe.
g=int(input("numarul de găini este egal cu "))
b=int(input("numarul de boabe este egal cu "))
if g>b:
    del (g,b)
x=b//(g+1)
r=b-(x*g)
if r>x:
    print("curcanul Clapon a primit cu",r-x,"mai multe boabe")
elif r<x:
    print("gainile au primit cu",x-r,"mai multe boabe")
elif r==x:
    print("egalitate")
