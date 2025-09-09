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
    print("hola")