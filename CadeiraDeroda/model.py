import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao() #Abrindo a conexao com o banco de dados
        self.db_connection = self.db_connection.conectar()#Método que realiza a conexão com BD
        self.con = self.db_connection.cursor() #Navegação no banco de dados

    def inserirD(self, nome, telefone, endereco, dataDeNascimento):
            try:
                sql = "insert into pessoa(codigo, nome, telefone, endereco, dataDeNascimento) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataDeNascimento)
                self.con.execute(sql)
                self.db_connection.commit()  # Insere o dado no banco de dados
                return "{} linha afetada".format(self.con.rowcount)
            except Exception as erro:
                return erro

    def inserirR(self, locall, numero, reclamacao):
        try:
            sql = "insert into reclamacao(codigo, locall, numero, reclamacao) values('','{}', '{}', '{}')".format(
                locall, numero, reclamacao)
            self.con.execute(sql)
            self.db_connection.commit()  # Insere o dado no banco de dados
            return "{} linha afetada".format(self.con.rowcount)
        except Exception as erro:
            return erro


    def selecionarD(self):
        try:
            sql = "select * from pessoa"
            self.con.execute(sql)  # Devolve os dados salvos
            msgD = ""
            for (codigo, nome, telefone, endereco, dataDeNascimento) in self.con:
                msgD += "\nCoódigo: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}".format(codigo, nome,  telefone,  endereco, dataDeNascimento)
            return msgD

        except Exception as erro:
            return erro

    def selecionarR(self):
        try:
            sql = "select * from reclamacao"
            self.con.execute(sql)  # Devolve os dados salvos
            msgR = ""
            for (codigo, locall, numero, reclamacao ) in self.con:
                msgR += "\nCoódigo: {}, locall: {}, numero: {}, reclamacao: {}".format(codigo, locall, numero, reclamacao)
            return msgR

        except Exception as erro:
            return erro

    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha(s) atualizada(s)!".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def excluir(self, cod):
        try:
            sql = "delete from pessoa where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            print("{} linha(s) excluída(s)!".format(self.con.rowcount))
        except Exception as erro:
            return erro

