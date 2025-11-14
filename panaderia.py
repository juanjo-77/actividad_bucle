def hornear_pan(lotes):
    
    for i in range(1, lotes +1):
        
        if i % 3 == 0:
            print("verificacion de calidad")
            
        elif lotes == i:
            print("produccion terminada")
            
        else: 
            print(f"Lote {i} horneado")
            
n = int(input("¿Cuántos lotes de pan se van a hornear? "))
hornear_pan(n)