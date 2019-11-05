
class Invoice:
    def __init__(self, _code=None, _names=None, _lastNames=None, _date=None, _phone=None, _total=None, _list=None):
        self.code = _code  # Codigo unico generado
        self.date = _date  # Fecha generada
        self.total = _total  # Suma de todos los produtos
        self.list = _list  # Lista con Productos
        self.names = _names
        self.phone = _phone

    def printInvoice(self):
        print("\t******************* FACTURA *********************")
        print("\t*************************************************\n")
        print("\tFactura: ", self.code)
        print("\tFecha: ", self.date)
        print("\tNombres: ", self.names)
        print("\n\t******************** ITEMS **********************")
        print("\t*************************************************\n")

        nodeItem = self.list.getHead()
        while nodeItem != None:
            nodeItem.data.printProduct()
            nodeItem = nodeItem.next

        print("\n\t*************************************************")
        print("\t TOTAL: ", self.total)
        print("\t*************************************************")
        print("\t-------------------------------------------------\n\n\n")


