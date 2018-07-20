primer_numero = int(input("Coloca el numero a divinar del 1 al 10: "))
segundo_numero = int(input("Coloca uno de prueba (este no vale): "))


while primer_numero < 11 and primer_numero != segundo_numero:

    segundo_numero = int(input("Coloca el numero para a divinar: "))

    if primer_numero != segundo_numero:
        print("Has Perdido")


if primer_numero == segundo_numero:
        print("Has Ganado")

print("Juego Terminado")







