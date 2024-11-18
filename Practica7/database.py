import psycopg2

conexion=psycopg2.connect(dbname="dvdrental",user="postgres",password="PostgreSqlAdmin")

cursor=conexion.cursor()
print("Conexión establecida con la base de datos 'dvdrental'")

duracion=int(input("Introduce duracion peliculas:"))

consulta="""SELECT title, special_features, length FROM film WHERE length < %s;"""
cursor.execute(consulta,(duracion,))

primer_registro=cursor.fetchone()
if primer_registro:
    print(primer_registro[0])
    print(primer_registro[1])
    print(primer_registro[2])





