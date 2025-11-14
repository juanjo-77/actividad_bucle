def calcular_millas():
    total = 0
    
    while True:
        viaje = input("ingrese la distacia del viaje en filometros y dale fin para terminar: ")
        if viaje == "fin":
            break
        
        distancia = float(viaje)
           
        if distancia < 1000:
            total += 500
            
        elif distancia > 3000:
            total += 2000
            
        else:
            total += 1000
            
    print(f"Usted ha acumulado un total de {total} millas")
    
calcular_millas()