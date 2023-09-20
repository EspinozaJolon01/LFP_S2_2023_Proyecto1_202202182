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
        
        if self.tipo.operacion(arbol).lower()  == 'suma':
            return round(left_values + right_values,2)
        elif self.tipo.operacion(arbol).lower()  == 'resta':
            return round(left_values - right_values,2)
        elif self.tipo.operacion(arbol).lower()  == 'multiplicacion':
            return round(left_values * right_values,2)
        elif self.tipo.operacion(arbol).lower()  == 'division':
            return round(left_values / right_values,2)
        elif self.tipo.operacion(arbol).lower()  == 'mod':
            return round(left_values % right_values,2)
        elif self.tipo.operacion(arbol).lower()  == 'potencia':
            return round(left_values ** right_values,2)
        elif self.tipo.operacion(arbol).lower()  == 'raiz':
            return round(left_values ** (1/right_values),2)
        else:
            return 0
        
    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()