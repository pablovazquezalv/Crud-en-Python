class Lista:

    def __init__(self):
        self.listas = []

    def crear(self, item):
        self.listas.append(item)

    def mostrar(self):
        return self.listas

    def actualizar(self, index, item):
        self.listas[index] = item

    def eliminar(self, index):
        del self.listas[index]
