
def calcular_propina(total_cuenta):

    if total_cuenta > 100000:
        total =  (total_cuenta / 100) * 15
        promedio = total + total_cuenta
        return f"el total a pagar con la propina es: {promedio} ya que tu cuenta es mas grande tienes mas descuento"
    
    else: 
        total = (total_cuenta / 100) * 10
        promedio = total + total_cuenta
        return f"el total a pagar con la propina es: {promedio}"
    
    
total_cuenta = float(input("ingrese el monto sin la propina: "))

mensaje = calcular_propina(total_cuenta)
print(mensaje)