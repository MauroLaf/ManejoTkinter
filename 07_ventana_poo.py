import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# 1.0 - Defino clase App que hereda de tk.Tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()  # 1.1 - Constructor de la clase padre Tk que hereda App
        # 1.2 - Agrego constructor de clase hija

        # 2.0 - Configurar la ventana
        self.configurar_ventana()

        # 3.0 - Configurar grid
        self.configurar_grid()

        # 4.0 - Mostrar la tabla
        self.mostrar_tabla()
    
    # 2.1 - Métodos para configurar ventana
    def configurar_ventana(self):
        self.geometry('600x400')
        self.configure(background='#1d2d44')
        self.title('Manejo de Ventanas con POO')
    
    # 3.1 - Método para configurar la distribución en columnas
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)  # 3.2 - Columna para tabla
        self.columnconfigure(1, weight=0)  # 3.3 - Columna para scroll
    
    # 4.1 - Método para mostrar la tabla
    def mostrar_tabla(self):
        # 4.2 - Definir un estilo
        estilos = ttk.Style()
        estilos.theme_use('clam')  # 4.3 - Prepara el manejo del tema oscuro
        estilos.configure('Treeview', background='black', foreground='white',
                          fieldbackground='black', rowheight=30)
        estilos.map('Treeview', background=[('selected','#3a86ff')])
        
        # 4.4 - Definir las columnas
        columnas = ('Id', 'Nombre', 'Edad')
        self.tabla = ttk.Treeview(self, columns=columnas, show='headings')  # 4.5 - Creamos el componente de tabla. Ponemos un show porque la 1º columna se usa como treeview que muestra subregistros o más información

        # 4.6 - Cabeceros de la tabla
        self.tabla.heading('Id', text='Id', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='Nombre', anchor=tk.CENTER)
        self.tabla.heading('Edad', text='Edad', anchor=tk.CENTER)
        
        # 4.7 - Formato de columnas
        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Edad', width=120)

        # 4.8 - Cargar datos a la tabla
        datos = ((1,'Alejandra',25), (2,'Matias',32))  # 4.9 - Definimos los datos como tuplas
        for persona in datos:
            self.tabla.insert(parent='', index=tk.END, values=persona)  # 4.10 - parent es el registro padre que estará vacío; para agregar registros se usa END

        # 4.11 - Agregamos un scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)  # 4.12 - Sincronizamos los componentes con set
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        
        # 4.13 - Asociar el evento select de la tabla
        self.tabla.bind('<<TreeviewSelect>>', self.mostrar_registro_seleccionado)
        
        # 4.14 - Publicamos la tabla en el grid
        self.tabla.grid(row=0, column=0, sticky=tk.NSEW)

    # 5.0 - Definimos método mostrar registro seleccionado
    def mostrar_registro_seleccionado(self, event):
        print('Ejecutando metodo mostrar_registro_seleccionado')
        elemento_seleccionado = self.tabla.selection()[0]  # 5.1 - Solo procesamos el primer registro seleccionado
        elemento = self.tabla.item(elemento_seleccionado)  # 5.2 - Obtenemos el item/elemento
        persona = elemento['values']  # 5.3 - Tupla que almacena datos de persona definidos más arriba
        print(persona)
        showinfo(title='Persona Seleccionado', message=f'Persona: {persona}')

# 6.0 - Validamos para ejecutar app directamente        
if __name__ == '__main__':
    app = App()
    app.mainloop()
