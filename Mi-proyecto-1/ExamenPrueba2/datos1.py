import psycopg2

conexion1= psycopg2.connect(database="dvdrental", user="postgres", password="PostgreSqlAdmin")
cursor1=conexion1.cursor()

sql="select film_id,description FROM film WHERE title like '%a'"
cursor1.execute(sql)
resultados=cursor1.fetchall()
cont=0
peliculas={}

for numero,descripcion in resultados:
    cont=1+cont
    peliculas[numero]={descripcion}
    if cont==4:
        break

lista_tuplas=[]

for numero,descripcion in peliculas.items():
    lista_tuplas.append((numero,descripcion))



try:
    with open("peliculas.txt","w") as f:
        for numero,descripcion in lista_tuplas:
            f.write(f"{numero}>>{descripcion}\n")

except IOError as e:
    print("Error al escribir")
conexion1.close()
cursor1.close()





