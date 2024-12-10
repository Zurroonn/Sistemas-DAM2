texto=input("Introduce dato")
encontrado=False
indice =0
encontrados=()
while indice<len(texto):
    if texto[indice].isdigit():
        encontrado=True
        encontrados+=(int(texto[indice]),)

    indice+=1
if encontrado:
    print(encontrados)
else:
    print("No se ha encontrado")