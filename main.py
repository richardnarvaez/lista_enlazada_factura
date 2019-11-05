
'''
    Autor: Richard Vinueza
    Curso: Estructura de Datos - ESPOCH
    Ejercicio: FACTURA (PYTHON 3)
    IDE: PyCharm
'''


import List as ls
import Utils as u
import uuid
from datetime import date


class Factura:
    def __init__(self, _code=None, _names=None, _lastNames=None, _date=None, _phone=None, _total=None, _list=None):
        self.code = _code  # campo codigo
        self.names = _names  # campo que almacena el nombre
        self.date = _date  # campo que almacena la direccion
        self.phone = _phone   # campo que almacena el telefono
        self.total = _total  # campo que almacena el telefono
        self.list = _list  # campo que almacena el telefono

    def getData(self):
        print("Data")

    def set(self):
        print("setDAta")


class Item:
    def __init__(self, _name=None, _price=None):
        self.count = 0
        self.name = _name
        self.price = _price
        self.total = 0.0


# -------------------- MENU PRINCIPAL --------------------
def menu():
    print("\n----------------------------------------")
    print("            [    FACTURAS    ]            ")
    print("----------------------------------------\n")
    print(" 1. REGISTRAR FACTURA                     ")
    print(" 2. ELIMINAR FACTURA                      ")
    print(" 3. MOSTRAR NODOS                         ")
    print(" 4. MOSTRAR LISTADO DE FACURAS            ")
    print(" 5. SALIR                                 ")
    return input("\n Ingrese opción : ")


# ----------------- MENU ACTUALIZAR UN DATO --------------
def menu_actualizar():
    print("\n\t\t[    ESPECIFIQUE CAMPO A ACTUALIZAR    ]\n  ")
    print("\t\t----------------------------\n\n              ")
    print(" 1. NOMBRES                                       ")
    print(" 2. APELLIDOS                                     ")
    print(" 3. DIRECCION                                     ")
    print(" 4. TELEFONO                                      ")
    print(" 5. SALIR                                         ")
    return input("\n Ingrese opcion : ")


# ----------------- REGISTRAR ITEM -----------------------
def registrar_items():
    listItems = ls.List()
    total = 0
    op = ""
    while op != "n":
        try:
            print("Ingresar Item")
            item = Item()
            item.count = input("Cuantos Quieres?: ")
            item.name = "Item 1"
            item.price = 12.80
            item.total = int(item.count) * item.price
            listItems.add_at_front(item)
            total += item.total
            op = input("Desea ingresar otro producto? (y/n)").lower()
        except ValueError:
            print("\t-------------------------------------")
            print("\tOcurrio un error al ingresar el ITEM!")
            print("\t-------------------------------------")
            op = 'y'

    return listItems, total


# -------------------- REGISTRAR FACTURA -----------------
def registrar_factura(lista):
    register = Factura()
    print("\n\n\t[  REGISTRO  ]")
    print("\t--------------------")
    print("\n\tDATOS DE FACTURA ")

    register.code = uuid.uuid4().hex[:4]
    register.date = date.today().strftime("%b-%d-%Y")
    print("\tCODIGO: ", register.code)
    print("\tFECHA: ", register.date)
    register.name = input("\tNOMBRES:")
    register.phone = input("\tTELEFONO:")
    itm = registrar_items()
    register.list = itm[0]
    register.total = itm[1]
    lista.add_at_front(register)
    print("Su FACTURA FUE GENERADA")
    print("Imprimir datos")
    lista.print_list()
    # else:
    #     print("Parece que no hay productos")
    #     print("Quieres abandonar esta Factura? (y/n)")


# -------------------- MOSTRAR FACTURA -------------------
def mostrar_facturas(list):
    node = list.getHead()
    while node != None:
        print("\t*************************************************")
        print("\t******************* FACTURA *********************")
        print("\t*************************************************")
        print("\tFactura: ", node.data.code)
        print("\tFecha: ", node.data.date)
        print("\tNombres: ", node.data.names)
        print("\t******************** ITEMS **********************")
        nodeItem = node.data.list.getHead()
        print("\t*************************************************")
        while nodeItem != None:
            print("\t", nodeItem.data.count, "    ",  nodeItem.data.name, "    ", nodeItem.data.price, "  ", nodeItem.data.total)
            nodeItem = nodeItem.next
        print("\t*************************************************")
        print("\t TOTAL: ", node.data.total)
        print("\t*************************************************")
        print("\t-------------------------------------------------\n\n")
        node = node.next


# -------------------- MOSTRAR NODOS -------------------
def mostrar_nodos(list):
    list.print_list()
# ------------------------ ELIMINAR FACTURA --------------
def eliminar_factura(list):
    cod = input("Ingresa el codigo de la FACTURA que deseas BORRAR: ")
    list.delete_node(cod)
    print("\n\n\n\tFACTURA ELIMINDA")
    print("------------------------")
    list.print_list()


# -------------------- ACTUALIZAR FACTURA ----------------
def actualizar_factura(list):
    print("Proximamente")


# /*-------------------- FUNCION PRINCIPAL ---------------*/
def main():
    out = False
    list = ls.List()

    while not out:

        u.clear()
        option = menu()
        u.clear()
        if option == "1":
            registrar_factura(list)
        elif option == "2":
            if list.is_empty():
                u.emptyData()
            else:
                eliminar_factura(list)
        elif option == "3":
            if list.is_empty():
                u.emptyData()
            else:
                # actualizar_factura(list)
                mostrar_nodos(list)
        elif option == "4":
            if list.is_empty():
                u.emptyData()
            else:
                mostrar_facturas(list)
        elif option <= "0" or option >= "6":
            print("\nINGRESE UNA OPCION VALIDA...\n")

        if option != "5":
            u.pause()
        else:
            print("Saliendo...")
            out = True


if __name__ == '__main__':
    main()
