def evaluar_empleado():
    
    horas_extra = 0
    horas_normales = 0
    
    for  i in range(1, horas + 1):
        
        if i > 8:
            horas_extra += 1
            
        else:
            horas_normales += 1
            
        
        
    print("El empleado", nombre, "trabajo un total de", horas) 
    print("horas, de las cuales", horas_extra, "fueron extras") 
    print(" y " , horas_normales, "fueron normales.")
    
nombre = input("ingrese el nombre del empleado: ")
horas = int(input("ingrese las horas trabajadas en el mes: "))    
    
evaluar_empleado()