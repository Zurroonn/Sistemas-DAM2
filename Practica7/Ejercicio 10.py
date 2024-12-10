from datetime import datetime
from contextlib import nullcontext
from sys import excepthook

import  psycopg2
from psycopg2 import DATETIME
try:
    conexion= psycopg2.connect(dbname="dvdrental",user="postgres",password="PostgreSqlAdmin")

    cursor=conexion.cursor()
    """
    print("Conexion establecida")
    cliente=int(input("Introduce id del cliente"))
    nombre=input("Introduce nombre del cliente")
    email=input("Introduce email del cliente")
    fecha=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    clientedata=(cliente,4,nombre,"Zurron",email,5,"True",fecha,fecha,0)

    cursor.execute(f'INSERT INTO customer values {clientedata}')
    cursor.execute(f"UPDATE customer SET email='cliente@servidor.com' WHERE customer_id=10000")
    """
    cursor.execute("SELECT * FROM customer")
    for linea in cursor.fetchall():
        print(linea)

    conexion.commit()
except Exception:
    print("Algo salio mal")
    conexion.rollback()

conexion.close()
