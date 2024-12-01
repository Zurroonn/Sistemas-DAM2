from Practica8.funciones1 import  mayor, suma
from Practica8.funciones2 import calcular_area as c_area, potencia as pot

from Practica8.objetosYclase2 import vAcuatico

##print(mayor(647,1111))

num=(20,56,15,89)
##print(suma(*num))

rect=c_area("rectangulo")
##print(rect(9,6))

##print(pot(7,1,5000))

DeAgua= vAcuatico("kayak",False,"parado",2.90,300)
DeAgua.mover()
##print(DeAgua.estado)