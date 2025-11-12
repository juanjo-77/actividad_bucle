def promedio_notas(n1, n2, n3):
    total = (n1 + n2 + n3) / 3
    

    if total >= 3.0:
        return f"aprobado con promedio de {total:.2f}"
            
    else:
        return f"reprobado con promedio de {total:.2f}"
            

while True:
        estudiante = input("ingrese el numero del estudiante (0 para salir): ")
        
        if estudiante == "0":
           break        

        n1 = float(input("ingrese la nota 1: "))
        n2 = float(input("ingrese la nota 2: "))
        n3 = float(input("ingrese la nota 3: "))

        mensaje = promedio_notas(n1, n2, n3)
        print(f"{estudiante} {mensaje} \n")
