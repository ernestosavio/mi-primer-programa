
texto_usuario = input("Introdusca un texto: ")

vocal = ["a", "e", "i", "o", "u"]

lista_vocal = []

for letra in texto_usuario:
    if letra in vocal:
        lista_vocal.append(letra)

print(lista_vocal)
