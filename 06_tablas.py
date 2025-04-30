import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# 1.0 - Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')  # 1.1 - Establecemos tamaño
ventana.configure(background='#1d2d44')  # 1.2 - Fondo
ventana.title('Manejo de Tabla')  # 1.3 - Título de la ventana

# 2.0 - Configurar el grid
ventana.columnconfigure(0, weight=1)  # 2.1 - Para centrar su contenido
ventana.columnconfigure(1, weight=0)  # 2.2 - Agrego columna para el scroll con peso 0

# 3.0 - Definir un estilo
estilos = ttk.Style()
estilos.theme_use('clam')  # 3.1 - Prepara el manejo del tema oscuro
estilos.configure('Treeview', background='black', foreground='white',
                  fieldbackground='black', rowheight=30)  # 3.2 - Estilo general
estilos.map('Treeview', background=[('selected','#3a86ff')])  # 3.3 - Color de selección

# 4.0 - Definir las columnas
columnas = ('Id', 'Nombre', 'Edad')
tabla = ttk.Treeview(ventana, columns=columnas, show='headings')  # 4.1 - Creamos el componente de tabla. Ponemos un show porque la 1º columna se usa como treeviews que muestran subregistros o más información

# 5.0 - Cabeceros de la tabla
tabla.heading('Id', text='Id', anchor=tk.CENTER)
tabla.heading('Nombre', text='Nombre', anchor=tk.CENTER)
tabla.heading('Edad', text='Edad', anchor=tk.CENTER)

# 6.0 - Formato de columna
tabla.column('Id', width=80)
tabla.column('Nombre', width=120)
tabla.column('Edad', width=120)

# 7.0 - Cargar datos a la tabla
datos = ((1,'Alejandra',25), (2,'Matias',32))  # 7.1 - Definimos como tuplas
for persona in datos:
    tabla.insert(parent='', index=tk.END, values=persona)  # 7.2 - parent es el registro padre que estará vacío y para agregar registros uno a otro se usa END

# 8.0 - Agregamos un scrollbar
scrollbar = ttk.Scrollbar(ventana, orient=tk.VERTICAL, command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)  # 8.1 - Sincronizamos los componentes con set
scrollbar.grid(row=0, column=1, sticky=tk.NS)

# 9.0 - Definimos método mostrar registro seleccionado
def mostrar_registro_seleccionado(event):
    print('Ejecutando metodo mostrar_registro_seleccionado')
    elemento_seleccionado = tabla.selection()[0]  # 9.1 - Solo procesamos el primer registro seleccionado
    elemento = tabla.item(elemento_seleccionado)  # 9.2 - Obtenemos el item/elemento
    persona = elemento['values']  # 9.3 - Tupla que almacena datos de persona definidos más arriba
    print(persona)
    showinfo(title='Persona Seleccionado', message=f'Persona: {persona}')

# 10.0 - Asociar el evento select de la tabla
tabla.bind('<<TreeviewSelect>>', mostrar_registro_seleccionado)

# 11.0 - Publicamos la tabla
tabla.grid(row=0,column=0, sticky=tk.NSEW)

# 12.0 - Ejecutamos ventana
ventana.mainloop()