import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror #para msjs de eventos en boton log

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.geometry('600x400')  # Redimensionar la ventana
ventana.title('Login')  # Modificar el título
ventana.configure(background='#1d2d44')  # Color de la ventana

# 2. Configuración del Grid de la ventana
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

# 3. Crear y configurar los estilos
estilos = ttk.Style()
estilos.theme_use('clam')  # Usamos tema clam 'oscuro'
estilos.configure(ventana, background='#1d2d44', foreground='white', fieldbackground='black')
estilos.configure('TButton', background='#005f73')  # Tbutton es una clase que afecta a todos los botones
estilos.map('TButton', background=[('active','#0a9396')])  # Efecto de color al hacer clic en el botón

# 4. Crear el Frame contenedor (ventana invisible)
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# 5. Titulo de la ventana
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)  # Centrar el texto en las dos columnas restantes

# 6. Campos de Usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')  # Etiqueta Usuario
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

usuario_caja_texto = ttk.Entry(frame)  # Caja de texto para el usuario
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# 7. Campos de Password
password_etiqueta = ttk.Label(frame, text='Password: ')  # Etiqueta Password
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_texto = ttk.Entry(frame, show='*')  # Caja de texto para la contraseña (caracteres ocultos)
password_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# 8. Botón de login
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# 9. Método de validación del evento de login
def validar(event):
    usuario = usuario_caja_texto.get()  # Obtener texto del campo usuario
    password = password_caja_texto.get()  # Obtener texto del campo password
    if usuario == 'root' and password == 'root':  # Validar los datos de usuario y contraseña
        showinfo(title='Login', message='Datos correctos')  # Si son correctos, mostrar mensaje de éxito
    else:
        showerror(title='Login', message='Datos incorrectos')  # Si no, mostrar mensaje de error

# 10. Asociar eventos al botón de login
login_boton.bind('<Return>', validar)  # Asociar el evento de presionar "Enter" al método de validación
login_boton.bind('<Button-1>', validar)  # Asociar el evento de presionar el botón izquierdo del ratón

# 11. Publicar el frame en la ventana
frame.grid(row=0, column=0)  # Centrar el frame en la ventana

# 12. Ejecutar la ventana
ventana.mainloop()  # Iniciar la interfaz gráfica
