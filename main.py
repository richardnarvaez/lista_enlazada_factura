
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


# -------------------- REGISTRAR ITEM
def registrar_products():
    listProducts = List()  # Lista que llevara todos los Productos
    total = 0
    op = ""
    while op != "n":
        try:
            print("Ingresar NUEVO Item")
            item = Product()
            item.name = input("Como se llama el PRODUCTO: ")
            item.price = float(input("Cual es el precio (Formato: 9.85): "))
            item.count = int(input("Cuant@s -> " + item.name + " quieres?: "))
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
    item_invoice = Invoice()
    print("\n\n\t[  REGISTRO  ]")
    print("\t--------------------")
    print("\n\tDATOS DE FACTURA ")

    item_invoice.code = utils.getRandomID()
    item_invoice.date = date.today().strftime("%b-%d-%Y")

    print("\tCODIGO: ", item_invoice.code)
    print("\tFECHA: ", item_invoice.date)
    item_invoice.names = input("\tNOMBRES:")
    item_invoice.phone = input("\tTELEFONO:")

    # Registramos los Productos, como es otra lista tenemos una funcion separada.
    iproduct = registrar_products()
    item_invoice.list = iproduct[0]  # Devuelve la LISTA de Productos
    item_invoice.total = iproduct[1]  # Devuelve el valor total de la compra
    lista.add_at_front(item_invoice)


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
    return list


# -------------------- ACTUALIZAR FACTURA
def actualizar_factura(list):
    print("Proximamente")

def insertar_en_posicion(list):
  pos = input("Ingresar la posicion: ")
  item_invoice = Invoice()
  print("\n\n\t[  REGISTRO  ]")
  print("\t--------------------")
  print("\n\tDATOS DE FACTURA ")

  item_invoice.code = utils.getRandomID()
  item_invoice.date = date.today().strftime("%b-%d-%Y")

  print("\tCODIGO: ", item_invoice.code)
  print("\tFECHA: ", item_invoice.date)
  item_invoice.names = input("\tNOMBRES:")
  item_invoice.phone = input("\tTELEFONO:")

  # Registramos los Productos, como es otra lista tenemos una funcion separada.
  iproduct = registrar_products()
  item_invoice.list = iproduct[0]  # Devuelve la LISTA de Productos
  item_invoice.total = iproduct[1]  # Devuelve el valor total de la compra
  list.add_in_position(int(pos), item_invoice)


# -------------------- FUNCION PRINCIPAL
def main():
    out = False
    list_facturas = List()

    while not out:

        option = menu()
        utils.clear()

        if option <= "0" or option >= "7":
            print("\nINGRESE UNA OPCION VALIDA...\n")

        elif option == "1":
            registrar_factura(list_facturas)

        elif option == "2":
            if list_facturas.is_empty():
                utils.emptyData()
            else:
                eliminar_factura(list_facturas).print_list()

        elif option == "3":
            if list_facturas.is_empty():
                utils.emptyData()
            else:
                mostrar_nodos(list_facturas)

        elif option == "4":
            if list_facturas.is_empty():
                utils.emptyData()
            else:
                mostrar_facturas(list_facturas)

        elif option == "5":
            if list_facturas.is_empty():
                print("Solo se puede insertar en la primera posicion por que no hay mas items")
            else:
                insertar_en_posicion(list_facturas)

        if option != "6":
            utils.pause()
        else:
            print("Saliendo...")
            out = True

        utils.clear()


if __name__ == '__main__':
    main()