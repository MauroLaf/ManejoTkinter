import tkinter as tk  # 1.0 - Renombro la librería tkinter
from tkinter import ttk  # 1.1 - Mejora de componentes de tkinter

# 2.0 - Creamos Ventana
ventana = tk.Tk()
ventana.geometry('600x400')  # 2.1 - Tamaño en px
ventana.title('Nueva Ventana')  # 2.2 - Título de la ventana
ventana.configure(background='#1d2d44')  # 2.3 - Fondo

# 3.0 - Manejo de grid (rejilla o cuadrícula)
boton1 = ttk.Button(ventana, text='Boton1')
boton2 = ttk.Button(ventana, text='Boton2')
boton3 = ttk.Button(ventana, text='Boton3')

# 4.0 - Configurar el grid para columnas (ocupan espacio en relación con las demás)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

# 5.0 - Configurar el grid para filas (rows)
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)

# 6.0 - Publicando de manera horizontal componentes
# 6.1 - Llamo al método grid
boton1.grid(row=0, column=0, sticky=tk.NSEW, padx=20, pady=20)  # 6.1.1 - Uso sticky para mover el botón en coordenadas 'N,S,E,W'
boton2.grid(row=0, column=1, sticky=tk.SE, ipadx=20, ipady=20)  # 6.1.2 - Con ipady o ipadx agregamos márgenes internos
boton3.grid(row=0, column=2, sticky=tk.NW)

# 7.0 - Publicando de manera vertical componentes (descomentar si se desea)
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)

# 8.0 - Publicando de manera diagonal componentes (descomentar si se desea)
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=1)
# boton3.grid(row=2, column=2)

# 9.0 - Hacemos visible la ventana
ventana.mainloop()
