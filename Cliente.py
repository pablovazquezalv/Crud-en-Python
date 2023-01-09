class Cliente:

    def __init__(self, rfc, nombre, telefono, lista_clientes):
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono
        self.lista_clientes = lista_clientes

    # Lista de clientes


lista_clientes = []


def crear(cliente: Cliente, lista_clientes):
    lista_clientes.append(cliente)


# ya funciona
def buscar(nombre,lista_clientes):
    for cliente in lista_clientes:
        if cliente.rfc == nombre:
            return cliente
        else:
            print("no existe")


def eliminar(eliminarv,lista_clientes):
    eliminarc = buscar(eliminarv,lista_clientes)
    lista_clientes.remove(eliminarc)


def modificar(modificarv, codigo, nombre, telefono,lista_clientes):
    modificarc = buscar(modificarv,lista_clientes)
    if modificarc:
        print(modificarc)
        lista_clientes.remove(modificarc)
        cliente = Cliente(codigo, nombre, telefono,lista_clientes)
        lista_clientes.append(cliente)
    else:
        print("no existe")


def mostrar(lista_clientes):
    for cliente in lista_clientes:
        print("---------------------------")
        print("RFC |Nombre | Telefono  ")
        print(f"{cliente.rfc} |{cliente.nombre}|{cliente.telefono} |")
