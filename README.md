# 🌳 Sistema de Árbol de Directorios en Python
## 📌 Descripción

Este proyecto implementa una estructura de datos tipo árbol para simular un sistema de carpetas y archivos, similar al explorador de archivos de un sistema operativo.

## Cada nodo representa:

📁 Una carpeta
📄 Un archivo

Además, permite recorrer el árbol utilizando distintos métodos clásicos:

* Preorden
* Inorden
* Postorden
* 🧱 Estructura del Código
* 🔹 Clase Nodo

Representa cada elemento del árbol.

### Atributos:

nombre: Nombre del archivo o carpeta
hijos: Lista de nodos hijos

## Métodos:

* agregar_hijo(hijo): Añade un nuevo nodo hijo
* mostrar(nivel): Imprime la estructura jerárquica
* 🔁 Recorridos Implementados
* 📍 Preorden
* Orden: Raíz → Hijos
* Se usa para copiar o representar la estructura
* 📍 Inorden
* Orden: Hijo izquierdo → Raíz → Hijos derechos
* Adaptado para árboles no binarios
* 📍 Postorden
* Orden: Hijos → Raíz
* Útil para eliminar estructuras
## 🌲 Estructura del Árbol
Disco C:
├── Documentos
│   ├── Documentos
│   │   └── apuntes.txt
│   └── Trabajo
│       ├── informe.txt
│       └── informe2.txt
└── Multimedia
    ├── Fotos
    │   └── vacaciones.png
    └── Música
        └── melodia.mp3
## ▶️ Ejecución
* Guarda el archivo como:
* arbol.py
* Ejecuta en la terminal:
* python arbol.py
* 📤 Salida Esperada
## 📌 Estructura

### Se imprime el árbol con niveles:

Nivel 1: Disco C:
   Nivel 2: Documentos
   Nivel 2: Multimedia
   ...
## 📌 Recorridos

#### Preorden:

Disco C: -> Documentos -> Documentos -> apuntes.txt -> Trabajo -> informe.txt ...

#### Inorden:

apuntes.txt -> Documentos -> Documentos -> informe.txt ...

#### Postorden:

apuntes.txt -> Documentos -> informe.txt -> informe2.txt -> Trabajo ...
## ⚙️ Complejidad

| Operación            | Complejidad |
|---------------------|------------|
| Recorridos          | O(n)       |
| Inserción           | O(1)       |
| Mostrar estructura  | O(n)       |

Este proyecto muestra cómo usar árboles para representar estructuras jerárquicas, siendo útil en:

Sistemas de archivos
Organización de datos
Estructuras tipo XML o JSON