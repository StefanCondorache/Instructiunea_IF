# La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
# secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? 
# Exemplu : date de intrare : x=38 date de ieşire : rosie. 
x=int(input("x="))
if (x>=1) and (X<=100):
    if x<=25:
        print("albă")
    elif (x>25) and (x<=50):
        print("roşie")
    elif (x>50) and (x<=75):
        print("albastră")
    elif x>75:
        print("neagră")