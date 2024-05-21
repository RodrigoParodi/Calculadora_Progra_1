
from calculos import *

def ingrese_numero_entero(mensaje:str)->int:
    from os import system
    system("cls")

    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            numero = int(entrada)
            break
        else:
            mostrar_mensajes("Error, Numero invalido!!!")
    return numero

def mostrar_mensajes(mensaje):
    from os import system
    system("cls")
    print(mensaje)
    system("pause")

def menuOpciones(x:int , y:int)->str:
    from os import system
    system("cls")
    print("----MENU DE OPCIONES---\n")
    print(f"1. Ingresar 1er operando(A={x})")
    print(f"2. Ingresar 2do operando(B={y})")
    print("3. Calcular todas las operaciones")
    print("4. Informar resultados")
    print("5. Salir")
    opcion_usuario = input("\nIngrese opcion : ")

    return opcion_usuario

def menuCalcular(x:int,y:int):
    from os import system
    system("cls")
    print(f"A)Calcular la suma ({x}+{y})")
    print(f"B)Calcular la resta ({x}-{y})")
    print(f"C)Calcular la division ({x}/{y})")
    print(f"D)Calcular la multiplicacion ({x}*{y})")
    print(f"E)Calcular Factorial ({x}!) ({y}!)")
    print("F)Volver atras")
    opcion_usuario = input("\nIngrese opcion : ").upper()

    return opcion_usuario

def seleccionar_operacion(x,y):
    from os import system
    resultado = 0

    while True:
        match menuCalcular(x,y):
            case "A":
                resultado = sumar_enteros(x,y)
                mensaje_resultado = f"El resultado de {x} + {y} es : {resultado}"
                mostrar_mensajes("Operacion realizada con exito!!!")
                break
            case "B":
                resultado = restar_enteros(x,y)
                mensaje_resultado = f"El resultado de {x} - {y} es : {resultado}"
                mostrar_mensajes("Operacion realizada con exito!!!")
                break
            case "C":
                resultado = dividir(x,y)
                mensaje_resultado = mensaje_division(resultado,x,y)
                mostrar_mensajes("Operacion realizada con exito!!!")
                break
            case "D":
                resultado = multiplicar_enteros(x,y)
                mensaje_resultado = f"El resultado de {x} * {y} es : {resultado}"
                mostrar_mensajes("Operacion realizada con exito!!!")
                break
            case "E":
                factorial_x = factorial(x)
                factorial_y = factorial(y)
                mensaje_resultado = f"El Factorial de {x}! es: {factorial_x} y el factorial de {y}! es: {factorial_y}"
                mostrar_mensajes("Operacion realizada con exito!!!")
                break
            case "F":
                mensaje_resultado = resultado
                break
            case other:
                mostrar_mensajes("Opcion Invalida!!!")

    return mensaje_resultado

def mensaje_division(resultado,x:int,y:int)->str:
    if resultado != 0:
        mensaje_resultado = f"El resultado de {x} / {y} es : {resultado}"
    else:
        mensaje_resultado = "No se puede dividir por zero!!!!"
    
    return mensaje_resultado

