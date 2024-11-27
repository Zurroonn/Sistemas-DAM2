class vehiculo:
    total=0
    def __init__(self, nombre, tiene_motor, estado, longitud, precio):
        self._nombreOculto = nombre  # Atributo privado para nombre
        self._tieneMotor = tiene_motor  # Atributo privado para el motor
        self._estado = estado  # Atributo privado para el estado
        self._longitud = longitud  # Atributo privado para la longitud
        self.__precio = precio  # Atributo privado y oculto para el precio
        vehiculo.total += precio  # Actualizar el gasto total con el precio del vehículo

    @property
    def nombre(self):
        return self._nombreOculto

    @nombre.setter
    def nombre(self, valor):
        self._nombreOculto = valor

    @property
    def tieneMotor(self):
        return self._tieneMotor

    @tieneMotor.setter
    def tieneMotor(self, valor):
        self._tieneMotor = valor

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    @property
    def longitud(self):
        return self._longitud

    @longitud.setter
    def longitud(self, valor):
        self._longitud = valor

    @property
    def peso(self):
        return self._longitud * 3

    @peso.setter
    def peso(self, valor):
        self._peso = valor

    @classmethod
    def gasto(cls):  # cls es la convención para referirse a la clase
        print(str(cls.total))

    @staticmethod
    def informar():
        print("La clase 'vehiculo' sirve para crear todo tipo de vehículos")

    def mover (self):
        self._estado="moviendose"

    def parar (self):
        self._estado="parandose"

    def __gt__(self, vehiculo2):
        return self.longitud > vehiculo2.longitud



class vTerrestre(vehiculo):
    def mover (self):
        self._estado="rodando"
    def enganchar(self,entero):
        self._longitud=self.longitud+entero


class vAreo(vehiculo):
    def __init__(self, nombre, tiene_motor, estado, longitud, precio, altura):
        super().__init__(nombre, tiene_motor, estado, longitud, precio)
        self._altura = 1000
    def mover (self):
        self._estado="volando"
    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        self._altura = valor


class vAcuatico(vehiculo):
    def mover(self):
        self._estado = "navegando"

class vHibrido1(vTerrestre,vAcuatico):
    pass
class vHibrido2(vAreo,vAcuatico):
    pass
class reproductor():
    def __init__(self,nombre):
        self._nombre=nombre

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,valor):
        self._nombre=valor
    def cantar(self):

        print("Mi carro, me lo robaron...")

class turismo(vTerrestre):
    def __init__(self, nombre, tiene_motor, estado, longitud, precio,radio):
        super().__init__(nombre, tiene_motor, estado, longitud, precio)
        self._radio=radio
    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, nuevo_radio):
        self._radio = nuevo_radio



terrestre1=vTerrestre("camion",True,"parado",10.5,75000)
aereo1=vAreo("Boing 747",True,"parado",65.70,100000000,0)
acuatico1=vAcuatico("barca",False,"parado",3.90,400)

aereo1.mover()
acuatico1.mover()
terrestre1.enganchar(entero=9.15)

hibrido1=vHibrido1("anfibio",True,"parado",8.15,125000)
hibrido2=vHibrido2("hidroavion",True,"parado",15.60,50000,0)

hibrido1.mover()
hibrido2.mover()

reproduce=reproductor("MxOnda")
turismo1=turismo("Seat Ateca",True,"Parado",4.40,23000,reproduce)
turismo1.radio.cantar()



















