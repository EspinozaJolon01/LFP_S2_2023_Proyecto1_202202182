from abstract_num import Abstract_num

class Numero(Abstract_num):

    def __init__(self,valor,tipo, fila, columna):
        self.valor = valor
        self.tipo = tipo
        super().__init__(self,fila, columna)

    def operacion(self, arbol):
        return self.valor