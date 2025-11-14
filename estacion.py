def simular_viaje(pasajeros):
    
    for i in range(1, pasajeros +1):
        
        if i >= 10:
            print("bus lleno")
        
        elif i < pasajeros:
            print(f"Pasajero {i} a bordo")
        
        
n = int(input("¿Cuántos pasajeros suben al bus? "))
simular_viaje(n)