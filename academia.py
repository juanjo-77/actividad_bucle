def tabla_multiplicar(numero):
    
    for i in range(1, 11):
        
        if i == 10:
            print(f"{numero} x {i} = {numero * i} ")
            
        else:
            print(f"{numero} x {i} = {numero * i} , ", end="")
            
n = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(n)
