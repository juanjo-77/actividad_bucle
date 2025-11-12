montos = 0
contador = 0
total = 0

while True:
    montos = float(input(f"ingresa el monto numero {contador + 1}: "))
    
    if montos == 0:
        break 
    
    contador += 1  
    total += montos
    
    if montos > 100000:
        print("venta destacada") 

print(f"el total es: {total}")