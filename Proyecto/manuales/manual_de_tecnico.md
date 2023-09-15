# MANUAL TECNICO 

## José Luis Espinoza Jolón - 202202182

### Caracteristicas del proyecto 

- Se puede analizar un archivo Json
- Podra mostrar los Errores lexicos que contenga el Json
- Motrar las operaciones correctas
- Se podra generar una grafica de las operaciones

### app.py

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
### Funcion leer_json

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

### Funcion guardar

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

### Funcion guardar_como

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

### Funcion acutualizar_linea_num

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

### Función analizar_lexema

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

### Función errores_lexemas

Esta función va analizar los errores y se genera un archivo json de salida, con dicho errores.

```python
    def errores_lexemas(self):
        try:
            messagebox.showinfo("Generado","Se genero correctamente el archivo json")
            self.Analizar.archivo_salida()
        
        except:
            messagebox.showinfo("Error","no se ha ingresado ningun archivo")
```

### Función generar_graficas

Esta función va analizar generar grafica de las operaciones correcta y con sus resultados

```python
    def generar_graficas(self):
        try:
            messagebox.showinfo("Generado","Se genero correctamente la grafica")
            self.Analizar.graficar()
        
        except:
             messagebox.showinfo("Error","no se ha ingresado ningun archivo")
```

## Clase analizador


