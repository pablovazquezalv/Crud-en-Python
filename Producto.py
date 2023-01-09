from Cliente import Cliente, buscar


class Producto(Cliente):

    def __init__(self, rfc, nombre, descripcion, precio, lista_productos):
        super().__init__(rfc, nombre, descripcion, lista_productos)
        self.codigo = rfc
        self.descripcion = descripcion
        self.precio = precio
        self.lista_productos = lista_productos


listaproductos = []


def modificar(productomodificar, codigo, nombre, descripcion, precio, lista_productos):
    modificarc = buscar(productomodificar, lista_productos)
    if modificarc:
        print(modificarc)
        lista_productos.remove(modificarc)
        cliente = Producto(codigo, nombre, descripcion, precio, lista_productos)
        lista_productos.append(cliente)
    else:
        print("no existe")


def mostrar(lista_productos):
    for producto in lista_productos:
        print("---------------------------")
        print("Codigo|Nombre|Descripcion| Precio")
        print(f"{producto.codigo}     |{producto.nombre}  |{producto.descripcion}  | {producto.precio}")
