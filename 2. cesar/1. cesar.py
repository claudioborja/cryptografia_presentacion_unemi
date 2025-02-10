import tkinter as tk
from tkinter import ttk

def cifrado_cesar(texto, desplazamiento):
    """Función para cifrar un texto usando el cifrado César."""
    resultado = ""
    for char in texto:
        if char.isalpha():  # Verifica si es una letra
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char  # Si no es letra, se mantiene igual
    return resultado

def descifrado_cesar(texto, desplazamiento):
    """Función para descifrar un texto cifrado con el cifrado César."""
    return cifrado_cesar(texto, -desplazamiento)

def cifrar_texto():
    """Obtiene el texto y desplazamiento, y muestra el texto cifrado."""
    texto = entrada_texto.get()
    try:
        desplazamiento = int(entrada_desplazamiento.get())
        texto_cifrado = cifrado_cesar(texto, desplazamiento)
        salida_texto.delete(1.0, tk.END)
        salida_texto.insert(tk.END, texto_cifrado)
    except ValueError:
        salida_texto.delete(1.0, tk.END)
        salida_texto.insert(tk.END, "Por favor, ingresa un número válido para el desplazamiento.")

def descifrar_texto():
    """Obtiene el texto y desplazamiento, y muestra el texto descifrado."""
    texto = entrada_texto.get()
    try:
        desplazamiento = int(entrada_desplazamiento.get())
        texto_descifrado = descifrado_cesar(texto, desplazamiento)
        salida_texto.delete(1.0, tk.END)
        salida_texto.insert(tk.END, texto_descifrado)
    except ValueError:
        salida_texto.delete(1.0, tk.END)
        salida_texto.insert(tk.END, "Por favor, ingresa un número válido para el desplazamiento.")

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Cifrado César")
ventana.geometry("400x350")

# Etiqueta y entrada para el texto a cifrar/descifrar
ttk.Label(ventana, text="Texto:").pack(pady=5)
entrada_texto = ttk.Entry(ventana, width=50)
entrada_texto.pack(pady=5)

# Etiqueta y entrada para el desplazamiento
ttk.Label(ventana, text="Número de desplazamientos:").pack(pady=5)
entrada_desplazamiento = ttk.Entry(ventana, width=10)
entrada_desplazamiento.pack(pady=5)

# Botón para cifrar
boton_cifrar = ttk.Button(ventana, text="Cifrar", command=cifrar_texto)
boton_cifrar.pack(pady=10)

# Botón para descifrar
boton_descifrar = ttk.Button(ventana, text="Descifrar", command=descifrar_texto)
boton_descifrar.pack(pady=10)

# Caja de texto para mostrar el resultado
ttk.Label(ventana, text="Resultado:").pack(pady=5)
salida_texto = tk.Text(ventana, height=5, width=50)
salida_texto.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
