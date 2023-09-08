from abstract_num import Abstract_num

class Opera_aritm(Abstract_num):


    def __init__(self,left,right,tipo,fila,columna):
        self.left =left
        self.right = right
        self.tipo = tipo
        super().__init__(fila,columna)

    def operacion(self, arbol):
        left_values = ''
        right_values = ''
        if self.left != None:
            left_values = self.left.operacion(arbol)
        if self.right != None:
            right_values = self.right.operacion(arbol)
        
        if self.tipo.operacion(arbol) == 'suma':
            return f'{self.tipo.operacion(arbol)}: {left_values + right_values}'
        elif self.tipo.operacion(arbol) == 'resta':
            return f'{self.tipo.operacion(arbol)}: {left_values - right_values}'
        elif self.tipo.operacion(arbol) == 'multiplicacion':
            return f'{self.tipo.operacion(arbol)}: {left_values * right_values}'
        elif self.tipo.operacion(arbol) == 'division':
            return f'{self.tipo.operacion(arbol)}: {left_values / right_values}'
        elif self.tipo.operacion(arbol) == 'modulo':
            return f'{self.tipo.operacion(arbol)}: {left_values % right_values}'
        elif self.tipo.operacion(arbol) == 'potencia':
            return left_values ** right_values
        elif self.tipo.operacion(arbol) == 'raiz':
            return left_values ** (1/right_values)
        elif self.tipo.operacion(arbol) == 'inverso':
            return 1/right_values
        else:
            return 0
        
    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()