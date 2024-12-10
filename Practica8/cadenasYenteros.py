hijos=input("Introduce numero de hijos")
año=input("Introduce año")
res=input("Pasar hijos a enteros Y/N")
if res=="Y":
    hijos=int(hijos)

res2=input("Pasar año a entero Y/N")
if res2=="Y":
    año=int(año)

match (hijos,año):
    case (str(),str()):
        input("Se transformaron los datos a enteros")
        año = int(año)
        hijos = int(hijos)
    case (int(),str()):
        input("Se transformo año a int")
        año = int(año)
    case (str(),int()):
        input("Se transformo hijos a int")
        hijos=int(hijos)
    case (int(),int()):
        print("Multiplicacion")
        print(hijos*año)