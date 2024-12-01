
def cuantos(x,y="§"):
    try:
        assert not (isinstance(y, (int, float)) and y > 5), "El segundo parámetro no debe ser mayor de 5."
        match x:
            case (a,b,c,d):
                resultado= a+b+c+d
            case (a,b,c):
                resultado= (a*b)/c
            case (a,b):
                resultado= a/b
            case _:
                raise AssertionError ("Error: El parametro no es una tupla valida")
        print ("No existen errores")
        return resultado

    except ZeroDivisionError as e:
        return  "No se puede dividir entre 0"
    except AssertionError as e:
        return "El segundo parametro es mayor que 5"
    except TypeError as e:
        return "Division no admitida por sus valores"
    except Exception as e:
        return "Ocurrio un error: "
    finally:
        print("Programa terminado")

print(cuantos((1,2,3,4),3))
print(cuantos((10,5,2),"Texto"))
print(cuantos((20,5)))



