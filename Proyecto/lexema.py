from abstract_num import Abstract_num

class Lexema(Abstract_num):

    def __init__(self,lexema, fila, columna):
        self.lexema = lexema
        super().__init__(fila, columna)

    def operacion(self, arbol):
        return self.lexema
    
    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()