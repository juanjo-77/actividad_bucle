def calcular_factorial():
    
    numero = int(input("ingrese un numero: "))
    
    resultado = 1
    
    for i in range(numero, 0, -1):
        
        if numero < 0:
            print("no se pueden numeros negativos")
            
        else:
        
            resultado *= i
            print(f"{i}  resultado parcial es {resultado}")
    
    print(f"El factorial de {numero} es {resultado}")
        
calcular_factorial()