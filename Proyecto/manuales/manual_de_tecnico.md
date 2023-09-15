# MANUAL TECNICO 

## José Luis Espinoza Jolón - 202202182

### Caracteristicas del proyecto 

- Se puede analizar un archivo Json
- Podra mostrar los Errores lexicos que contenga el Json
- Motrar las operaciones correctas
- Se podra generar una grafica de las operaciones

### Clase app.py

Es la función donde se crea la interfaz grafica.

```python
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.path = None
        self.Analizar = analizador()
        

        self.linea_numero = tk.Text(root, width=4, padx=4, takefocus=0, border=0, background='#5FA0E0', state='disabled')
        self.linea_numero.pack(side=tk.LEFT, fill=tk.Y)

        self.widget = ScrolledText(self.root, wrap=tk.WORD)
        self.widget=ScrolledText(root,width=150,height=50)
        self.widget.pack(expand=True, fill='both')
        # self.widget.pack(side=tk.TOP, fill=tk.Y)

        self.widget.bind('<Key>', self.acutualizar_linea_num)
        self.widget.bind('<MouseWheel>', self.acutualizar_linea_num)

        self.conteo_linea = 1

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.leer_xml)
        self.file_menu.add_command(label="Guardar", command=self.guardar)
        self.file_menu.add_command(label="Guardar Como", command=self.guardar_como)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)
        
        self.menu_bar.add_cascade(label="Analizar", command=self.analizar_lexema)
        self.menu_bar.add_cascade(label="Errores", command=self.errores_lexemas)
        self.menu_bar.add_cascade(label="Reporte", command=self.generar_graficas)

```
####  Funcion leer_json

Esta funcion realiza la accion de poder leer nuestro archivo json.

```python
    def leer_xml(self):
        global contenido_json
        self.Analizar.limpiar_listas()
        path = filedialog.askopenfilename(filetypes=[("Archivos json", "*.json")])
        self.path = path 
        if path:
            with open(path, 'r') as file:
                contenido_json = file.read()
                self.widget.delete(1.0, tk.END)
                self.widget.insert(tk.END, contenido_json)
            self.acutualizar_linea_num()

```

####  Funcion guardar

Esta funcion realiza la accion de poder guarda alguna modificacion realiza en nuestro documento.

```python
    def guardar(self):
        # path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos", "*.json")])
        global contenido_json
        path = self.path
        if path:
            contenido_json = self.widget.get(1.0, tk.END)
            with open(path, 'w') as file:
                file.write(contenido_json)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")
```

####  Funcion guardar_como

Esta funcion realiza la acción de poder guarda alguna modificacion realiza en nuestro documento, con cualquier nombre.

```python
    def guardar_como(self):
        global contenido_json
        path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos", "*.json")])
        if path:
            contenido_json = self.widget.get(1.0, tk.END)
            with open(path, 'w+') as file:
                file.write(contenido_json)
            messagebox.showinfo("Guardado", "Archivo guardado exitosamente.")
```

####  Funcion acutualizar_linea_num

Esta función actualiza las lineas en la vista.

```python
    def acutualizar_linea_num(self, event=None):
        conteo = self.widget.get('1.0', tk.END).count('\n')
        if conteo != self.conteo_linea:
            self.linea_numero.config(state=tk.NORMAL)
            self.linea_numero.delete(1.0, tk.END)
            for line in range(1, conteo + 1):
                self.linea_numero.insert(tk.END, f"{line}\n")
            self.linea_numero.config(state=tk.DISABLED)
            self.conteo_linea = conteo
```

####  Función analizar_lexema

Esta función va analizar el json("Mas adelante se dara la explicación mas detallada"), y se mostrarar una mensaje de las operaciones correctas.

```python
    def analizar_lexema(self):
        try:
            global contenido_json
            self.Analizar.limpiar_listas()
            self.Analizar.insutrucciones_lexam(contenido_json)
            resultados =  self.Analizar.recursividad_operar()
            resultados_as_string = ""
            Opercion = 1


            for resultado in resultados:
                if isinstance(resultado.operacion(None), int) or isinstance(resultado.operacion(None),float) == True:
                    resultados_as_string += str(f"Operacion: {Opercion} > {resultado.tipo.operacion(None)} = {resultado.operacion(None)}") + "\n"
                    Opercion += 1
                # resultados_as_string += str(resultado.operacion(None)) + "\n"
                # print(resultado.operar(None))
            messagebox.showinfo("Resultados",resultados_as_string)


        
        except:
            messagebox.showinfo("Error","no se ha ingresado ningun archivo")
```

####  Función errores_lexemas

Esta función va analizar los errores y se genera un archivo json de salida, con dicho errores.

```python
    def errores_lexemas(self):
        try:
            messagebox.showinfo("Generado","Se genero correctamente el archivo json")
            self.Analizar.archivo_salida()
        
        except:
            messagebox.showinfo("Error","no se ha ingresado ningun archivo")
```

####  Función generar_graficas

Esta función va analizar generar grafica de las operaciones correcta y con sus resultados

```python
    def generar_graficas(self):
        try:
            messagebox.showinfo("Generado","Se genero correctamente la grafica")
            self.Analizar.graficar()
        
        except:
             messagebox.showinfo("Error","no se ha ingresado ningun archivo")
```

### Clase analizador

####  Función insutrucciones_lexam

Esta funcion obtiene el json como un parametro, para arma los lexemas y se realiza la opcion de guardar los errores lexicos obtenidos del Json


```python
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
```

####  Función coleccionar_lexema

Esta función obtiene un argumento, json donde va iterar caracter por caracter para formar las palabras.

```python
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
```

####  Función fomar_numero

Esta función obtiene un argumento json, donde va iterar caracter para formar los numeros y separarlo en float e int.

```python
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
```

####  Función operar

Esta función va realizar las operaciones dependiendo si son aritmeticas o trigonometricas y tambien obtenemos los datos para nuestra graficar.

```python
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
```

####  Función recursividad_operar

Esta función realizar la recursividad para las operaciones, si contiene operaciones anidadas.

```python
    def recursividad_operar(self):
        global instrucciones

        while True:
            operacion = self.operar()
            if operacion:
                instrucciones.append(operacion)
            else:
                break
        
        return instrucciones
```

####  Función limpiar_listas

Esta función es para limpiar nuestras listas usadas.

```python
    def limpiar_listas(self):
        lista_lexa.clear()
        lista_errores.clear()
        instrucciones.clear()
        self.num_columna = 1
        self.num_linea = 1
```

####  Función archivo_salida

Esta función generar el archivo json.

```python
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
```
####  Función graficar

Esta función generar la grafica.

```python
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
```
####  Función unir_nodos_de_graficar

Esta función une los nodos para formar las graficas y se vayan relacionando.

```python
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
```


### Clase abstract_num

funcion donde realizamos nuestro constructor que obtiene fila, columnas, hereadamos para las demas clases, lo cuales contiene lo siguiente metodos.

```python
    def __init__(self,fila,columna):
        self.fila = fila
        self.columna = columna

    @abstractmethod
    def operacion(self, arbol):
        pass


    @abstractmethod
    def obtener_fila(self):
        return self.fila

    @abstractmethod
    def obtener_columna(self):
        return self.columna

```

### Clase Lexema_errores

funcion donde realizamos nuestro constructor que obtiene num,tipo,lexema, fila, columna,  realizar nuestro errores lexicos

```python

    def __init__(self,num,tipo,lexema, fila, columna):
        self.num = num
        self.tipo = tipo
        self.lexema = lexema
        super().__init__(fila, columna)

    def operacion(self, arbol):
        return self.lexema
    
    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()
```

### Clase Numero

funcion donde realizamos nuestro constructor que obtiene valor, fila, columna,  realizar los valores numericos

```python

   def __init__(self,valor, fila, columna):
        self.valor = valor

        super().__init__(fila, columna)

    def operacion(self, arbol):
        return self.valor


    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()
```

### Clase Opera_aritm

Función operar donde ralizamos las operaciones aritmeticas y se devuelve el valor. 
```python

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
            return round(left_values + right_values,2)
        elif self.tipo.operacion(arbol) == 'resta':
            return round(left_values - right_values,2)
        elif self.tipo.operacion(arbol) == 'multiplicacion':
            return round(left_values * right_values,2)
        elif self.tipo.operacion(arbol) == 'division':
            return round(left_values / right_values,2)
        elif self.tipo.operacion(arbol) == 'modulo':
            return round(left_values % right_values,2)
        elif self.tipo.operacion(arbol) == 'potencia':
            return round(left_values ** right_values,2)
        elif self.tipo.operacion(arbol) == 'raiz':
            return round(left_values ** (1/right_values),2)
        elif self.tipo.operacion(arbol) == 'inverso':
            return round(1/right_values, 2)
        else:
            return 0
        
    def obtener_fila(self):
        return super().obtener_fila()
    
    def obtener_columna(self):
        return super().obtener_columna()

```

### Clase Opera_trigono

Función operar donde ralizamos las operaciones trigonometrico y se devuelve el valor. 
```python

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

```

