palabra1 = input("ingrese la palabra: ")

for palabra in range(1,6):

    if palabra % 2 != 0:
        print(palabra1.upper())

    else:
        print(palabra1.lower())