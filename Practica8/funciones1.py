
def area(y,base=8):
    return base*y

def suma(*args):
    return sum(args)

def repetir(texto,veces=1):
    return texto*veces

def peque(diccionario):
    habitacion=min(diccionario,key=diccionario.get)
    return habitacion,diccionario[habitacion]
habitaciones = {
    "Cocina": 12,
    "Dormitorio": 15,
    "Baño": 6,
    "Salón": 20
}
habitacion, tamaño = peque(habitaciones)

def mayor(x,y):
    if x>y:
        return x
    elif y>x:
        return y
    else:
        return x
def funcion(func1, arg1, func2, arg2):
    return func1(*arg1), func2(*arg2)
resultado=funcion(mayor,(10,5),peque,(habitaciones,))
print(resultado)