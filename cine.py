
def calcular_entradas():
    
    while True:
        
        edad = int(input("ingrese su edad: "))
        
        if edad == 0:
            print("Saliendo del programa...")
            break
        
        elif edad < 12:
            print("entrada a 5.000")
            
        elif edad > 12 and edad <= 59:
            print("entrada a 8.000")
            
        else:
            print("entrada a 4.000")
            

calcular_entradas()