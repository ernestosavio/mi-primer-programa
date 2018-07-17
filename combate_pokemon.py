

pokemon_elegido = input("Contra quien quieres luchar (Squirtle / Charmander / Bulbaur): ")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    nombre_pokemon = "Squirtle"
    ataque_pokemon = 8

elif pokemon_elegido == "Charmander":
        vida_enemigo = 80
        nombre_pokemon = "Charmander"
        ataque_pokemon = 7

elif pokemon_elegido == "Bulbaur":
            vida_enemigo = 100
            nombre_pokemon = "Bulbaur"
            ataque_pokemon = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("Que ataque vamos a usar (Chispazo / Bola voltio): ")
    if ataque_elegido == "Chispazo":
        vida_enemigo -=10
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -=12

    print("Ahora la vida del {} es {}".format(nombre_pokemon, vida_enemigo))
    vida_pikachu -= ataque_pokemon

    print("{} te hizo {} de daño".format(pokemon_elegido, ataque_pokemon))

    print("Tienes {} de vida".format(vida_pikachu))

if vida_enemigo <= 0:
    print("HAS GANADO")
if vida_enemigo >= 0:
    print("HAS PERDIDO")

print("Ha termino la batalla")