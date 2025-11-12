# litros = 0
# contador = 0
# total = 0

# while total < 100:
#     litros = int(input(f"ingrese cantidad de litros: {contador + 1}: "))

#     total += litros
#     contador += 1
     
   
#     if total < 100:
#       print("sigue vendiendo")

#     else: 
#       print("meta diaria alcanzada")

 
total = 0

while total < 100:

    litros = int(input("Ingresa los litros vendidos: "))
    total += litros
    print(f"Total vendido: {total} litros.")
    
print("Meta diaria alcanzada.")
