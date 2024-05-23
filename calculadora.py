from funMenus import *
from os import system

x = 0
y = 0
resultado = 0
bandera = False

while True:
    match menuOpciones(x,y):
        case "1":
            x = ingrese_numero_entero("Ingrese 1er operando: ")
            bandera = False
        case "2":
            y = ingrese_numero_entero("Ingrese 2do operando: ")
            bandera = False
        case "3":
            resultado = seleccionar_operacion(x,y,resultado)
            bandera = True
        case "4":
            if bandera == True:
                mostrar_mensajes(resultado)
            else:
                mostrar_mensajes("Primero Debes seleccionar una operacion!!!")
        case "5":
            system("cls")
            break
        case other:
            mostrar_mensajes("Opcion Invalida!!!")

print("FIN DEL PROGRAMA")