
texto_usuario = input("Pon una frase que tu quieras: ")

espacio = " "
punto = "."
comas = ","

n_espacio = 0
n_comas = 0
n_punto = 0

for letra in texto_usuario:
    if letra in punto:
        n_punto +=1
    elif letra in comas:
        n_comas +=1
    elif letra in espacio:
        n_espacio +=1

print("El numero de puntos son: {}".format(n_punto))
print("El numero de comas son: {}".format(n_comas))
print("El numero de espacio son: {}".format(n_espacio))



