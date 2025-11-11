total = 0

for mes in range(1,7):
    ahorro_mes = float(input(f"ingrese el ahorro del mes {mes}: "))

    total += ahorro_mes

    if total >= 1000000:
        print("meta alcanzada")
        
print(f"total acumulado de ahoroo: {total}: ")