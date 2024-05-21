from funMenus import *
from os import system

x = 0
y = 0

while True:
    match menuOpciones(x,y):
        case "1":
            x = ingrese_numero_entero("Ingrese 1er operando: ")
        case "2":
            y = ingrese_numero_entero("Ingrese 2do operando: ")
        case "3":
            resultado = seleccionar_operacion(x,y)
        case "4":
            mostrar_mensajes(resultado)
        case "5":
            system("cls")
            break
        case other:
            mostrar_mensajes("Opcion Invalida!!!")

print("FIN DEL PROGRAMA")