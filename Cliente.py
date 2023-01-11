from Lista import Lista
import json


class Cliente(Lista):

    def __init__(self, rfc="", nombre="", telefono=""):
        super().__init__()
        self.rfc = rfc
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"RFC: {self.rfc}\nNombre: {self.nombre}\nTelefono: {self.telefono}\n"
    # Lista de clientes


if __name__ == "__main__":
    clientes = Lista()
    clientes1 = Cliente("1001", "Pablo", "8717684433")
    clientes2 = Cliente("1002", "Raul", "8717684433")
    clientes3 = Cliente("1003", "Melissa", "8712624633")
    clientes.crear(clientes1)
    clientes.crear(clientes2)
    clientes.crear(clientes3)
   # x = '{ "rfc":"1004", "nombre":Jesus, "telefono":"872828822"}'
    #y = json.loads(x)
    #clientes.crear(y)
    cliente_nuevo = Cliente("1000", "Andrea", "567738398")
    clientes.actualizar(2, cliente_nuevo)
    clientes.eliminar(1)
    listado = clientes.mostrar()

    for cliente in listado:
        print("---------------------------")
        print(f"{cliente.rfc} |{cliente.nombre}|{cliente.telefono} |")

    # print(lista1)
    # lista.__str__()
    # cliente_nuevo = Cliente("123", "Pablo", 871869644)
    # lista.actualizar(0,cliente_nuevo)
    # cliente.eliminar(0)
