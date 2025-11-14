def evaluar_paciente():
    
    while True:
        
        nombre = input("ingrese el nombre del paciente---> para salir ingrese 'fin': ")
        
        temperatura = float(input("ingrese la temperatura del paciente: "))
        frecuencia = int(input("ingrese la frecuencia cardiaca del paciente: "))
        
        if nombre == "fin":
            print("Saliendo del programa...")
            break
        
        if temperatura > 38 or frecuencia > 100:
            print("paciente en observacion")
            
        else:
            print("estas aliviado")
        
evaluar_paciente()