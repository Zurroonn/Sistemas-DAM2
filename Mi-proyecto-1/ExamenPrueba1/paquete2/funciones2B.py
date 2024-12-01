def ceros(func):
    def wrapper(cadena):
        resultado = func(cadena)
        # Contar las 'O' en el resultado
        cantidad_o = resultado.count('O')
        print(f"Número de caracteres 'O': {cantidad_o}")
        return resultado

    return wrapper

@ceros
def limpiar (cadena):
    return cadena.lstrip('0')

cadena_original = "0001O2O03O4"
cadena_limpiada = limpiar(cadena_original)
print(f"Cadena original: {cadena_original}")
print(f"Cadena limpiada: {cadena_limpiada}")