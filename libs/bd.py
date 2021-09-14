import mysql.connector

conn = mysql.connector.connect(user='root',password='password',host='localhost',database='banco')

cursor = conn.cursor()

query = ("select * from clientes")


cursor.execute(query)

for registro in cursor:
    print(registro)