# 🗝️ Proyecto Criptografía - UNEMI

*Repositorio académico del Grupo B - Tecnologías de la Información*  
**Asignatura:** Sistemas Operativos  
**Institución:** Universidad Estatal de Milagro (UNEMI)

## 📌 Acerca del Proyecto
Colección de implementaciones didácticas de algoritmos criptográficos históricos:
- Cifrado César (variantes básica y avanzadas)
- Cifrado Atbash
- Cifrado Hill (matricial)
  
Desarrollado como material complementario para la asignatura de Sistemas Operativos.

## Estructura de Directorios

```bash
📂 cryptografia_presentacion_unemi/
├── 📂 1. atbash/
│   └── 📜 atbash.py        # Implementación clásica con CLI
├── 📂 2. cesar/
│   ├── 📜 1. cesar.py                 # César simple (desplazamiento fijo)
│   ├── 📜 2.cesar_multiple.py         # Múltiples desplazamientos predefinidos
│   ├── 📜 3.cesar_multiple_aleatorio.py # Desplazamientos dinámicos
│   └── 📜 4. cesar_fb.py              # Fuerza Bruta
├── 📂 3. Hill/
│   └── 📜 hill.py           # Matricial
├── 📜 crypto.pptx        # Presentación teórica principal
├── 📜 crypto.pdf         #Presentación teórica principal formato PDF
└── 📜 LICENSE            # Licencia MIT (uso académico)
```
## Programas Destacados
🔷 Cifrado Hill (Matricial)

## Configuración clave en hill.py
```bash

MATRIZ_CIFRADO = [[11, 8], [3, 7]]       
MATRIZ_DESCIFRADO = [[7, 18], [23, 11]]  
```
## Características:
- Interfaz gráfica intuitiva (Tkinter) 
- Visualización paso a paso del proceso
- Manejo automático de padding ('X')
- Validación de entrada de texto

## César Avanzado
```bash

# Ejecución con parámetros variables
Variantes implementadas:

    Desplazamiento simple (César clásico) 
    Desplazamiento múltiple predefinido
    Desplazamiento aleatorio por carácter
    Fuerza Bruta
```
## 🖥️ Instrucciones de Uso

Clonar repositorio:

```bash

git https://github.com/claudioborja/cryptografia_presentacion_unemi.git
```
Ejecutar programa deseado:

```bash

# Ejemplo: Cifrado Hill
cd 3.Hill && python hill.py

# Ejemplo: César aleatorio
cd 2.cesar && python 3.cesar_multiple_aleatorio.py "Texto" 5 7 13
```
## 📄 Licencia


MIT License - Restricción académica:
El uso de este material queda limitado a fines educativos y de investigación dentro de la comunidad estudiantil UNEMI.

## 🎓 Contexto Académico
Material desarrollado conforme al syllabus 2025 de la asignatura Sistemas Operativos - Carrera de Tecnologías de la Información, fundamentado en:
- NIST Special Publication 800-175B (Guidelines for Cryptographic Algorithms) 
- ISO/IEC 18033-1:2015 (Encryption Algorithms) 
- Estándares de seguridad informática UNEMI-2024 

**Creado por Grupo B - ©2025 UNEMI**
Última actualización: 10 de febrero de 2025
- ALEJANDRO ENRIQUE AÑAPA DE LA CRUZ
- CLAUDIO XAVIER BORJA SALTOS
- MERCY JOHANNA MARIDUEÑA ALAVA
- RONALD ALEXANDER SOLÓRZANO ZAPATA

**Nota**
Se utilizo DeepSeek R1 como soporte en el desarrollo y ajuste de codigos.
