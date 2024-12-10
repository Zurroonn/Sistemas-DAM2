def repetido(func):
    def wrapper(*args,**kwargs):
        lista=func(*args,**kwargs)
        for i in range(len(lista)):
            if lista[i] in lista [i+1:]:
                return True
                break
        return False
    return wrapper

@repetido
def ordenar (lista):
    return lista
