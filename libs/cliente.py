from logging import exception
from os import execlp
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
        nome = (input('Nome: '))
        data_nascimento = input('Data Nascimento: ')
        endereco = input('Endereço: ')
        cpf = input('CPF: ')
        profissao = input('Profissão: ')

        cli = Cliente(nome, data_nascimento, endereco, cpf, profissao)

        try:

            add_cliente = ("INSERT INTO clientes"
                        "(nome, data_nascimento,endereco,cpf,profissao)"
                        "VALUES(%s,%s,%s,%s,%s)")

            dados_cliente = (cli.nome,cli.data_nascimento,cli.endereco,cli.cpf,cli.profissao)

            cursor.execute(add_cliente,dados_cliente)
            emp_no = cursor.lastrowid
            conn.commit()
            print('Cadastro realizado com sucesso !!')
        except DataError:
            print('Por favor revise os dados digitados e tenta novamente')
        except Exception as err:
            print('Erro desconhecido: ',err)

        
    def consulta_totos_os_registros():
        
        
        query = ("SELECT * FROM clientes")       

        cursor.execute(query)

        for registro in cursor:
            print('ID: ',registro[0])
            print('Nome: ',registro[1])
            print('Data Nascimento: ',registro[2])
            print('Endereço: ',registro[3])
            print('CPF: ',registro[4])
            print('Profissão: ',registro[5])





     
        
    