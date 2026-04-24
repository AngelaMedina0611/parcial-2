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
            
# Inorden: hijo izquierdo -> raíz -> hijos derechos
def inorden(nodo, resultado):
    if nodo:
        if len(nodo.hijos) > 0:
            inorden(nodo.hijos[0], resultado)   # Recorre el primer hijo (izquierda)

        resultado.append(nodo.nombre)           # Luego guarda el nodo actual

        for hijo in nodo.hijos[1:]:             # Recorre los demás hijos (derecha)
            inorden(hijo, resultado)
            
# Postorden: primero hijos -> luego raíz
def postorden(nodo, resultado):
    if nodo:
        for hijo in nodo.hijos:                 # Recorre todos los hijos primero
            postorden(hijo, resultado)
        resultado.append(nodo.nombre)           # Al final guarda el nodo actual
# ---------------- CONSTRUCCIÓN DEL ÁRBOL ----------------
raiz = Nodo("Disco C:")   # Nodo raíz del árbol

# Nivel 2
documentos = Nodo("Documentos")
multimedia = Nodo("Multimedia")

raiz.agregar_hijo(documentos)
raiz.agregar_hijo(multimedia)

# Nivel 3
docs = Nodo("Documentos")
trabajo = Nodo("Trabajo")
fotos = Nodo("Fotos")
musica = Nodo("Música")

documentos.agregar_hijo(docs)
documentos.agregar_hijo(trabajo)

multimedia.agregar_hijo(fotos)
multimedia.agregar_hijo(musica)