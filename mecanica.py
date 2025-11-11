contador = 0

for revision in range(1,4):
    contador += 1

    if revision == 3:
        print("revision especial de motor")
    else:
        print(f"{revision}")