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

# 6.0 - Métodos para ejecutar con botón
def saludar():
    print('Saludos desde el botón')  # 6.1 - Método para saludo sin parámetros

# 7.0 - Método con parámetro
def saludar_usuario(nombre):
    print(f'Saludos {nombre}')  # 7.1 - Método que recibe parámetro 'nombre'

# 8.0 - Botones
boton1 = ttk.Button(ventana, text='Enviar', command=saludar)  # 8.1 - Botón que ejecuta el saludo básico
boton2 = ttk.Button(ventana, text='Enviar', command=lambda: saludar_usuario('Juan'))  # 8.2 - Botón que ejecuta el saludo con parámetro
boton1.pack(pady=20)  # 8.3 - Publicamos el primer botón con separación vertical
boton2.pack(pady=20)  # 8.4 - Publicamos el segundo botón con separación vertical

# 9.0 - Hacemos visible la ventana
ventana.mainloop()  # 9.1 - Ejecutamos el ciclo principal de la ventana
