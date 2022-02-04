import os

from self import self


def op1():
    op1_c=0
    while op1_c!=1:
        try:
            print("1.agregar producto al carro\n" +
                  "2.finalizar compra\n" +
                  "3.eliminar producto\n" +
                  "4.editar cantidad\n" +
                  "5.salir\n")
            opcion = input("que desea hacer:\t")
            if opcion == "1":

                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                op1_c=1
                os.system("cls")
                pass
            pass
        except:
            pass
        pass
    pass
def op2():
    op2_c = 0
    while op2_c != 1:
        try:
            print("1.crear archivo de historial\n" +
                  "2.buscar\n" +
                  "3.eliminar historial\n" +
                  "4.respadar historial\n" +
                  "5.salir\n")
            opcion = input("que desea hacer:\t")
            if opcion == "1":

                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                op2_c = 1
                os.system("cls")
                pass
            pass
        except:
            pass
        pass
    pass
class Menu:
    def menu(self):
        c_menu=0
        while c_menu!=1:
            try:
                print("que desea hacer\n" +
                      "1.comprar\n" +
                      "2.ver historial de compra\n" +
                      "3.salir\n"
                      )
                op = input("seleccione una opcion:\t")
                if op == "1":
                    os.system("cls")
                    op1()
                elif op == "2":
                    os.system("cls")
                    op2()
                    pass
                elif op == "3":
                    c_menu = 1
                    os.system("cls")
                else:
                    pass
                pass
            except:
                pass
            pass
        pass
    pass
Menu.menu(self)