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
        self.texto = ''
        self.fondo = ''
        self.fuente = ''
        self.forma = ''
            
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
        'TEXTO' : 'Operaciones',
        'FONDO' : 'azul',
        'FUENTE' :'blanco',
        'Textos' : 'textos',
        'Fondo' : 'fondo',
        'Fuente' : 'fuente',
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
            
        # for lexema in lista_lexa:
        #     print(lexema)
        # print("----------------")
        # for erroes in lista_errores:
        #     print(erroes)
        # print("--------------------")
        # for error in lista_errores:
        #     print("Error encontrado: num: {} error: {}, Lexema: {}, Fila: {}, Columna: {}".format(
        #         error.num, error.tipo, error.lexema, error.obtener_fila(), error.obtener_columna()))
        # print("--------------------")
        
        
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
                self.texto = lista_lexa.pop(0)


            if Lexema.operacion(None) == 'fondo':
                self.fondo = lista_lexa.pop(0)


            if Lexema.operacion(None) == 'fuente':
                self.fuente = lista_lexa.pop(0)


            if Lexema.operacion(None) == 'forma':
                self.forma = lista_lexa.pop(0)


            if operacion and num1 and num2:
                return Opera_aritm(num1,num2,operacion, f'Inicio: {operacion.obtener_fila()}:{operacion.obtener_columna()}' , f'Fin: {num2.obtener_fila()}:{num2.obtener_columna()} ')
            
            elif operacion and num1 and operacion.operacion(None) == ('seno' or 'coseno' or 'tangente'):
                return Opera_trigono(num1, operacion, f'Inicio: {operacion.obtener_fila()}:{operacion.obtener_columna()}', f'Fin: {num1.obtener_fila()}:{num1.obtener_columna()}')
        return None

    def graficar(self):
        global instrucciones

        texto = """digraph G {
                    label=" """+self.texto.lexema+""""
                    rankdir="LR"
                    
                    node[style=filled, color=" """+self.fondo.lexema+"""", fontcolor=" """+self.fuente.lexema+"""", shape="""+self.forma.lexema+"""]"""

        for i in range(len(instrucciones)):
            
            texto += self.unir_nodos_de_graficar(instrucciones[i], i, 0,'')
            

        texto += "\n}"
        f = open('bb.dot', 'w')

        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o REPORTE_202202182.png')

    
    def unir_nodos_de_graficar(self, tipo, num, clave, separador):
        datos = ""

        if tipo:
            if type(tipo) == Numero:
                
                datos += f'nodo{num}{clave}{separador}[label="{tipo.operacion(None)}"];\n'


            if type(tipo) == Opera_aritm:
                datos += f'nodo{num}{clave}{separador}[label="{tipo.tipo.lexema}\\n{tipo.operacion(None)}"];\n'

                datos += self.unir_nodos_de_graficar(tipo.left ,num, clave+1, separador+"_left")

                datos += f'nodo{num}{clave}{separador} -> nodo{num}{clave+1}{separador}_left;\n'

                datos += self.unir_nodos_de_graficar(tipo.right,num, clave+1, separador+"_right")

                datos += f'nodo{num}{clave}{separador} -> nodo{num}{clave+1}{separador}_right;\n'
            
            if type(tipo) == Opera_trigono:
                
                datos += f'nodo{num}{clave}{separador}[label="{tipo.tipo.lexema}\\n{tipo.operacion(None)}"];\n'

                datos += self.unir_nodos_de_graficar(tipo.left,num, clave+1, separador+"_tri")

                datos += f'nodo{num}{clave}{separador} -> nodo{num}{clave+1}{separador}_tri;\n'


        return datos

    def recursividad_operar(self):
        global instrucciones

        while True:
            operacion = self.operar()
            if operacion:
                instrucciones.append(operacion)
            else:
                break
        
        # for instruccion in instrucciones:
        #     print("===========resultado===========")
        #     print(instruccion.operacion(None))

        return instrucciones


    def limpiar_listas(self):
        lista_lexa.clear()
        lista_errores.clear()
        instrucciones.clear()
        self.num_columna = 1
        self.num_linea = 1


entrada = '''{
    "operaciones": [
        {
            "operacion": "restaQ",
            "valor1": 4.5,
            "valor2": 5.32
        },
        {
            "operacion": "resta",
            "valor1": 4.5,
            "valor2": [
                {
                    "operacion": "potencia",
                    "valor1": 10,
                    "valor2": 3
                }
            ]
        },
        {
            "operacion": "suma",
            "valor1": [
                {
                    "operacion": "seno",
                    "valor1": 90
                }
            ],
            "valor2": 5.32
        },
        {
            "operacion": "multiplicacion",
            "valor1": 7,
            "valor2": 3
        },
        {
            "operacion": "division",
            "valor1": 15,
            "valor2": 3
        }
    ],
    "configuraciones": [
        {
            "textos": "Operaciones",
            "fondo": "azul",
            "fuente": "blanco",
            "forma": "circulo"
        }
    ]
}'''

# app = analizador()

# app.insutrucciones_lexam(entrada)
# app.recursividad_operar()