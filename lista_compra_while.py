
mi_lista = []
input_usuario = ""
input_usuario = input("Que quieres en tu lista: (Escribe FIN para salir)")


while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("Que quieres en tu lista: (Escribe FIN para salir)")

for item in mi_lista:
    print("Tengo que ir a comprar: {}".format(item))


print("Mi lista de compra")
