# “Mă iubeşte un pic, mult, cu pasiune, la nebunie, de loc, un pic,…”. Rupând petalele unei margarete cu x petale, el (ea) mă
# iubeşte …. Exemplu: Date de intrare: x=10 Date de ieşire: … de loc.
x=int(input("numarul de petale este egal cu "))
a="Mă iubeşte un pic"
b="Mă iubeşte mult"
c="Mă iubeşte cu pasiune"
d="Mă iubeşte la nebunie"
e="Mă iubeşte de loc"
f="Mă iubeşte un pic"
if x-((x//6)*6)==0:
    print(a)
elif x-((x//6)*6)==1:
    print(b)
elif x-((x//6)*6)==2:
    print(c)
elif x-((x//6)*6)==3:
    print(d)
elif x-((x//6)*6)==4:
    print(e)
elif x-((x//6)*6)==5:
    print(f)
