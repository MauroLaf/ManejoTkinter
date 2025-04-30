import tkinter as tk  # 1.0 - Renombro la librería tkinter

# 2.0 - Creamos un objeto de tipo ventana, llamando a la clase Tk
ventana = tk.Tk()

# 3.0 - Redimensionar la ventana
ventana.geometry('600x400')  # 3.1 - Tamaño de la ventana en px

# 4.0 - Modificar el título
ventana.title('Nueva Ventana')  # 4.1 - Establecemos el título de la ventana

# 5.0 - Evitar redimensionar la ventana
ventana.resizable(0, 0)  # 5.1 - Establecemos valores 0 en x e y para que no se redimensione más, incluso si tratamos de hacer más grande la ventana

# 6.0 - Color de la ventana
ventana.configure(background='#1d2d44')  # 6.1 - Cambiamos el color de fondo de la ventana

# 7.0 - Hacemos visible la ventana
ventana.mainloop()  # 7.1 - Ejecutamos el ciclo principal de la ventana
