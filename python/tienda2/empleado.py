from datetime import date

from persona import Persona


class Empleado(Persona):
    id_em = 0
    fecha = ""
    lista_personal = []
    def __init__(self, id, nombre, apellido):
        super().__init__(id, nombre, apellido)
        self.id
        self.nombre
        self.apellido
        self.tipo_p = self.tipo[1]
    def agregar_personal(self):
        self.id+= 1
        self.id_em+=1
        self.fecha=str(date.today())
        nombre = input("primer y segundo nombre :\t")
        apellido = input("apellidos :\t")
        self.lista_personal.append(
            {
                "id_em":int(self.id_em),
                "id": int(self.id),
                "nombre": str(nombre),
                "apellido": str(apellido),
                "tipo": str(self.tipo[1]),
                "fecha":str(self.fecha)
            })
        pass
    def mostrar_personal(self):
        for x in self.lista_personal:
            print(x)
        pass
    def buscar_persona(self, nombre):
        for x in self.lista_personal:
            if x["nombre"] == nombre:
                print("-----------------------------\n" +
                      "nombre:\t\t" + x["nombre"] + "\n" +
                      "apellido:\t\t" + str(x["apellido"]) + "\n" +
                      "tipo:" + str(x["tipo"]) + "\n" +
                      "-----------------------------\n")
            else:
                print("no se encontro el producto")
        pass
        pass
    def editar_persona(self, buscar):
        for x in self.lista_personal:
            if x["nombre"] == buscar:
                print("que desea modificar:\n"
                      "1.nombre\n2.apellido")
                mod_op = input("seleccion:")
                if mod_op == "1":
                    x["nombre"] = input("ingrese el nuevo nombre:\t")
                elif mod_op == "2":
                    x["apellido"] = input("ingrese el nuevo apellido:\t")
            else:
                print("no se encontro el producto")
        pass
    def EliminarPersona(self, buscar):
        d = -1
        for x in self.lista_personal:
            d += 1
            if x["nombre"] == buscar:
                del self.lista_personal[d]
                print("producto eliminado")
            else:
                print("no se encontro el producto")
            pass
        pass