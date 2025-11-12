
def calcularEnergia(repeticiones):
    if repeticiones < 5:
        return "Necesitas más esfuerzo"
    else:
        return "¡Buen trabajo!"


repeticiones = int(input("Ingresa el número de repeticiones: "))
mensaje = calcularEnergia(repeticiones)
print(mensaje)










































# def calcularEnergia(repeticiones):


#     if repeticiones < 0:
#         print("ingrese un dato valido") 
       
#     elif repeticiones < 5:
#         print("necesitas mas esfuerzo")

#     else:
#         print("buen trabajo")

# try:
#     repeticiones = int(input("ingrese numero de repeticiones: "))
#     calcularEnergia(repeticiones)

# except ValueError:
#     print("porfa ingrese un valor valido")

