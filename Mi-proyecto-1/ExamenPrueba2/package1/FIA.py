def nombres():
    listanombres =()
    contA=0
    contNA=0
    nombre=input("Introduce un nombre")
    while nombre!="":
        listanombres=listanombres+(nombre,)
        if nombre.lower().__contains__("a"):
            contA=contA+1
        else:
            contNA=contNA+1
        nombre=input("Introduce un nombre")
    return (f"Estos nombres contienen {contA}y no contienen {contNA}")

juntar=lambda x,y,z:(z+y+x)

import sys
parametros = lambda: sys.argv[::-1]