import os


class Menu:

    @staticmethod
    def mostrarOpciones():
        os.system("cls")
        print("-------------------SISTEMA DE VENTAS-------------------")
        print("")
        print("Selecciona una categoria:")
        print("A) PRODUCTOS")
        print("B) VENTAS")
        print("C) CLIENTE")
        print("D) SALIR")
        opcion = input("Seleccione la opcion:")

        return opcion

    @staticmethod
    def mostrarAcciones():
        print("")
        print("Seleccione una accion:")
        print("1) Crear")
        print("2) Modificar")
        print("3) Eliminar")
        print("4) Ver")
        print("5) Regresar")
        opcion = int(input("Seleccione la opcion:"))
        return opcion
