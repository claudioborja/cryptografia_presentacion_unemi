import tkinter as tk
from tkinter import messagebox

# Función para cifrar una palabra con el cifrado César
def cesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Si es una letra
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Si no es letra, se deja igual
    return result

# Función para cifrar el texto completo
def cifrar_texto():
    texto = entrada_texto.get()  # Obtener el texto ingresado
    if not texto.strip():
        messagebox.showerror("Error", "Por favor ingrese un texto válido.")
        return

    palabras = texto.split()  # Dividir el texto en palabras
    texto_cifrado = []

    for i, palabra in enumerate(palabras):
        desplazamiento = i + 1  # Desplazamiento para cada palabra (1 para la primera, 2 para la segunda, etc.)
        palabra_cifrada = cesar_cipher(palabra, desplazamiento)
        texto_cifrado.append(palabra_cifrada)

    # Mostrar el texto cifrado en el área de resultado
    resultado.set(" ".join(texto_cifrado))

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Cifrado César por Palabra")
ventana.geometry("500x300")

# Etiqueta y entrada para el texto
tk.Label(ventana, text="Ingrese el texto a cifrar:", font=("Arial", 12)).pack(pady=10)
entrada_texto = tk.Entry(ventana, font=("Arial", 12), width=40)
entrada_texto.pack(pady=5)

# Botón para cifrar
tk.Button(ventana, text="Cifrar", font=("Arial", 12), command=cifrar_texto).pack(pady=10)

# Área para mostrar el resultado
resultado = tk.StringVar()
tk.Label(ventana, text="Texto cifrado:", font=("Arial", 12)).pack(pady=10)
tk.Entry(ventana, font=("Arial", 12), width=40, state="readonly", textvariable=resultado).pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()
