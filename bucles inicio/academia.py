num = int(input("ingrese el numero: "))

for num in range(1,num + 1):
    print(f"numero: {num}")
    
    if num % 5 == 0:
        print("gran avance")
        
    else:
        print("ejercicio completado") 