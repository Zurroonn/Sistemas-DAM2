class vehiculo:
    total = int(0)
    def __init__(self, nombre, tiene_motor, estado, longitud, precio):
        self._nombreOculto = nombre
        self._tieneMotor = tiene_motor
        self._estado = estado
        self._longitud = longitud
        self.__precio = precio
        vehiculo.total += precio


    @property
    def nombre(self):
        return self._nombreOculto

    @nombre.setter
    def nombre(self,valor):
        self._nombreOculto=valor

    @property
    def tieneMotor(self):
        # Getter para la propiedad 'tieneMotor'
        return self._tieneMotor

    @tieneMotor.setter
    def tieneMotor(self, valor):
        # Setter para la propiedad 'tieneMotor'
        self._tieneMotor = valor

    @property
    def estado(self):
        # Getter para la propiedad 'estado'
        return self._estado

    @estado.setter
    def estado(self, valor):
        # Setter para la propiedad 'estado'
        self._estado = valor

    @property
    def longitud(self):
        # Getter para la propiedad 'longitud'
        return self._longitud

    @longitud.setter
    def longitud(self, valor):
        # Setter para la propiedad 'longitud'
        self._longitud = valor

    @property
    def peso(self):
        # Getter para la propiedad 'peso', que se calcula
        return self._longitud *3

    @property
    def peso(self):
        # Getter para la propiedad 'peso', que se calcula
        return self._longitud * 3
    def mover (self): #METODO DE INSTANCIA
        self._estado="moviendose"
    def parar(self):
        self._estado="parado"
    def peso(self):
        return self._longitu*3
    @classmethod
    def gasto(cls):#METODO DE CLASE
        print("Gasto total = "+str(cls.total))
    @staticmethod #STATIC METODO
    def informar():
        print("La clase ‘vehiculo’ sirve para crear todo tipo de vehículos")
    def __gt__ (self,other): #METODO MAGICO
        if isinstance(other,vehiculo):
            if self._longitud>other._longitud:
                return "El primer vehiculo es mas largo"
            elif self._longitud<other._longitud:
                return "El segundo vehiculo es mas largo"
            else:
                return "Tienen misma longitud"
        return NotImplemented

v1=vehiculo("coche",True,"parado",3.79,19000)
v2=vehiculo("bicicleta",False,"parado",1.40,120)
v3=vehiculo("barco",True,"parado",8.55,678000)

v1.mover()
v2.mover()

v1.nombre="turismo"
#v3.informar()
#v2.gasto()

v1.parar()

print(vehiculo.__gt__(v2,v3))