def aplicar_descuentos():
    total_general = 0
    
    while True:
        precio = int(input("ingrese el precio: "))
        if precio == 0:
            print(f"\nel total de todas las compras es: {total_general}")
            break
        
        elif precio > 50000:
            
            porcentaje = (precio / 100) * 10
            total = precio - porcentaje
            total_general += total
            print(f"el total de su compra fue de: {total}")
            
        else: 
            total_general += precio
            print(f"total a pagar{precio}")
            
            
            
aplicar_descuentos()