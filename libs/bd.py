import mysql.connector

conn = mysql.connector.connect(user='root',password='password',host='localhost',database='banco')

cursor = conn.cursor()

query = ("select * from clientes")


cursor.execute(query)

for registro in cursor:
    print('ID: ',registro[0])
    print('Nome: ',registro[1])
    print('Data Nascimento: ',registro[2])
    print('Endereço: ',registro[3])
    print('CPF: ',registro[4])
    print('Profissão: ',registro[5])