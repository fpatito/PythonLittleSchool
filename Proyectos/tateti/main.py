
from tablero import Tablero


tablero = Tablero()


def cambiar_turno(turno):
    if turno == "X":
        turno = "0"
    elif turno == "0":
        turno ="X"
    return turno

def bucle():

    contador = 0

    jugador1 = "X"
    jugador2 = "0"

    turno = jugador1

    while contador < 9:
        tablero.mostrar_tablero()
        
        print(f"turno: {turno}")
        fila = int(input("Ingrese fila:"))
        col = int(input("Ingrese columna:"))

        tablero.insertar((fila, col), turno)

        if tablero.verificar_estado() == True:
            print(f"\nGano {turno}\n")
            tablero.mostrar_tablero()
            break
        else:
            turno = cambiar_turno(turno)
        
bucle()

