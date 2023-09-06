from abstract_num import Abstract_num

class Opera_aritm(Abstract_num):


    def __init__(self, left,right,tipo, fila, columna):
        self.left =left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operacion(self, arbol):
        left_values = ''
        right_values = ''
        if self.left != None:
            left_values = self.left.operacion(arbol)
        if self.right != None:
            right_values = self.left.operacion(arbol)
        
        if self.tipo == "Suma":
            return left_values + right_values
        elif self.tipo == "Resta":
            return left_values - right_values
        elif self.tipo == "Multiplicacion":
            return left_values * right_values
        elif self.tipo == "Division":
            return left_values / right_values
        elif self.tipo == "Modulo":
            return left_values % right_values
        elif self.tipo == "Potencia":
            return left_values ** right_values
        elif self.tipo == "Raiz":
            return left_values ** (1/right_values)
        elif self.tipo == "Inverso":
            return 1/right_values
        else:
            return 0
        
        