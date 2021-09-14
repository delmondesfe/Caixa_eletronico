from libs import cliente


print('Digite a escolha\n 1- cadastrar novo cliente \n 2- Consultar todos os cadastros')
opt = int(input('Escolha: '))

if opt ==1:
    cliente.Cliente.cadastra_cliente()

elif opt ==2:
    print('Consulta do Cliente, favor digite o CPF: ')
    cliente.Cliente.consulta_totos_os_registros()
else:
    print('Escolha invalida')
