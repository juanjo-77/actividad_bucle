def carrito():
    
    while True:
        
        nombre = input("ingrese el nombre del producto------para salir ingrese 0: ")
        precio = float(input("ingrese el precio del producto: "))
        
        
        if precio < 0:
            print("el precio no puede ser negativo")
            continue
        
        if nombre == "0":
            print("saliendo del programa...")
            break
        
        if precio > 100000:
            
            descuento = (precio / 100) * 20
            precio_final = precio - descuento
            print(f"el precio final con descuento es de: {precio_final}")
            
        else:
            print(f"no aplica descuento su total es de: {precio}")
    
carrito()