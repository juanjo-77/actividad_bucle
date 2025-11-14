

def calcular_puntos(compras):
    puntos = 0
    for i in range(1, compras + 1):
        print(f"Compra {i} registrada.")
        
        if i % 3 == 0:
            puntos += 10
            print("¡Has ganado un bono de 10 puntos por tu tercera compra!")
        else:
            puntos += 5
            print("Has ganado 5 puntos por tu compra.")
            
    print(f"Has acumulado {puntos} puntos por tus compras.")  
           
n = int(input("¿Cuántas compras has realizado? "))
calcular_puntos(n)