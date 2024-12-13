from paquete2.funciones2A import  verdad

class animal:
    num_animales=0
    def __init__(self,nombre,orden,continentes,alimentacion):
        self.nombre=nombre
        self.orden=orden
        self.continentes=continentes
        self.alimentacion=alimentacion
        animal.num_animales=animal.num_animales +1

    def datos (self):
        print(f"[DEBUG]{self.nombre},{self.orden},{self.alimentacion}")

    def comprobar_continentes(self):
        return verdad(self.continentes)

class perro(animal):
    def __init__(self, nombre, orden, continentes, alimentacion, num_animales, pedigri):
        super().__init__(nombre, orden, continentes, alimentacion, num_animales)
        self.pedigri=pedigri
    @property
    def pedigri(self):
        return self.pedigri

    @pedigri.setter
    def pedigri(self, value):
        self._pedigri = value

    def datos(self):
        animal.datos()
        print(f"{self.pedigri=}")

    def __lt__(self, other):
        if isinstance(other, perro):
            return not self.pedigri and other.pedigri
        return NotImplemented

