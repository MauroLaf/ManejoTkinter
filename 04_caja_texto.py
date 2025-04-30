import tkinter as tk  # 1.0 - Renombro la librería tkinter
from tkinter import ttk  # 1.1 - Mejora de componentes de tkinter

# 2.0 - Creamos Ventana
ventana = tk.Tk()
ventana.geometry('600x400')  # 2.1 - Tamaño en px
ventana.title('Nueva Ventana')  # 2.2 - Título de la ventana
ventana.configure(background='#1d2d44')  # 2.3 - Fondo

# 3.0 - Método para el botón
def mostrar():
    texto = caja_texto.get()  # 3.1 - Recuperamos el valor de la textbox
    print(f'Texto proporcionado: {texto}')
    etiqueta['text'] = texto  # 3.2 - Asignamos el texto a la etiqueta

# 4.0 - Caja de texto
caja_texto = ttk.Entry(ventana, font=('Arial', 15))  # 4.1 - Componente textEntry
caja_texto.pack(pady=20)  # 4.2 - Publicamos con separación vertical

# 5.0 - Agregar un botón
boton = ttk.Button(ventana, text='Enviar', command=mostrar)  # 5.1 - Asocia el botón con la función
boton.pack(pady=20)  # 5.2 - Publicamos el botón

# 6.0 - Agregamos una etiqueta
etiqueta = ttk.Label(ventana, text='Valor Inicial')  # 6.1 - Creamos etiqueta con texto por defecto
etiqueta.pack(pady=20)  # 6.2 - Publicamos la etiqueta

# 7.0 - Hacemos visible la ventana
ventana.mainloop()
