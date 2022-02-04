from empleado import Empleado
from cliente import Cliente
from producto import Producto


class Comprar(Producto,Cliente,Empleado):
    id=0
    carrito=[]
    orden_compra=[]
    cantidad=0
    def __init__(self):
        super().__init__()
    def AgregarCarrito(self):
        self.id+=1
        c_carrito=0
        a=input("ingrese el # del producto:\t")
        b=input("ingrese la cantidad a comprar:\t")
        
        self.carrito.append(
            {
                "producto":int(a),
                "cantidad":int(b)
             })
        print("producto agregado al carro")
    def MostrarCarrito(self):
        print("productos en el carrito:\n")
        print(self.carrito)
    def EditarCarrito(self):
        self.MostrarCarrito()
    def mostrar(self):
        for x in self.lista_productos:
            print(
                "-----------------------------\n"+
                "#:\t\t\t"+str(x["id_producto"])+"\n"+
                "nombre:\t\t"+x["nombre"]+"\n"+
                "precio:\t\t"+str(x["precio"])+"\n"+
                "disponibles:"+str(x["stok"])+"\n"+
                "-----------------------------\n"
                 )
        pass
c=Comprar()
c.agregar_producto()
c.mostrar_productos()
c.AgregarCarrito()
c.MostrarCarrito()
#print(c.carrito)