def sumar_enteros(x:int,y:int)->int:
    return x + y

def restar_enteros(x:int,y:int)->int:
    return x - y

def multiplicar_enteros(x:int,y:int)->int:
    return x * y

def dividir(x:int, y:int)->int:
    try:
        resultado = x / y
        return resultado
    except:
        resultado = 0
        return resultado

def factorial(n:int)->int:
    fact = None
    if n == 0 or n == 1:
        fact = 1
    else:
        fact = n * factorial(n-1)
    return fact

