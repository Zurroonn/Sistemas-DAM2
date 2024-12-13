import psycopg2

from Practica7.database import cursor, conexion

conexion1 = psycopg2.connect(dbname="dvdrental", user="postgres", password="PostgreSqlAdmin")
sql = "select title, film from film where 100<length<120"
cursor1 = conexion1.cursor()
cursor1.execute(sql)
for f in cursor1:
    print(f)

conexion1.close()
cursor1.close()