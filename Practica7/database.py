import psycopg2

conexion=psycopg2.connect(dbname="dvdrental",user="postgres",password="PostgreSqlAdmin")

cursor=conexion.cursor()
print("Conexión establecida con la base de datos 'dvdrental'")

cliente=int(input("\n Introduce el id del cliente"))
nombre=input("\n Introduce el nombre del cliente")
apellido=input("\n Introduce el apellido del cliente")
email=input("\n Introduce el email del cliente")
store=1
address_id=1
data=(cliente,store,address_id,nombre,apellido,email)

print(data)

insertar="""INSERT INTO customer (customer_id,store_id,address_id,first_name,last_name,email) VALUES (%s, %s, %s,%s,%s,%s);"""
cursor.execute(insertar,data)
print("Insertado")