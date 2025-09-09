#OPCION 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
#OPCION 2
def suma_entero(n):
    if n < 0:
        return "Debe ser un numero positivo"
    else:
        return n + 1
#OPCION 3
def fibonacci(n=0):
    if n < 0:
        return "Debe ser un numero positivo"
    else:
        return n + n+1
#OPCION 4
def contar_letra(text):
    if len(text()):
        pass
while True:
    print("-"*10 + "MENU" + "-"*10 + "\n"
          "1. Calcular el factorial de un numero\n"
          "2. Suma de los primeros numeros naturales\n"
          "3. Calcular el numero de fibonacci\n"
          "4. Cuantas veces aparece una letra en una palabra\n"
          "5. Invertir cadena de un texto\n"
          "6. Calcular la potencia de un número\n"
          "7. Salir")
    option = int(input("Ingrese la opcion que desea consultar: "))
    match option:
        case 1:
            n = int(input("Ingrese un número: "))
            factorial()
            print(f"El factorial de {n} es: {factorial(n)}")
        case 2:
            n = int(input("Ingrese un número: "))
            suma_entero()
            print(f"La suma de {n} es: {factorial(n)}")
        case 3:
            n = int(input("Ingrese un numero: "))
            fibonacci()
            print(f"El numero en fibonacci es: {fibonacci(n)}")
        case 4:
            n = int(input("Ingrese una palabra"))

        case 5:
            pass
        case 6:
            pass
        case 7:
            print("Saliendo del programa...")
        case _:
            print("Ingrese una opcion valida")
