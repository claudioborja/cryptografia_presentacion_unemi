import tkinter as tk
from tkinter import ttk

def descifrar_cesar_fuerza_bruta(texto):
    """Descifra un texto cifrado con César probando todos los desplazamientos posibles."""
    resultados = []
    for desplazamiento in range(26):  # Probar todos los desplazamientos posibles (0 a 25)
        texto_descifrado = ""
        for char in texto:
            if char.isalpha():  # Solo descifrar letras
                base = ord('A') if char.isupper() else ord('a')
                texto_descifrado += chr((ord(char) - base - desplazamiento) % 26 + base)
            else:
                texto_descifrado += char  # Mantener caracteres no alfabéticos
        resultados.append(f"Desplazamiento {desplazamiento}:\n{texto_descifrado}\n")
    return "\n".join(resultados)

def descifrar():
    """Función para descifrar el texto ingresado por el usuario."""
    texto_cifrado = entrada_texto.get("1.0", tk.END).strip()  # Obtener texto del cuadro de entrada
    if not texto_cifrado:
        salida_texto.delete(1.0, tk.END)
        salida_texto.insert(tk.END, "Por favor, ingresa un texto cifrado.")
        return

    resultados = descifrar_cesar_fuerza_bruta(texto_cifrado)
    salida_texto.delete(1.0, tk.END)
    salida_texto.insert(tk.END, resultados)

# Configurar la ventana principal
ventana = tk.Tk()
ventana.title("Descifrador César por Fuerza Bruta")
ventana.geometry("800x800")  # Cambiar la resolución de la ventana

# Etiqueta y cuadro de texto para ingresar el texto cifrado
ttk.Label(ventana, text="Texto cifrado:").pack(pady=5)

# Frame para el cuadro de entrada con barra de desplazamiento
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

scroll_entrada = tk.Scrollbar(frame_entrada)
scroll_entrada.pack(side=tk.RIGHT, fill=tk.Y)

entrada_texto = tk.Text(frame_entrada, height=10, wrap=tk.WORD, yscrollcommand=scroll_entrada.set)
entrada_texto.pack(fill=tk.BOTH, expand=True)
scroll_entrada.config(command=entrada_texto.yview)

# Botón para descifrar
boton_descifrar = ttk.Button(ventana, text="Descifrar", command=descifrar)
boton_descifrar.pack(pady=10)

# Etiqueta y cuadro de texto para mostrar los resultados
ttk.Label(ventana, text="Resultados (todos los desplazamientos):").pack(pady=5)

# Frame para el cuadro de salida con barra de desplazamiento
frame_salida = tk.Frame(ventana)
frame_salida.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

scroll_salida = tk.Scrollbar(frame_salida)
scroll_salida.pack(side=tk.RIGHT, fill=tk.Y)

salida_texto = tk.Text(frame_salida, height=25, wrap=tk.WORD, yscrollcommand=scroll_salida.set)
salida_texto.pack(fill=tk.BOTH, expand=True)
scroll_salida.config(command=salida_texto.yview)

# Iniciar la aplicación
ventana.mainloop()
