class Producto:
    id_producto =0
    nombre =""
    stok =0
    precio_u =0.0
    lista_productos = []
    def __init__(self):
        self.id_producto=0
        self.nombre = ""
        self.stok = 0
        self.precio_u = 0.0
        self.lista_productos = []
        pass
    def agregar_producto(self):
        self.id_producto+=1
        self.nombre = input("nombre del producto:\t")
        self.stok = input("cantidad en almacen:\t")
        self.precio = input("precio que tendra el producto:\t")
        self.lista_productos = [
            {
                "id_producto": self.id_producto,
                "nombre": str(self.nombre),
                "stok": int(self.stok),
                "precio": float(self.precio)
            }]
        pass
    def mostrar_productos(self):
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
    def buscar_producto(self,nombre):
        for x in self.lista_productos:
            if x["nombre"]==nombre:
                print("-----------------------------\n" +

                    "#:\t\t\t" + str(x["id_producto"]) + "\n" +
                    "nombre:\t\t" + x["nombre"] + "\n" +
                    "precio:\t\t" + str(x["precio"]) + "\n" +
                    "disponibles:" + str(x["stok"]) + "\n" +
                    "-----------------------------\n")
            else:
                print("no se encontro el producto en el inventario")
        pass
    def editar_producto(self,buscar):
        for x in self.lista_productos:
            if x["nombre"]== buscar:
                print("que desea modificar:\n"
                      "1.nombre\n2.precio\n3.stock")
                mod_op=input("seleccion:")
                if mod_op=="1":
                    x["nombre"]=input("ingrese el nuevo nombre:\t")
                elif mod_op=="2":
                    x["precio"]=input("ingrese el nuevo precio:\t")
                elif mod_op=="3":
                    x["stok"]=input("ingrese la nueva cantidad en inventario:\t")
            else:
                print("no se encontro el producto")
        pass
    def EliminarProducto(self,buscar):
        d=-1
        for x in self.lista_productos:
            d+=1
            if x["id_producto"]== buscar:
                del self.lista_productos[d]
                print("producto eliminado")
            else:
                print("no se encontro el producto")
            pass
        pass
"""
p=Producto()
p.agregar_producto()
print(p.lista_productos[0])
p.mostrar_productos()
p.buscar_producto("prueba")
xd=input("buscar:")
p.editar_producto(xd)
p.mostrar_productos()
c=input("producto a eliminar:\t")
p.EliminarProducto(c)
p.mostrar_productos()
"""