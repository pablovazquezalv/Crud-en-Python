from Lista import Lista


class Producto(Lista):

    def __init__(self, codigo="", nombre="", descripcion="", precio=""):
        super().__init__()
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio


if __name__ == "__main__":
    producto = Lista()
    producto1 = Producto("75011", "Xbox", "consola", 30000)
    producto2 = Producto("75012", "Play", "consola", 49000)
    producto3 = Producto("75013", "Wii", "consola", 2000)
    producto.crear(producto1)
    producto.crear(producto2)
    producto.crear(producto3)
    venta_nueva = Producto("75010", "Computadora", "Marca Acer", 310000)
    producto.actualizar(2, venta_nueva)
    producto.eliminar(1)
    listado = producto.mostrar()

    for producto in listado:
        print("---------------------------")
        print(f"{producto.codigo} |{producto.nombre}|{producto.descripcion} |{producto.precio}")

    """producto = Producto("182", "xbox", "consola", 2000000)
    producto.crear(producto)
    producto.mostrar()
    """
