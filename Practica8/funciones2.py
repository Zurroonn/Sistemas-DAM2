#CLAUSURA
def calcular_area (figura):
    def calcular(base,altura):
        if figura=="rectangulo":
            return base*altura
        elif figura=="triangulo":
            return (base*altura)/2
        else:
            return None
    return calcular

caTriangulo=calcular_area("triangulo")
area=caTriangulo(12,7)
#--------------------------------------------
#LAMBDA
fResto= lambda x,y:x%y
#--------------------------------------------
#DECORADORA
def mayusculas(func):
    def wrapper(*args,**kwargs):
        resultado=func(*args,**kwargs)
        return resultado.upper()
    return wrapper

@mayusculas
def concatena (tex1,tex2):
    return tex1+tex2
#--------------------------------------------
#RECURSIVA
def potencia(base,exponente,limite):
    if base ** exponente>limite:
        return exponente-1
    else:
        return potencia(base,exponente+1,limite)
# --------------------------------------------
#VALORES GLOBALES
def por5 (int):
    global valor
    valor = int * 5
    return valor

valor=18
por5(valor)
