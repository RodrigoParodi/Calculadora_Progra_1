def sumar_enteros(x:int,y:int)->int:
    """Sumar dos numeros enteros

    Args:
        x (int): Primer numero
        y (int): Segundo Numero

    Returns:
        int: Retorna el resulado de la suma
    """
    return x + y

def restar_enteros(x:int,y:int)->int:
    """Resta dos numeros enteros

    Args:
        x (int): Primer numero
        y (int): Segundo Numero

    Returns:
        int: Retorna el resultado de la resta
    """
    return x - y

def multiplicar_enteros(x:int,y:int)->int:
    """Multiplcia dos numeros enteros

    Args:
        x (int): Primer numero
        y (int): Segundo Numero

    Returns:
        int: Retorna el resultado de la multiplicacion
    """
    return x * y

def dividir(x:int, y:int)->int:
    """Divide dos numeros enteros

    Args:
        x (int): Primer numero
        y (int): Segundo Numero

    Returns:
        int: Retorna el resultado de la operacion y si se dividio por cero retornara 0
    """
    try:
        resultado = x / y
        return resultado
    except:
        resultado = 0
        return resultado

def factorial(n:int)->int:
    """Calcula el factorial de un numero

    Args:
        n (int): Numero a calcular

    Returns:
        int: Retorna el resultado del factoreo
    """
    fact = None
    if n == 0 or n == 1:
        fact = 1
    else:
        fact = n * factorial(n-1)
    return fact

