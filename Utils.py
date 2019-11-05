import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    print("\n--------------------------------------------- ")
    print("       [    Press Enter to continue    ]        ")
    print("--------------------------------------------- ")
    input()


def emptyData():
    print("\n\tNo existen FACTURAS en este momento.....!!!!\n")