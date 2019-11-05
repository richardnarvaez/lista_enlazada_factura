
'''
    Autor: Richard Vinueza
    Curso: Estructura de Datos - ESPOCH
    Ejercicio: Funcionamiento basico de FACTURAS con LISTAS enlazadas (PYTHON 3)
    IDE: PyCharm
    Version: v0.0.2
    Ejecutar: python main.py
'''

# Importaciones
# --------------------
from List import List
import Utils as utils
from datetime import date

# Modelos
from models.Invoice import Invoice
from models.Product import Product
# --------------------


# -------------------- MENU PRINCIPAL
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


# -------------------- MENU ACTUALIZAR UN DATO
def menu_actualizar():
    print("\n\t\t[    ESPECIFIQUE CAMPO A ACTUALIZAR    ]\n  ")
    print("\t\t----------------------------\n\n              ")
    print(" 1. NOMBRES                                       ")
    print(" 2. APELLIDOS                                     ")
    print(" 3. DIRECCION                                     ")
    print(" 4. TELEFONO                                      ")
    print(" 5. SALIR                                         ")
    return input("\n Ingrese opcion : ")


# -------------------- REGISTRAR ITEM
def registrar_items():
    listProducts = List()  # Lista que llevara todos los Productos
    total = 0
    op = ""
    while op != "n":
        try:
            print("Ingresar NUEVO Item")
            item = Product()
            item.name = input("Como se llama el PRODUCTO: ")
            item.price = float(input("Cual es el precio (Formato: 9.85): "))
            item.count = int(input("Cuantos -> " + item.name + " quieres?: "))
            item.total = item.count * item.price
            listProducts.add_at_front(item)
            total += item.total
            op = input("Desea ingresar otro producto? (y/n)").lower()
        except ValueError:
            print("\t-------------------------------------")
            print("\tOcurrio un error al ingresar el ITEM!")
            print("\tEL ULTIMO PRODUCTO NO FUE AGREGADO!")
            print("\t-------------------------------------\n\n")
            op = 'y'

    return listProducts, total


# -------------------- REGISTRAR FACTURA
def registrar_factura(lista):
    register = Invoice()
    print("\n\n\t[  REGISTRO  ]")
    print("\t--------------------")
    print("\n\tDATOS DE FACTURA ")

    register.code = utils.getRandomID()
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


# -------------------- MOSTRAR FACTURA
def mostrar_facturas(list):
    node = list.getHead()
    while node != None:
        node.data.printInvoice()
        node = node.next


# -------------------- MOSTRAR NODOS
def mostrar_nodos(list):
    list.print_list()


# -------------------- ELIMINAR FACTURA
def eliminar_factura(list):
    cod = input("Ingresa el codigo de la FACTURA que deseas BORRAR: ")
    list.delete_node(cod)
    print("\n\n\n\tFACTURA ELIMINDA")
    print("------------------------")
    list.print_list()


# -------------------- ACTUALIZAR FACTURA
def actualizar_factura(list):
    print("Proximamente")


# -------------------- FUNCION PRINCIPAL
def main():
    out = False
    list = List()

    while not out:

        option = menu()
        utils.clear()

        if option == "1":
            registrar_factura(list)
        elif option == "2":
            if list.is_empty():
                utils.emptyData()
            else:
                eliminar_factura(list)
        elif option == "3":
            if list.is_empty():
                utils.emptyData()
            else:
                # actualizar_factura(list)
                mostrar_nodos(list)
        elif option == "4":
            if list.is_empty():
                utils.emptyData()
            else:
                mostrar_facturas(list)
        elif option <= "0" or option >= "6":
            print("\nINGRESE UNA OPCION VALIDA...\n")

        if option != "5":
            utils.pause()
        else:
            print("Saliendo...")
            out = True

        utils.clear()


if __name__ == '__main__':
    main()
