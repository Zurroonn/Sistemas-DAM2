import psycopg2

with open("registros.txt","w") as archivo:
    archivo.write("604:Alejandro:Zurron\n")
    archivo.write("605:Jeronimo:Gordito\n")
    archivo.write("606:AleJero:Nobios\n")

lista_tuplas=[]

with open("registros.txt","r")as archiv:
    for linea in archiv:
        elementos=linea.strip().split(":")
        numero=elementos[0]
        nombre=elementos[1]
        apellido=elementos[2]
        lista_tuplas.append((numero,nombre,apellido))

conexion1 = psycopg2.connect(database="dvdrental", user="postgres", password="PostgreSqlAdmin")
cursor1=conexion1.cursor()
sql="insert into actor(actor_id,first_name,last_name) values(%s,%s,%s);"
try:
    for lista in lista_tuplas:
        numero,nombre,apellido=lista
        print(f"{float(numero):06.2f},{nombre:^10},{apellido}")
        datos=(numero,nombre,apellido)
        cursor1.execute(sql,datos)
        conexion1.commit()
except Exception as e:
    print("Error ocurrido "+ e)
    conexion1.rollback()

except psycopg2.errors.UniqueViolation as e:
    # Manejo de violación de clave primaria (duplicado)
    print("Error de duplicado en la base de datos: " + str(e))
    conexion1.rollback()
finally:
    cursor1.close()