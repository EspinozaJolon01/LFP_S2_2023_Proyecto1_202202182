import tkinter as tk
from tkinter import Menu, filedialog, messagebox, ttk
from analizador import analizador
import json

lista_analizado = analizador()
# Variable global para almacenar el contenido
contenido = None
archivo1 = ""
cursor_label = None
lista_lexmas = []

def leet_json():
    global archivo1
    archivo1 = filedialog.askopenfilename(filetypes=[("Archivo JSON", "*.json")])
    if archivo1:
        with open(archivo1, 'r') as file:
            contenido_json = json.load(file)
            contenido.delete("1.0", tk.END)
            contenido.insert("1.0", json.dumps(contenido_json, indent=4))
        
    lista_lexmas.append(contenido_json)
    print(archivo1)

def guardar_archivo():
    global contenido, archivo1
    if contenido and archivo1:
        try:
            with open(archivo1, "w") as f:
                f.write(contenido.get("1.0", tk.END))
            messagebox.showinfo("Exito","Guardado exitosamente en ")
        except Exception as e:
            messagebox.showerror("Error","Error al guardar: " + str(e))

def guardar_como_archivo():
    global contenido
    if contenido:
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo JSON", "*.json")])
        if archivo:
            with open(archivo, "w") as f:
                f.write(contenido.get("1.0", tk.END))

def analizar_archivo():
    lista_analizado.imprimir_lista(lista_lexmas)

def errores():
    print("Errores")

def reporte():
    print("reporte")

def actualizar_cursor_label(event):
    cursor_pos = contenido.index(tk.CURRENT)
    fila, columna = map(int, cursor_pos.split('.'))
    cursor_label.config(text=f"Fila: {fila}, Columna: {columna}")

def salir():
    root.destroy()

root = tk.Tk()
root.title("Editor de Texto")
root.attributes('-fullscreen', True)  # para abrir en toda la pantalla

root.configure(bg="#e2e8f3")

menubar = Menu(root) 

archivo_menu = Menu(menubar, tearoff=0)
archivo_menu.add_command(label="Abrir", command=leet_json)
archivo_menu.add_command(label="Guardar", command=guardar_archivo)
archivo_menu.add_command(label="Guardar como", command=guardar_como_archivo)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=salir)

archivo_menu1 = Menu(menubar, tearoff=0)
archivo_menu1.add_command(label="analizar", command=analizar_archivo)

archivo_menu2 = Menu(menubar, tearoff=0)
archivo_menu2.add_command(label="errores", command=errores)

archivo_menu3 = Menu(menubar, tearoff=0)
archivo_menu3.add_command(label="reporte", command=reporte)

menubar.add_cascade(label="Archivo", menu=archivo_menu)
menubar.add_cascade(label="Analizar", menu=archivo_menu1)
menubar.add_cascade(label="Errores", menu=archivo_menu2)
menubar.add_cascade(label="Reporte", menu=archivo_menu3)

root.config(menu=menubar)

# Crear el widget Text para el contenido y ajustar su tamaño y ubicación
contenido = tk.Text(root, width=200, height=60)  # Ajusta el ancho y alto según tus preferencias
contenido.place(relx=0.5, rely=0.5, anchor="center")

# Agregar una etiqueta para mostrar la posición del cursor
cursor_label = tk.Label(root, text="", bg="#e2e8f3")
cursor_label.place(relx=0.01, rely=0.01)

# Asociar el evento de movimiento del mouse al widget Text
contenido.bind("<Motion>", actualizar_cursor_label)

root.mainloop()


