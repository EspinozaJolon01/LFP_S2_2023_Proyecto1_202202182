
class analizador:


    global linea 
    global columna
    global instru
    global lista_lexa
    
    lista_lexa = []

    def __init__(self) :
            
        self.num_linea = 1 
        self.num_columna = 1


    reversed = {
        'OPERACIONES' : 'operacion',
        'SUMA' : 'suma',
        'RESTA': 'resta',
        'MULTIPLICACIÓN' : 'multiplicacion',
        'DIVISIÓN' : 'division',
        'POTENCIA' : 'potencias',
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

                    lista_lexa.append(lexema)
                    self.num_columna += len(lexema) + 1
                    puntero = 0
            elif char.isdigit():
                token, lista = self.fomar_numero(lista)
                if token and lista:
                    self.num_columna += 1
                    lista_lexa.append(token)
                    self.num_columna += len(str(token)) + 1
                    puntero = 0
            elif char == '[' or char == ']':
                lista_lexa.append(char)
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
                self.num_columna += 1
            else:
                lista = lista[1:]
                puntero = 0
                self.num_columna += 1
            
        for lexema in lista_lexa:
            print(lexema)
    
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

    def imprimir_lista(self, lista):
        if lista is not None:
            for elemento in lista:
                print(elemento)
        else:
            print("La lista es None")


entrada = '''{
    "operaciones": [
        {
            "operacion": "restas",
            "valor1": 4.5,
            "valor2": 5.32,
            "valor3": 5.32
        },
        {
            "operacion": "resta",
            "valor1": 4.5,
            "valor2": [
                {
                    "operaciones": "potencias",
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
            "operaciones": "multiplicacion",
            "valor1": 7,
            "valor2": 3
        },
        {
            "operaciones": "division",
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

app = analizador()

app.insutrucciones_lexam(entrada)