class Vehiculo():
    def __init__(self,color,carga,ruedas,ancho,alto,asientos,estado):
        self.color=color
        self.carga=carga
        self.ruedad=ruedas
        self.ancho=ancho
        self.alto=alto
        self.asientos=asientos
        self.estado=estado

    def arrancar(self):
        self.estado="Vehiculo arrancando"

    def acelerar(self):
        self.estado="Vehiculo acelerando"

    def frenar(self):
        self.estado="Vehiculo frenando"

    def cargar(self,value):
        self.carga=self.carga+value

    def girar(self):
        self.estado="Vehiculo girando"

    def atras(self):
        self.estado="Vehiculo retrocediendo"

class Furgoneta(Vehiculo):
    def __init__(self, color, carga, ruedas, ancho, alto, asientos, marchas, aire,estado):

        super().__init__(color, carga, ruedas, ancho, alto, asientos,estado)
        self.marchas=marchas
        self.aire=aire


class Bicicleta(Vehiculo):
    def saltar(self):
        self.estado="Bici saltando"


class Coche(Vehiculo):
    def __init__(self, color, carga, ruedas, ancho, alto, asientos, marchas, aire,estado):
        super().__init__(color, carga, ruedas, ancho, alto, asientos,estado)
        self.marchas = marchas
        self.aire = aire


class Moto(Vehiculo):
    def __init__(self, color, carga, ruedas, ancho, alto, asientos,cilindrada,estado):
        super().__init__(color, carga, ruedas, ancho, alto, asientos,estado)
        self.cilindrada=cilindrada

    def derrapar(self):
        self.estado="Moto derrapando"


furgoneta1=Furgoneta("Azul",200,4,2,4,5,6,"Si","parado")
bicicleta1=Bicicleta("Roja",0,2,0.5,1,1,"parado")
coche1=Coche("Negro",50,4,2,3,5,6,"No","parado")
moto1=Moto("Blanco",0,2,0.5,1,2,"Si","parado")

furgoneta1.girar()
print(furgoneta1.estado)
bicicleta1.saltar()
print(bicicleta1.estado)
coche1.acelerar()
print(coche1.estado)
moto1.derrapar()
print(moto1.estado)
print(furgoneta1.carga)
furgoneta1.cargar(400)
print(furgoneta1.carga)

