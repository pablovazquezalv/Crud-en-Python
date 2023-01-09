from Cliente import Cliente, buscar


class Venta(Cliente):

    def __init__(self, rfc, nombre, fecha, total, lista_ventas):
        super().__init__(rfc, nombre, fecha, lista_ventas)
        self.codigo = rfc
        self.total = total
        self.detalle_productos = nombre
        self.fecha=fecha
        self.lista_ventas = lista_ventas


lista_ventas = []


def modificar(venta_modificar, cliente, detalle_productos, fecha, total, lista_ventas):
    modificarc = buscar(venta_modificar, lista_ventas)
    if modificarc:
        print(modificarc)
        lista_ventas.remove(modificarc)
        cliente = Venta(cliente, detalle_productos, fecha, total, lista_ventas)
        lista_ventas.append(cliente)
    else:
        print("no existe")


def mostrar(lista_ventas):
    for venta in lista_ventas:
        print("---------------------------")
        print("Cliente |Detalle |Fecha| Total")
        print(f"{venta.codigo} |{venta.detalle_productos} |{venta.fecha} |{venta.total} ")
