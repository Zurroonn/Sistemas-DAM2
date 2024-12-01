def verdad(*lista):
    cont1=0
    cont2=0
    for i in lista:
        if i==True:
           cont1=cont1+1
        elif i==False:
            cont2=cont2+1
    return [cont1,cont2]

producto= lambda x,y,z:x*y*z
doble=lambda lista:lista*2



