import random


valorcompra=int(input("ingrese en valor de la compra"))
if valorcompra>50000:
    print("podras participar para el descuento de tu compra ")
    print("Si sacas la bolita roja obtienes 10% en el valor de tu compra ")
    print("Si sacas la bolita azul obtienes un 30% en el valor de tu compra")
    print("si sacas la bolita amarilla obtienes un 50% en el valor de tu compra")
    print("Si sacas la bolita blanca te llevas tu compra gratis")
    bolitas=random.randint(1,3)
    print(bolitas)
    if bolitas==1:
        print("sacaste la roja tines un 10 de descuento")
        valorcondescuento=valorcompra*0,10
        total=valorcompra-valorcondescuento
        print("su total a pagar es de  ", total)
    if bolitas==2:
        print("sacaste la azul tines un 30 de descuento")
        valorcondescuento=valorcompra*0,30
        total=valorcompra-valorcondescuento
        print("su total a pagar es de  ", total)
        
    if bolitas==3:
        print("sacaste la amarilla tines un 50 de descuento")
        valorcondescuento=valorcompra*0,50
        total=valorcompra+valorcondescuento
        print("su total a pagar es de  ",total )
else:
    print("el monto es muy bajo no participa en el descuento ")
    