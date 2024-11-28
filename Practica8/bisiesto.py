
year=int((input("Introduce año")))
if  year is None:
    print ("Hay que poner un numero")
elif (year%4==0 and year&100!=0)  or (year % 400 == 0):
        print("Es bisiesto")
else:
    print("No es bisiesto")