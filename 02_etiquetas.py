import tkinter as tk  # 1.0 - Renombro la librería tkinter
from tkinter import ttk  # 1.1 - Mejora de componentes de tkinter

# 2.0 - Creamos un objeto de tipo ventana, llamando a la clase Tk
ventana = tk.Tk()

# 3.0 - Redimensionar la ventana
ventana.geometry('600x400')  # 3.1 - Tamaño en px

# 4.0 - Modificar el título
ventana.title('Nueva Ventana')  # 4.1 - Establecemos el título de la ventana

# 5.0 - Color de la ventana
ventana.configure(background='#1d2d44')  # 5.1 - Cambiamos el color de fondo de la ventana

# 6.0 - Creamos una etiqueta (label)
etiqueta = tk.Label(ventana, text='Saludos')  # 6.1 - Creamos un componente etiqueta y configuramos el texto inicial

# 7.0 - Cambiar el texto usando el método configure
etiqueta.configure(text='Nos vemos...')  # 7.1 - Cambiamos el texto de la etiqueta mediante el método configure

# 8.0 - Cambiar el texto con ayuda de la llave text
etiqueta['text'] = 'Adios'  # 8.1 - Modificamos el texto de la etiqueta directamente

# 9.0 - Publicamos el componente
etiqueta.pack(pady=20)  # 9.1 - Empaquetamos el componente etiqueta y lo mostramos en la ventana, con separación vertical

# 10.0 - Hacemos visible la ventana
ventana.mainloop()  # 10.1 - Ejecutamos el ciclo principal de la ventana
