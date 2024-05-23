
from calculos import *

def ingrese_numero_entero(mensaje:str)->int:
    """Pide el ingreso de un numero entero y valida que lo ingresado sea un numero entero

    Args:
        mensaje (str): mensaje de lo que queremos pedir

    Returns:
        int: Retorna el numero entero validado y convertido a entero
    """
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
    """Limpia la consola ,muestra un mensaje y pausea la consola

    Args:
        mensaje (_type_): mensaje que queremos mostrar
    """
    from os import system
    system("cls")
    print(mensaje)
    system("pause")

def menuOpciones(x:int , y:int)->str:
    """Muestra el Menu principal de la calculadora y pide elejor una opcion

    Args:
        x (int): Valor X de la calculadora
        y (int): Valor y de la calculadora

    Returns:
        str: Retorna la opcion elejida por el usuario
    """
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
    """Sub menu para elejir una operacion

    Args:
        x (int): Valor X de la calculadora elejido por el usuario
        y (int): Valor Y de la calculadora elejido por el usuario

    Returns:
        _type_: Retorna la opcion elejida por el usuario
    """
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

def seleccionar_operacion(x,y,resultado):
    """Funcion que se encarga de llamar a las funciones que requiere utilizar el usuario para
        realizar una operacion y retorna un resultado

    Args:
        x (int): Valor X de la calculadora elejido por el usuario
        y (int): Valor Y de la calculadora elejido por el usuario
        resultado (_type_): resultado inicial

    Returns:
        _type_: Retorna el resultado de la operacion realizada por el usuario
    """
    from os import system

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
    """Si se dividio por cero mostrara un mensaje de error.
        Si la division se pudo realizar mostrara su resultado

    Args:
        resultado (_type_): resultado de la division
        x (int): Valor X de la calculadora elejido por el usuario
        y (int): Valor Y de la calculadora elejido por el usuario

    Returns:
        str: Mensaje que mostrara el resultado o el error
    """
    if resultado != 0:
        mensaje_resultado = f"El resultado de {x} / {y} es : {resultado}"
    else:
        mensaje_resultado = "No se puede dividir por zero!!!!"
    
    return mensaje_resultado

