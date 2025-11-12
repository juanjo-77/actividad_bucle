def promedioNotas(n1, n2, n3):
    total = (n1 + n2 + n3) / 3

    if total > 5.0 or total < 0:
       print("valida los datos")

    else:

        if total >= 3.0:
         print("aprobado")

        else:
         print("reprobado")

    return total

n1 = float(input("ingrese la nota 1: "))
n2 = float(input("ingrese la nota 2: "))
n3 = float(input("ingrese la nota 3: "))

mensaje = promedioNotas(n1, n2, n3)
print(mensaje)