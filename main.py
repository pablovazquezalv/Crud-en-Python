import os

import Cliente
import Menu
import Producto
import Venta
from Menu import Menu

def run():
    opcion = ""
    lista_clientes = []
    lista_productos = []
    lista_ventas = []
    miproducto = Producto
    miventa = Venta
    micliente = Cliente
    while opcion != "X":
        opcion = Menu.mostrarOpciones()
        if opcion == "A":
            os.system("cls")
            print("-------------------PRODUCTOS-------------------")
            action = 0
            while action != 5:
                action = Menu.mostrarAcciones()
                os.system("cls")
                # Crear
                if action == 1:
                    print("-------------------CREAR-------------------")
                    codigo = input("Escribe el codigo:")
                    nombre = input("Escribe el nombre:")
                    descripcion = input("Escribe la descripcion:")
                    precio = int(input("Escribe el precio:"))
                    producto = Producto.Producto(codigo, nombre, descripcion, precio, lista_productos)
                    micliente.crear(producto, lista_productos)
                    print("--Producto guardado---")
                # Actuarial
                if action == 2:
                    print("-----MODIFICAR----")

                    print("---PRODUCTOS---")
                    micliente.mostrar(lista_productos)
                    productomodificar = input("Escribe el producto a modificar:")
                    codigo = input("Escribe el codigo:")
                    nombre = input("Escribe el nombre:")
                    descripcion = input("Escribe la descripcion:")
                    precio = int(input("Escribe el precio:"))
                    miproducto.modificar(productomodificar, codigo, nombre, descripcion, precio, lista_productos)
                # Eliminar
                if action == 3:
                    print("-----ELIMINAR----")
                    micliente.mostrar(lista_productos)
                    productoeliminar = input("Escribe el producto a eliminar:")
                    micliente.eliminar(productoeliminar, lista_productos)
                # Ver
                if action == 4:
                    print("-----MOSTRAR PRODUCTOS----")
                    miproducto.mostrar(lista_productos)

        if opcion == "B":
            print("-----VENTAS----")
            action = 0
            while action != 5:
                action = Menu.mostrarAcciones()
                os.system("cls")
                # Crear
                if action == 1:
                    print("-----CREAR----")
                    cliente = input("Escribe el cliente:")
                    detalle_productos = input("Escribe el detalle_productos:")
                    fecha = input("Escribe la fecha:")
                    total = input("Escribe el total:")
                    venta = Venta.Venta(cliente, detalle_productos, fecha, total, lista_ventas)
                    micliente.crear(venta, lista_ventas)

                    print("--VENTA CREADA---")
                # Actuarial
                if action == 2:
                    print("-----MODIFICAR----")

                    print("---PRODUCTOS---")
                    miventa.mostrar(lista_ventas)
                    venta_modificar = input("Escribe la venta a modificar:")
                    cliente = input("Escribe el nuevo cliente:")
                    detalle_productos = input("Escribe el detalle del producto:")
                    fecha = input("Escribe la descripcion:")
                    total = int(input("Escribe el total:"))
                    miventa.modificar(venta_modificar, cliente, detalle_productos, fecha, total,lista_clientes)

                # Eliminar
                if action == 3:
                    print("-----ELIMINAR----")
                    miventa.mostrar(lista_ventas)
                    venta_eliminar = input("Escribe la venta a eliminar:")
                    micliente.eliminar(venta_eliminar, lista_ventas)
                # Ver
                if action == 4:
                    print("-----MOSTRAR----")
                    miventa.mostrar(lista_ventas)
        if opcion == "C":
            print("-----CLIENTE----")
            action = 0
            while action != 5:
                action = Menu.mostrarAcciones()
                os.system("cls")
                # Crear
                if action == 1:
                    print("-----CREAR----")
                    rfc = input("Escribe el rfc:")
                    nombre = input("Escribe el nombre:")
                    telefono = int(input("Escribe el telefono:"))
                    cliente = Cliente.Cliente(rfc, nombre, telefono, lista_clientes)
                    micliente.crear(cliente, lista_clientes)
                    print("--CLIENTE REGISTRADO---")
                # Actuarial
                if action == 2:
                    print("-----MODIFICAR----")
                    print("---CLIENTES---")
                    Cliente.mostrar(lista_clientes)
                    cliente_modificar = input("Escribe el cliente a modificar:")
                    rfc = input("Escribe el nuevo rfc:")
                    nombre = input("Escribe el nuevo nombre:")
                    telefono = input("Escribe el nuevo telefono:")
                    micliente.modificar(cliente_modificar, rfc, nombre, telefono, lista_clientes)
                # Eliminar
                if action == 3:
                    print("-----ELIMINAR----")
                    micliente.mostrar(lista_clientes)
                    cliente_del = input("Escribe el rfc / cliente a eliminar:")
                    Cliente.eliminar(cliente_del, lista_clientes)
                # Ver
                if action == 4:
                    print("-----LISTADO DE CLIENTES----")
                    Cliente.mostrar(lista_clientes)


run()
