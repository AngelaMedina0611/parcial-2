# 🌳 Sistema de Árbol de Directorios en Python

## 📌 Descripción
Este proyecto implementa una estructura de datos tipo árbol para simular un sistema de carpetas y archivos, similar al explorador de archivos de un sistema operativo.

Cada nodo representa:
- 📁 Una carpeta  
- 📄 Un archivo  

Además, permite recorrer el árbol utilizando distintos métodos:
- Preorden  
- Inorden  
- Postorden  

---

## ⚠️ Problemática
Una empresa guarda sus documentos en un sistema jerárquico de carpetas y archivos.

El administrador necesita:
- Crear copias de seguridad de toda la estructura  
- Realizar auditorías de forma rápida  
- Ejecutar procesos de limpieza para eliminar archivos innecesarios  

Para solucionar esto, se implementa una estructura de datos tipo árbol que permite organizar y recorrer eficientemente toda la información.

---

## 🧱 Estructura del Código

### 🔹 Nodos
Los nodos representan cada elemento del sistema:
- Carpetas  
- Archivos  

### 🔹 Conexiones
Las conexiones indican la ubicación de cada elemento dentro de la jerarquía.

### 🔹 Niveles del árbol
- Nivel 1: Raíz (Disco C:)  
- Nivel 2: Carpetas principales  
- Nivel 3: Subcarpetas  
- Nivel 4: Archivos (hojas)  

---

## 🌲 Estructura del Árbol
```
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
```

---

## 🔁 Recorridos

### 📍 Preorden
Raíz → Hijos  
✔ Útil para copiar toda la estructura (backup)

### 📍 Inorden
Izquierda → Raíz → Derecha  
✔ Útil para inspección ordenada (adaptado)

### 📍 Postorden
Hijos → Raíz  
✔ Útil para eliminar archivos o limpiar estructura

---

## ▶️ Ejecución
```bash
python arbol.py
```

---

## ⚙️ Complejidad

| Operación  | Complejidad |
|-----------|------------|
| Recorridos | O(n) |
| Inserción  | O(1) |

---

## 🎯 Conclusión
El uso de árboles permite representar estructuras jerárquicas de forma clara y eficiente, facilitando procesos como:
- Respaldo de información  
- Auditorías  
- Limpieza de archivos  
## 👩‍💻 AUTOR 
- Angela medina
- Kevin preciado
- Gustavo valencia

Proyecto académico de estructuras de datos.
