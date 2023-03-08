import random
print("_____craps_____\n")
print("ganas si sacas \n")
print("un par de unos\n un total de tres\n un total de once\n si se optiene dos o doce\n un total de 6")
dado1=random.randint(1,6)
print(dado1)
dado2=random.randint(1,6)
print(dado2)
total=dado1 + dado2
if total==2:
    print("sacaste par de unos ¡Ganaste! ")
if total==3:
    print("sacaste tres en total ¡Ganaste!")
if total==11:
    print("sacaste un total de 11 ¡Ganaste! ")
if total==12:
    print("sacaste un total de 12 ¡Gasnaste! ")
if total==6:
    print("sacaste un total de 6 ¡Ganaste! ")
else:
    print("sacaste un total de ",total,"los siento ¡perdiste!")