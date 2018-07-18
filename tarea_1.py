user_operation = input("Que operacion quieres hacer? (Suma / Resta / Divicion / Multiplicacion): ")

primer_numero = float(input("Elije el segundo numero: "))
segundo_numero = float(input("Elije el segundo numero: "))

if user_operation == "Suma":
   resultado_suma = float(primer_numero + segundo_numero)
   print("El resultado es: {} ".format(resultado_suma))

elif user_operation == "Resta":
    resultado_resta = float(primer_numero - segundo_numero)
    print("El resultado es: {}".format(resultado_resta))

elif user_operation == "Multiplicacion":
    resultado_multiplicacion = float(primer_numero * segundo_numero)
    print("El resultado es: {}".format(resultado_multiplicacion))

elif user_operation == "Divicion":
    resultado_divicion = float(primer_numero / segundo_numero)
    print("El resultado es {}".format(resultado_divicion))






