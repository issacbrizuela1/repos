from self import self
class Persona:
    tipo=["cliente","empleado"]
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_p = self.tipo[0]
        self.lista_personas = []
        pass
    def agregar_persona(self):
        self.id+= 1
        nombre = input("primer y segundo nombre :\t")
        apellido = input("apellidos :\t")
        tipo = 0
        self.lista_personas.append(
            {
                "id": int(self.id),
                "nombre": str(nombre),
                "apellido": str(apellido),
                "tipo": str(self.tipo[tipo])
            })
        pass
    def mostrar_persona(self):
        for x in self.lista_personas:
            print(x)
        pass
    def buscar_persona(self,nombre):
        for x in self.lista_personas:
            if x["nombre"]==nombre:
                print("-----------------------------\n" +
                    "nombre:\t\t" + x["nombre"] + "\n" +
                    "apellido:\t\t" + str(x["apellido"]) + "\n" +
                    "tipo:" + str(x["tipo"]) + "\n" +
                    "-----------------------------\n")
            else:
                print("no se encontro el producto")
        pass
        pass
    def editar_persona(self,buscar):
        for x in self.lista_personas:
            if x["nombre"]== buscar:
                print("que desea modificar:\n"
                      "1.nombre\n2.apellido")
                mod_op=input("seleccion:")
                if mod_op=="1":
                    x["nombre"]=input("ingrese el nuevo nombre:\t")
                elif mod_op=="2":
                    x["apellido"]=input("ingrese el nuevo apellido:\t")
            else:
                print("no se encontro el producto")
        pass
    def EliminarPersona(self,buscar):
        d=-1
        for x in self.lista_personas:
            d+=1
            if x["nombre"]== buscar:
                del self.lista_personas[d]
                print("producto eliminado")
            else:
                print("no se encontro el producto")
            pass
        pass
    pass
"""
P=Persona(0,"","")
P.agregar_persona()
P.buscar_persona("p")
P.mostrar_persona()
"""