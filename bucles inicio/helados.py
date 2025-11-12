clientes = 0

while clientes < 15:
    clientes += 1
    print(f"cliente numero: {clientes}")
    
    if clientes % 5 == 0:
        print("pausa para la limpieza")

    else:
        print("turno finalizado")