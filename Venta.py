from Lista import Lista


class Venta(Lista):

    def __init__(self, cliente="", detalle=0, fecha="", total=0):
        super().__init__()
        self.cliente = cliente
        self.detalle = detalle
        self.fecha = fecha
        self.total = total


if __name__ == "__main__":
    venta = Lista()
    venta1 = Venta("1001", 20, "2022",30000)
    venta2 = Venta("1002", 30, "2023",49000)
    venta3 = Venta("1003", 4, "2021",2000)
    venta.crear(venta1)
    venta.crear(venta2)
    venta.crear(venta3)
    venta_nueva = Venta("1000", 21, "2020",310000)
    venta.actualizar(2, venta_nueva)
    venta.eliminar(1)
    listado = venta.mostrar()

    for ventas in listado:
        print("---------------------------")
        print(f"{ventas.cliente} |{ventas.detalle}|{ventas.fecha} |{ventas.total}")



