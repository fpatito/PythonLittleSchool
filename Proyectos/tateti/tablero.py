

class Tablero:

    tablero = {
        (1,1):"",
        (1,2):"",
        (1,3):"",
        (2,1):"",
        (2,2):"",
        (2,3):"",
        (3,1):"",
        (3,2):"",
        (3,3):"",
    }



    def insertar(self, posicion, pieza):
        """
        Permite insertar una pieza en determinada posicion del tablero. Devuelve True si se pudo insertar, o false si no se pudo.
        """
        if self.tablero[posicion] == "":
            self.tablero[posicion] = pieza
            return True
        return False

    def verificar_estado(self):

        if self.verificar_filas() == True:
            return True

        elif self.verificar_columnas() == True:
            return True

        elif self.verificar_diagonales() == True:
            return True
        else:
            return False
    
    def verificar_filas(self):
        if self.tablero[(1,1)] == "X" and self.tablero[(1,2)] == "X" and self.tablero[(1,3)] == "X":
            return True
        elif self.tablero[(2,1)] == "X" and self.tablero[(2,2)] == "X" and self.tablero[(2,3)] == "X":
            return True
        elif self.tablero[(3,1)] == "X" and self.tablero[(3,2)] == "X" and self.tablero[(3,3)] == "X":
            return True
        elif self.tablero[(1,1)] == "0" and self.tablero[(1,2)] == "0" and self.tablero[(1,3)] == "0":
            return True
        elif self.tablero[(2,1)] == "0" and self.tablero[(2,2)] == "0" and self.tablero[(2,3)] == "0":
            return True
        elif self.tablero[(3,1)] == "0" and self.tablero[(3,2)] == "0" and self.tablero[(3,3)] == "0":
            return True    

        return False
    def verificar_columnas(self):
        if self.tablero[(1,1)] == "X" and self.tablero[(2,1)] == "X" and self.tablero[(3,1)] == "X":
            return True
        elif self.tablero[(2,1)] == "X" and self.tablero[(2,2)] == "X" and self.tablero[(2,3)] == "X":
            return True
        elif self.tablero[(3,1)] == "X" and self.tablero[(3,2)] == "X" and self.tablero[(3,3)] == "X":
            return True
        elif self.tablero[(1,1)] == "0" and self.tablero[(2,1)] == "0" and self.tablero[(3,1)] == "0":
            return True
        elif self.tablero[(2,1)] == "0" and self.tablero[(2,2)] == "0" and self.tablero[(2,3)] == "0":
            return True
        elif self.tablero[(3,1)] == "0" and self.tablero[(3,2)] == "0" and self.tablero[(3,3)] == "0":
            return True    

        return False

    def verificar_diagonales(self):
        if self.tablero[(1,1)] == "X" and self.tablero[(2,2)] == "X" and self.tablero[(3,3)] == "X":
            return True
        elif self.tablero[(1,1)] == "0" and self.tablero[(2,2)] == "0" and self.tablero[(3,3)] == "0":
            return True
        elif self.tablero[(1,3)] == "X" and self.tablero[(2,2)] == "X" and self.tablero[(3,1)] == "X":
            return True
        elif self.tablero[(1,3)] == "0" and self.tablero[(2,2)] == "0" and self.tablero[(3,1)] == "0":
            return True
    

    def mostrar_tablero(self):
        tablero = f" {self.tablero[(1,1)]} | {self.tablero[(1,2)]} | {self.tablero[(1,3)]} \n---+---+---\n {self.tablero[(2,1)]} | {self.tablero[(2,2)]} | {self.tablero[(2,3)]} \n---+---+---\n {self.tablero[(3,1)]} | {self.tablero[(3,2)]} | {self.tablero[(3,3)]} "
        print(tablero)