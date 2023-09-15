from opera_aritm import Opera_aritm
from opera_trigono import Opera_trigono
from lexema import Lexema
from numero import Numero
from abstract_num import Abstract_num
from lexema_errores import Lexema_errores
import json
import os



class analizador:


    global linea 
    global columna
    global instrucciones
    global lista_lexa
    global lista_errores
    global lexem

    
    lista_lexa = []
    instrucciones = []

    
    lista_errores= []
    

    def __init__(self) :
        self.text = ''
        self.fon = ''
        self.fuen = ''
        self.form = ''
            
        self.num_linea = 1 
        self.num_columna = 1


    reversed = {
        'OPERACIONES' : 'operaciones',
        'Valor1': 'valor1',
        'Valor2': 'valor2',
        'Operacion': 'operacion',
        'SUMA' : 'suma',
        'RESTA': 'resta',
        'MULTIPLICACIÓN' : 'multiplicacion',
        'DIVISIÓN' : 'division',
        'POTENCIA' : 'potencia',
        'RAIZ' : 'raiz',
        'INVERSO' : 'inverso',
        'SENO' : 'seno',
        'COSENO' : 'coseno',
        'TANGENTE' : 'tangente',
        'MOD' : 'mod',
        'CONFIGURACIONES' : 'configuraciones',
        'text' : 'Operaciones',
        'FONDO' : 'azul',
        'fuen' :'blanco',
        'texts' : 'texto',
        'Fondo' : 'fondo',
        'fuen' : 'fuente',
        'Forma' : 'forma',
        'Circulo' : 'circulo',
        'COMA' : ',',
        'PUNTO' : '.',
        'PUNTOS': ':',
        'CORCHETEA' : '[',
        'CORCHETEC' : ']',
        'LLAVEA' : '{',
        'LLAVEC' : '}'
    }

    lexem = list(reversed.values())


    def insutrucciones_lexam(self, lista):
        global linea
        global columna
        global lista_lexa
        global lista_errores
        global lexem
        
        lexema = ''
        contador = 1
        
        
        puntero = 0

        while lista:
            char = lista[puntero]
            puntero += 1

            if char == '\"':
                lexema, lista = self.coleccionar_lexema(lista[puntero:])
                if lexema and lista:
                    self.num_columna += 1
                    lexemas = Lexema(lexema,self.num_linea,self.num_columna)
                    lista_lexa.append(lexemas)
                    self.num_columna += len(lexema) + 1
                    puntero = 0

            elif char.isdigit():
                token, lista = self.fomar_numero(lista)
                if token and lista:
                    self.num_columna += 1
                    
                    numeros = Numero(token,self.num_linea,self.num_columna)


                    lista_lexa.append(numeros)
                    self.num_columna += len(str(token)) + 1

                    puntero = 0
                

            elif char == '[' or char == ']':

                lex = Lexema(char,self.num_linea,self.num_columna)

                lista_lexa.append(lex)
                lista = lista[1:]
                puntero = 0
                self.num_columna += 1
            
            elif char == '\t':  # si el char es igual un tabulacion
                self.num_columna += 4
                lista = lista[4:]
                puntero = 0
            elif char == '\n':
                lista = lista[1:]
                puntero = 0 
                self.num_linea += 1
                self.num_columna = 1

            elif char == ' ' or char == '\r' or char == '{' or char == '}' or char == ',' or char == ':' or char == '.':
                lista = lista[1:]
                self.num_columna += 1
                puntero = 0
            else:
                lista = lista[1:]
                puntero = 0
                self.num_columna += 1
                lista_errores.append(Lexema_errores(contador,"Error lexico",char,self.num_linea,self.num_columna))
                contador += 1
        
        return lista_lexa
    

    def archivo_salida(self):
        global lista_errores
        lista_temporal = {}
        lista_temporal["Errores"] = []

        for lista_error in lista_errores:
            lista_temporal["Errores"].append({
                'No.' : lista_error.num,
                'descripcion' : {
                    'lexema' : lista_error.lexema,
                    'tipo' : lista_error.tipo,
                    'columna': lista_error.columna,
                    'fila' : lista_error.fila
                }
            })

        
        with open('RESULTADOS_202202182.json', 'w') as file:
            json.dump(lista_temporal,file, indent=4)
    
    def coleccionar_lexema(self, lista):
        global linea
        global columna
        global lista_lexa
        lexema = ''
        cabeza = ''
        for char in lista:
            cabeza += char
            if char == '\"':
                return lexema, lista[len(cabeza):]
            else:
                lexema += char
        return None,None

    def verificar_errores(self):
        global lista_errores
        for errores in lista_errores:
            print(errores)


    def fomar_numero(self, lista):
        num = ''
        puntero = ''
        decimal  = False
        for char in lista:
            puntero += char
            if char == '.':
                decimal = True
            if char == '"' or char == ' ' or char == '\n' or char == '\t' or char == ',':
                if decimal:
                    return float(num),lista[len(puntero)-1:]
                else:
                    return int(num), lista[len(puntero)-1:]
            else:
                num += char
        return None,None
    
    def operar(self):
        global lista_lexa
        global instrucciones
        operacion = ''
        num1 = '' 
        num2 = ''
        while lista_lexa:
            Lexema = lista_lexa.pop(0)
            if Lexema.operacion(None) == 'operacion':
                operacion = lista_lexa.pop(0)
            elif Lexema.operacion(None) == 'valor1':
                num1 = lista_lexa.pop(0)
                if num1.operacion(None) == '[':
                    num1 = self.operar()
            elif Lexema.operacion(None) == 'valor2':
                num2 = lista_lexa.pop(0)
                if num2.operacion(None) == '[':
                    num2 = self.operar()

            #obtener las configuraciones
            if Lexema.operacion(None) == 'texto':
                self.text = lista_lexa.pop(0)


            if Lexema.operacion(None) == 'fondo':
                self.fondo = lista_lexa.pop(0)


            if Lexema.operacion(None) == 'fuente':
                self.fuen = lista_lexa.pop(0)


            if Lexema.operacion(None) == 'forma':
                self.form = lista_lexa.pop(0)


            if operacion and num1 and num2:
                return Opera_aritm(num1,num2,operacion, f'Inicio: {operacion.obtener_fila()}:{operacion.obtener_columna()}' , f'Fin: {num2.obtener_fila()}:{num2.obtener_columna()} ')
            
            elif operacion and num1 and operacion.operacion(None) == ('seno' or 'coseno' or 'tangente'):
                return Opera_trigono(num1, operacion, f'Inicio: {operacion.obtener_fila()}:{operacion.obtener_columna()}', f'Fin: {num1.obtener_fila()}:{num1.obtener_columna()}')
        return None

    def graficar(self):
        global instrucciones

        text = """digraph G {
                    label=" """+self.text.lexema+""""
                    rankdir="LR"
                    node[style=filled, color=" """+self.fondo.lexema+"""", fontcolor=" """+self.fuen.lexema+"""", shape="""+self.form.lexema+"""]"""

        for i in range(len(instrucciones)):
            
            text += self.unir_nodos_de_graficar(instrucciones[i], i, 0,'')
            

        text += "\n}"
        f = open('bb.dot', 'w')

        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o REPORTE_202202182.png')

    
    def unir_nodos_de_graficar(self, tipo, numero, codigo, barra):
        valor = ""
        if tipo:
            if type(tipo) == Numero:
                valor += f'nodo{numero}{codigo}{barra}[label="{tipo.operacion(None)}"];\n'
            if type(tipo) == Opera_aritm:
                valor += f'nodo{numero}{codigo}{barra}[label="{tipo.tipo.lexema}\\n{tipo.operacion(None)}"];\n'
                valor += self.unir_nodos_de_graficar(tipo.left ,numero, codigo+1, barra+"_left")
                valor += f'nodo{numero}{codigo}{barra} -> nodo{numero}{codigo+1}{barra}_left;\n'
                valor += self.unir_nodos_de_graficar(tipo.right,numero, codigo+1, barra+"_right")
                valor += f'nodo{numero}{codigo}{barra} -> nodo{numero}{codigo+1}{barra}_right;\n'
            
            if type(tipo) == Opera_trigono:
                valor += f'nodo{numero}{codigo}{barra}[label="{tipo.tipo.lexema}\\n{tipo.operacion(None)}"];\n'
                valor += self.unir_nodos_de_graficar(tipo.left,numero, codigo+1, barra+"_tri")
                valor += f'nodo{numero}{codigo}{barra} -> nodo{numero}{codigo+1}{barra}_tri;\n'
        return valor

    def recursividad_operar(self):
        global instrucciones

        while True:
            operacion = self.operar()
            if operacion:
                instrucciones.append(operacion)
            else:
                break
        
        return instrucciones


    def limpiar_listas(self):
        lista_lexa.clear()
        lista_errores.clear()
        instrucciones.clear()
        self.num_columna = 1
        self.num_linea = 1
