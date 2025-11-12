def calcularInteres(monto, tasa):
    intereses = monto * (tasa/100)
    valorFinal = monto + intereses
    return valorFinal
monto = float(input("ingrese el monto"))
tasa = float(input("ingrese la tasa"))

resultado = calcularInteres(monto, tasa)
print(f"el monto final despues de los intereses es: {resultado}")