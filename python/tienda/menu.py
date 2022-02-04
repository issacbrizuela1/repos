from self import self
import os
class menu:
    def __init__(self):
        self.carrito = {}
        pass
    def m_menu(self):
        c_menu = 0
        op = ""
        while c_menu != 1:
            try:
                print("que desea hacer\n" +
                      "1.comprar\n" +
                      "2.ver historial de compra\n" +
                      "3.buscar producto\n" +
                      "4.salir\n"
                      )
                op = input("seleccione una opcion:\t")

                if op == "1":
                    os.system("cls")
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

                            os.system("cls")
                            pass
                        pass
                    except:
                        pass
                    pass
                elif op == "2":
                    pass
                elif op == "3":
                    pass
                elif op == "4":
                    c_menu = 1
                    os.system("cls")
                    pass
                else:
                    pass
                pass
            except:
                pass
            pass
        pass
    pass