reps = int(input("ingresa el numero de repeticiones: "))

for reps in range(1,reps + 1):

    print(f"repeticion numero {reps}")
    
    if reps < 0:
        print("ingrese un numero valido")
        
    else: 
        
        if reps % 3 == 0:
            print("excelente ritmo") 