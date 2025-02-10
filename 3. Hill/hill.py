from tkinter import *

class HillCipher:
    def __init__(self):
        self.key = [[11, 8], [3, 7]]        # Matriz clave (invertible módulo 26)
        self.inv_key = [[7, 18], [23, 11]] # Matriz inversa
        
    def encrypt_text(self):
        texto = self.entrada_cifrar.get().upper().replace(" ", "")
        texto = ''.join([c for c in texto if c.isalpha()])
        
        if len(texto)%2 != 0:
            texto += 'X'
            
        procedimiento = f"Matriz de cifrado:\n{self.key}\nTexto original: {texto}\n\n"
        cifrado = ""
        
        for i in range(0, len(texto), 2):
            bloque = texto[i:i+2]
            m = [ord(c)-65 for c in bloque]
            c1 = (self.key[0][0]*m[0] + self.key[0][1]*m[1]) % 26
            c2 = (self.key[1][0]*m[0] + self.key[1][1]*m[1]) % 26
            cifrado_bloque = chr(c1+65) + chr(c2+65)
            
            procedimiento += f"Bloque: {bloque} = {m}\n"
            procedimiento += f"{self.key[0][0]}*{m[0]} + {self.key[0][1]}*{m[1]} = {c1} ({chr(c1+65)})\n"
            procedimiento += f"{self.key[1][0]}*{m[0]} + {self.key[1][1]}*{m[1]} = {c2} ({chr(c2+65)})\n"
            procedimiento += f"Resultado: {cifrado_bloque}\n\n"
            
            cifrado += cifrado_bloque
        
        self.texto_cifrar.delete(1.0, END)
        self.texto_cifrar.insert(END, procedimiento + f"\nTexto cifrado: {cifrado}")

    def decrypt_text(self):
        texto = self.entrada_descifrar.get().upper().replace(" ", "")
        texto = ''.join([c for c in texto if c.isalpha()])
        
        if len(texto)%2 != 0:
            texto += 'X'
            
        procedimiento = f"Matriz inversa:\n{self.inv_key}\nTexto cifrado: {texto}\n\n"
        descifrado = ""
        
        for i in range(0, len(texto), 2):
            bloque = texto[i:i+2]
            c = [ord(ch)-65 for ch in bloque]
            p1 = (self.inv_key[0][0]*c[0] + self.inv_key[0][1]*c[1]) % 26
            p2 = (self.inv_key[1][0]*c[0] + self.inv_key[1][1]*c[1]) % 26
            descifrado_bloque = chr(p1+65) + chr(p2+65)
            
            procedimiento += f"Bloque: {bloque} = {c}\n"
            procedimiento += f"{self.inv_key[0][0]}*{c[0]} + {self.inv_key[0][1]}*{c[1]} = {p1} ({chr(p1+65)})\n"
            procedimiento += f"{self.inv_key[1][0]}*{c[0]} + {self.inv_key[1][1]}*{c[1]} = {p2} ({chr(p2+65)})\n"
            procedimiento += f"Resultado: {descifrado_bloque}\n\n"
            
            descifrado += descifrado_bloque
        
        self.texto_descifrar.delete(1.0, END)
        self.texto_descifrar.insert(END, procedimiento + f"\nTexto descifrado: {descifrado}")

    def __init_gui__(self):
        root = Tk()
        root.title("Cifrado Hill")
        
        # Grupo cifrado
        grupo_cifrado = Frame(root)
        grupo_cifrado.pack(side=LEFT, padx=10, pady=10)
        
        Label(grupo_cifrado, text="Texto a cifrar:").pack()
        self.entrada_cifrar = Entry(grupo_cifrado, width=30)
        self.entrada_cifrar.pack()
        
        Button(grupo_cifrado, text="Cifrar", command=self.encrypt_text).pack(pady=5)
        
        self.texto_cifrar = Text(grupo_cifrado, width=50, height=20)
        self.texto_cifrar.pack()
        
        # Grupo descifrado
        grupo_descifrado = Frame(root)
        grupo_descifrado.pack(side=RIGHT, padx=10, pady=10)
        
        Label(grupo_descifrado, text="Texto a descifrar:").pack()
        self.entrada_descifrar = Entry(grupo_descifrado, width=30)
        self.entrada_descifrar.pack()
        
        Button(grupo_descifrado, text="Descifrar", command=self.decrypt_text).pack(pady=5)
        
        self.texto_descifrar = Text(grupo_descifrado, width=50, height=20)
        self.texto_descifrar.pack()
        
        root.mainloop()

if __name__ == "__main__":
    hc = HillCipher()
    hc.__init_gui__()
