from abstract_num import Abstract_num
from math import *

class Opera_trigono(Abstract_num):

    def __init__(self,left,tipo, fila, columna):
        self.tipo = tipo
        self.left = left
        super().__init__(fila, columna)

    def operacion(self, arbol):
        left_value = ''
        if self.left != None:
            left_value = self.left.operacion(arbol)

        
        if self.tipo.operacion(arbol) == 'seno':
            return sin(left_value)
        elif self.tipo.operacion(arbol) == 'coseno':
            return cos(left_value)
        elif self.tipo.operacion(arbol) == 'tangente':
            return tan(left_value)
        else:
            return None 

    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()


