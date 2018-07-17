apetece_helado_inputt = input("Te apetece un helado: (Si / No) ").upper()

if apetece_helado_inputt == "SI":
    apetece_helado = True
elif apetece_helado_inputt == "NO":
    apetece_helado == False
else:
    print("Te dije que digas SI / NO PERO CUENTO COMO QUE NO")
    apetece_helado = False

tienes_dinero_inputt = input("Tienes dinero para un elado?: (Si / No) ").upper()
senor_helado_inputt = input("Esta el señor de los helados?: (Si / No) ").upper()
esta_tu_tia_inputt = input("Esta tu tia con vos?: (Si / No) ").upper()

apetece_helado = apetece_helado_inputt == "SI"
tienes_dinero = tienes_dinero_inputt == "SI" or esta_tu_tia_inputt == "SI"
senor_helado = senor_helado_inputt == "SI"

if apetece_helado and tienes_dinero and senor_helado:
    print("comete un helado")
else:
    print("pues nada")



