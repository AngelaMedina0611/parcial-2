# Clase Nodo: representa cada carpeta o archivo en el árbol
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre      # Nombre del nodo (ej. "Documentos", "informe.txt")
        self.hijos = []           # Lista de hijos (subcarpetas o archivos dentro)