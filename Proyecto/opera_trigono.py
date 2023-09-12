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
            return round(sin(left_value),2)
        elif self.tipo.operacion(arbol) == 'coseno':
            return round(cos(left_value),2)
        elif self.tipo.operacion(arbol) == 'tangente':
            return round(tan(left_value),2)
        else:
            return None 

    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()


