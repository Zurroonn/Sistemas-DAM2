from package1.FIA import juntar as glue
import package1.FIB as B

class Mayor(Exception):
    pass


def visualiza(y,x="10"):
    try:
        match x,y:

            case int(x),int(y):
                if x>y:
                    raise Mayor("El primer parametro es mayor que el segundo")
                else:
                    resultado=x/y
                    print(float(f"{resultado:08.3f}"))
            case str(x),str(y):
                cadena= x.upper()+y.upper()
                print (cadena)
            case _:
                raise TypeError
    except ZeroDivisionError as e:
        print("No se puede dividir entre 0")
    except Mayor as e:
        print(e)
    except TypeError as e:
        print("Los parametros tienen que ser dos enteros o dos cadenas de texto")
    except Exception as e:
        print("Ocurrio un error")
    finally:
        print("La función acaba aquí")

#visualiza(45,30)
#visualiza("hola","adios")
#visualiza("",15)

print(glue("one","two","three"))
print(B.ordenar([5,8,12,5,3]))
