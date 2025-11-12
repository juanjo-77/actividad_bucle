
real = "12345"
intento = 1

while intento <= 3:
    intento += 1
    contraseña = input("ingrese la contraseña: ")

    if contraseña == real:
        print("acceso permitido")
        break

    elif contraseña != real:
        print("acceso denegado")