from opera_aritm import Opera_aritm
from opera_trigono import Opera_trigono
from lexema import Lexema
from numero import Numero
from abstract_num import Abstract_num



class analizador:


    global linea 
    global columna
    global instrucciones
    global lista_lexa
    
    lista_lexa = []
    instrucciones = []

    def __init__(self) :
            
        self.num_linea = 1 
        self.num_columna = 1


    reversed = {
        'OPERACIONES' : 'operaciones',
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
        'TEXTO' : 'texto',
        'FONDO' : 'fondo',
        'FUENTE' :'fuente',
        'FORMA' : 'forma',
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
        lexema = ''
        
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
            else:
                lista = lista[1:]
                puntero = 0
                self.num_columna += 1
            
        #for lexema in lista_lexa:
        #    print(lexema)
        
        return lista_lexa
    
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

            if operacion and num1 and num2:
                return Opera_aritm(num1,num2,operacion, f'Inicio: {operacion.obtener_fila()}:{operacion.obtener_columna()}' , f'Fin: {num2.obtener_fila()}:{num2.obtener_columna()} ')
            
            elif operacion and num1 and operacion.operacion(None) == ('seno' or 'coseno' or 'tangente'):
                return Opera_trigono(num1, operacion, f'Inicio: {operacion.obtener_fila()}:{operacion.obtener_columna()}', f'Fin: {num1.obtener_fila()}:{num1.obtener_columna()}')
        return None

    def recursividad_operar(self):
        global instrucciones

        while True:
            operacion = self.operar()
            if operacion:
                instrucciones.append(operacion)
            else:
                break
        
        #for instruccion in instrucciones:
        #    print("===========resultado===========")
        #    print(instruccion.operacion(None))
        #    print("--------------fila--------------")
        #    print(instruccion.obtener_fila())
        #    print("--------------columna--------------")
        #    print(instruccion.obtener_columna())
        return instrucciones

    def imprimir_lista(self, lista):
        if lista is not None:
            for elemento in lista:
                print(elemento)
        else:
            print("La lista es None")


entrada = '''{
    "operaciones": [
        {
            "operacion": "suma$",
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
            "textos": "Opercaiones",
            "fondo": "azul",
            "fuente": "blanco",
            "forma": "circulo"
        }
    ]
}'''

#app = analizador()

#app.insutrucciones_lexam(entrada)
#app.recursividad_operar()