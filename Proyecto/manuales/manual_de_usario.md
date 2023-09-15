# Manual de usuario

## Descripcion 

Se solicita la lectura de código fuente, el cual tendrá un formato JSON, creando un
programa el cual sea capaz de identificar un lenguaje dado, identificando los errores
léxicos y ejecutando las instrucciones correspondientes.

### paso 1

Al iniciar el programa se podra ver la siguiente interfaz

![Pantalla de inicio](/Proyecto/imagenes/img1.png)

1. Archivo 

El usuario tendra tendra 4 opciones para ejecutar.

- abrir:  donde podra escoger el archivo json 

![Pantalla de inicio](/Proyecto/imagenes/img2.png)

ya escogido el archivo, se mostrar la vista de la siguiente manera.

![Pantalla de inicio](/Proyecto/imagenes/img3.png)

- guardar:  donde podra guardar el archivo ejecutado.

- guardar como:  donde puede guardar el archivo con otro nombre y en otro carpeta.

- salir:  para cerrar el programa

2. Analizar 

El usaurio al darle clik, obtendra las operaciones realizadas correctamente. 

![Pantalla de inicio](/Proyecto/imagenes/img4.png)

A. el mensaje con las operaciones realizadas


3. Errores

El usuario al darle clik, obtendra el archivo de salida en json con los errores lexicos encontrado en el documento.

![Pantalla de inicio](/Proyecto/imagenes/img5.png)

#### Archivo json

De esta forma se mostrar al usario el archivo.

```python

{
    "Errores": [
        {
            "No.": 1,
            "descripcion": {
                "lexema": "*",
                "tipo": "Error lexico",
                "columna": 4,
                "fila": 1
            }
        },
        {
            "No.": 2,
            "descripcion": {
                "lexema": "*",
                "tipo": "Error lexico",
                "columna": 12,
                "fila": 19
            }
        },
        {
            "No.": 3,
            "descripcion": {
                "lexema": "*",
                "tipo": "Error lexico",
                "columna": 13,
                "fila": 19
            }
        }
    ]
}

```

4. grafica

El usuario al darle clik, obtendra la grafica con las operaciones realizadas. 

![Pantalla de inicio](/Proyecto/imagenes/img6.png)


- De esta forma le mostrar la imagen al usuario.


![Pantalla de inicio](/Proyecto/imagenes/img7.png)
