# Clase Nodo: representa cada carpeta o archivo en el árbol
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre      # Nombre del nodo (ej. "Documentos", "informe.txt")
        self.hijos = []           # Lista de hijos (subcarpetas o archivos dentro)
    
    def agregar_hijo(self, hijo):
        # Método para añadir un hijo (subcarpeta o archivo) al nodo actual
        self.hijos.append(hijo)

    def mostrar(self, nivel=1): # 
        #Muestra la estructura jerárquica del árbol con indentación
        print("   " * (nivel - 1) + f"Nivel {nivel}: {self.nombre}")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)   # Llamada recursiva para mostrar los hijos
# ---------------- RECORRIDOS ----------------
# Preorden: raíz -> hijos (izquierda a derecha)
def preorden(nodo, resultado):
    if nodo:
        resultado.append(nodo.nombre)       # Primero se guarda el nodo actual
        for hijo in nodo.hijos:             # Luego se recorren sus hijos
            preorden(hijo, resultado)