numero = int(input("escribe un numero entre 1 - 5: "))

if numero < 1 or numero > 5:
    print("del 1 - 5")

else:
    while numero != 3:
        print("sigue intentando")
        numero = int(input("escribe un numero entre 1 y 5: "))
    print("correcto")
