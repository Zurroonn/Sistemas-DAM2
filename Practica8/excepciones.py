import math
class noEsCadena(Exception):
    def __init__(self, variable):
        super().__init__(f"El dato {variable} no es de tipo cadena")
def compruebaCadenas(lista):
    for i in lista:
        if not isinstance(i,str):
            raise noEsCadena(i)
def resuelveEcuacion(a,b,c):
    try:
        assert a<=10
        #if a>10:
         #   raise AssertionErrorA
        if not all(isinstance(i,(int,float))for i in [a,b,c]):
            raise TypeError("Operacion no permitida para ese tipo de datos")
            return

        discriminante = b ** 2 - 4 * a * c

        if discriminante < 0:
            print("No hay soluciones reales")
        elif discriminante == 0:
            x = -b / (2 * a)
            print(f"La solución es: x = {x}")
        else:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            print("El programa ha podido calcular los resultados de la ecuación")
            print("Las soluciones son: "+str(x1)+str(x2))

    except AssertionError as e:
        print("Error de asercion",e)

    except TypeError as e:
        print(e)
    except noEsCadena as e:
        print(e)

    except Exception as e:
        print("Ocurrió algo y no se pudo realizar la operación.", e)
    finally:
        print("Funcion resuelveEcuacion finalizada")

#resuelveEcuacion(1,4,-5)
#resuelveEcuacion(1, -8, 16)
#resuelveEcuacion(	12, -4, 0 )
#resuelveEcuacion(5, "7", 9 )

cadenas=["lunes","martes","miercoles","jueves",4,"viernes","sabado","domingo"]
compruebaCadenas(cadenas)

