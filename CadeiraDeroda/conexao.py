import mysql.connector #elemento que faz a conexao com o banco de dados
from mysql.connector import errorcode #importando a classe para tratar erro com o banco de dados

class conexao:
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='reclamacao')
            print('Conectado com sucesso!')
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR: #Caso o banco de dados nao exista; errno é uma variavel interna da classe
                                                         #importada mysql.connector
                print("Banco de dados não existe!\nErro: {}".format(erro))
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR: #Há um erro de usuario:
                print("Nome de usuário ou senha inválido!\nErro: {}".format(erro))
            else:
                print(erro)
        else:
            self.db_connection.close() #Fechando a conxão com o banco de dadosS_DENIED_ERROR:
