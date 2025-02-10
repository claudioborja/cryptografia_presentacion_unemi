import tkinter as tk
from tkinter import ttk

def atbash_cipher(text):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]
    translation_table = str.maketrans(alphabet + alphabet.lower(), reversed_alphabet + reversed_alphabet.lower())
    return text.translate(translation_table)

def process_text():
    input_text = text_input.get("1.0", tk.END).strip()
    if input_text:
        result = atbash_cipher(input_text)
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert("1.0", result)
        text_output.config(state=tk.DISABLED)
    else:
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert("1.0", "Por favor, ingrese un texto.")
        text_output.config(state=tk.DISABLED)

# Configuración de la ventana
root = tk.Tk()
root.title("Cifrado Atbash")
root.geometry("800x800")
root.resizable(False, False)

# Etiqueta de título
title_label = ttk.Label(root, text="CIFRADO ATBASH", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Campo de entrada de texto
entry_label = ttk.Label(root, text="Ingrese el texto:", font=("Arial", 14))
entry_label.pack(pady=5)
text_input = tk.Text(root, font=("Arial", 14), width=80, height=10)
text_input.pack(pady=10)

# Botón para cifrar/descifrar
process_button = ttk.Button(root, text="Cifrar / Descifrar", command=process_text)
process_button.pack(pady=20)

# Área de salida de texto
output_label = ttk.Label(root, text="Texto cifrado/descifrado:", font=("Arial", 14))
output_label.pack(pady=5)
text_output = tk.Text(root, font=("Arial", 18, "bold"), width=80, height=15, state=tk.DISABLED)
text_output.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()