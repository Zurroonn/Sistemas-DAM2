class perro:
    def __init__(self,nombreOculto,edad,color,dueno,numperros):
        self._nombreOculto=nombreOculto
        self.edad=edad
        self.color=color
        self.dueno=dueno
        self.numperros=0
        perro.numperros=numperros+1

    @property
    def nombre(self):
        return self._nombreOculto
    @nombre.setter
    def nombre(self,value):
        self.nombre=value

    @property
    def numperros(self):
        return self.numperros()
    @numperros.setter
    def numperros(self, value):
        self._numperros = value

    def datos(self):
        dog=(self.color,self.dueno)
        return dog

class galgo(perro):
    def __init__(self, nombreOculto, edad, color, dueno, numperros,velocidad,peso):
        super().__init__(nombreOculto, edad, color, dueno, numperros)
        self.velocidad=velocidad
        self.peso=peso

    def datos(self):
        valores=(*super().datos(),self.velocidad)
        return valores

    def __lt__(self, other):
        if isinstance(other,galgo):
            return self.peso+self.peso
        return NotImplemented

