def verificarTurno(hora):
   
   
    if hora < 0 or hora > 24:
        return "revisa la hora"
        
    elif hora >= 12 and hora <= 18:
        return "turno de la tarde: "
        
    elif hora > 18:
        return "turno de noche"
        
    elif hora < 12:
        return "turno de mañana"
    
        
hora = float(input("ingresa la hora, en hora militar: "))

mensaje = verificarTurno(hora)
print(mensaje)

