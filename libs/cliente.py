from logging import exception
import mysql.connector
from mysql.connector.errors import DataError

conn = mysql.connector.connect(user='root',
                               password='password',
                               host='localhost',
                               database='banco')
cursor = conn.cursor()



class Cliente:
    def __init__(self, nome = '', data_nascimento = '', endereco = '', cpf = '', profissao= ''):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao


def cadastra_cliente():
    nome = str(input('Nome: '))
    data_nascimento = str(input('Data Nascimento: '))
    endereco = str(input('Endereço: '))
    cpf = str(input('CPF: '))
    profissao = str(input('Profissão: '))

    cli = Cliente(nome, data_nascimento, endereco, cpf, profissao)

    try:

        add_cliente = ("INSERT INTO clientes"
                    "(nome, data_nascimento,endereco,cpf,profissao)"
                    "VALUES(%s,%s,%s,%s,%s)")

        dados_cliente = (cli.nome,cli.data_nascimento,cli.endereco,cli.cpf,cli.profissao)

        cursor.execute(add_cliente,dados_cliente)
        emp_no = cursor.lastrowid
        conn.commit()
    except DataError:
        print('Por favor revisar os dados digitados.')


     
        
    