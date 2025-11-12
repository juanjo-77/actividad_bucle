def evaluar_credito(ingresos, edad):
    
    if edad >= 25 and edad <= 60  and  ingresos >= 2000000:
        return "credito aprobado"
    else:
        return "credito rechazado"
    
ingresos = float(input("escribe el valor de tus ingresos: "))
edad = int(input("ingresa tu edad: "))

mensaje = evaluar_credito(ingresos, edad)
print(mensaje)
