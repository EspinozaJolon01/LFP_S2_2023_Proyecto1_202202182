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

        
        if self.tipo == 'Seno':
            return sin(left_value)
        elif self.tipo == 'Coseno':
            return cos(left_value)
        elif self.tipo == 'Tangente':
            return tan(left_value)
        else:
            return None 
    


