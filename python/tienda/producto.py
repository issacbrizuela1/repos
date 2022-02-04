class producto:
    def __init__(self, id, nombre, stok, precio):
        self.id = id
        self.nombre = nombre
        self.stok = stok
        self.precio_u = precio
        self.lista_productos = []
        pass
    def agregar_producto(self):
        ids=self.id+1
        nombre = input("nombre del producto:\t")
        stok = input("cantidad en almacen:\t")
        precio = input("precio que tendra el producto:\t")
        self.lista_productos = [{"id": ids, "nombre": str(nombre), "stok": int(stok), "precio": float(precio)}]
        pass
    def mostrar_productos(self):
        for x in self.lista_productos:
            print(x)
        pass
    def buscar_producto(self):

        pass
    pass
