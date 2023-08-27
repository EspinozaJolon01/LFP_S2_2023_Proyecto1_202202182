from tkinter import *

ventana = Tk()

menu = Menu(ventana)
ventana.config(menu=menu)

file_menu = Menu(menu, tearoff=0)   #tearoff no mustra una linea de abajo
file_menu.add_command(label="New proyect")
file_menu.add_command(label="New proyect")


edit_menu = Menu(menu,tearoff=0)
edit_menu.add_command(label="New proyect")


help_menu = Menu(menu,tearoff=0)
help_menu.add_command(label="New proyect")

menu.add_cascade(label="File", menu=file_menu)  
menu.add_cascade(label="Edit", menu=edit_menu) 
menu.add_cascade(label="Help", menu=help_menu)  

ventana.mainloop()


