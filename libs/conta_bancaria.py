from cliente import Cliente

class Conta(Cliente):
    def __initi__(self, agencia = '001', conta = '',saldo = 0):
        self.agencia = agencia
        self.conta_corrente = conta
        self.__saldo = saldo
        self.cpf = self.cpf


    def extrato(self):
        return self.__saldo
    
    def deposita(self, valor):
        valor = self.__saldo
        return 'Valor depositado com sucesso'

    def saque(self, valor):
        if valor > self.__saldo:
            print('Saldo indiponível')
        else:
            return valor - self.__saldo