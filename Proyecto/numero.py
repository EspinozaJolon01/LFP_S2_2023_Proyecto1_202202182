from abstract_num import Abstract_num

class Numero(Abstract_num):

    def __init__(self,valor, fila, columna):
        self.valor = valor

        super().__init__(fila, columna)

    def operacion(self, arbol):
        return self.valor


    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()