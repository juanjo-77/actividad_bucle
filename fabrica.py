numero = int(input("ingrese la cantidad de productos fabricados: "))

for productos in range(1,numero + 1):
    if productos % 2 == 0:
        print("producto verificado")

    else:
        print("producto pendiente")