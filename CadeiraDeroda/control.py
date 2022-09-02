from model import model

class control:
    def __init__(self):
       self.opcao = -1
       self.opcao1 = -1
       self.modelo = model()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def getOpcao1(self):
        return self.opcao1

    def setOpcao1(self, opcao1):
        self.opcao1 = opcao1


    def menu(self):
        print("Escolha um das opçoes abaixo: \n "   +
              "\n0.Sair "                           +
              "\n01.cadastrar"                       +
              "\n02.cadastrar reclamação"            +
              '\n03.Atualizar dados'                 +
              "\n09.Excluir")
        self.setOpcao(int(input()))

    def menuA(self):
        print("Escolha um das opçoes abaixo: \n " +
              "\n04.atualizar Nome " +
              "\n05.atualizar Telefone" +
              "\n06.atualizar endereco" +
              "\n07.Atualizar data de nascimento" +
              "\n08. Menu principal")
        self.setOpcao1(int(input()))

    def operacoes(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrarD()
            elif self.getOpcao() == 2:
                self.cadastrarR()
            elif self.getOpcao() == 3:
                self.operacoes1()
            elif self.getOpcao() == 9:
                self.excluir()
            else:
                print("Opção inválida! Tente novamente.")

    def operacoes1(self):
        while self.getOpcao() != 0:
            self.menuA()
            if self.getOpcao1() == 4:
                self.atualizarNome()
            elif self.getOpcao1() == 5:
                self.atualizarTelefone()
            elif self.getOpcao1() == 6:
                self.atualizarEndereco()
            elif self.getOpcao1() == 7:
                self.atualizarData()
            elif self.getOpcao1() == 8:
                self.menu()
            else:
                print("Opção inválida! Tente novamente.")

    def cadastrarD(self):
        print('Informe seu Nome: ')
        nome = input()
        print('Informe seu telefone: ')
        telefone = input()
        print('Informe seu endereço: ')
        endereco = input()
        print('Informe a sua data de nascimento: ')
        dataDeNascimento = input()
        print(self.modelo.inserirD(nome, telefone, endereco, self.transformarData(dataDeNascimento)))

    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)

    def cadastrarR(self):
        print('Informe o local: ')
        locall = input()
        print('Informe O numero: ')
        numero = input()
        print("Iforme a sua reclamação: ")
        reclamacao = input()
        print(self.modelo.inserirR(locall, numero, reclamacao))

    def atualizarNome(self):
        print("Informe o código do dado que será atualizado:")
        codigo = int(input())
        print("Informe o novo nome:")
        name = input()
        print(self.modelo.atualizar("nome", name, codigo))

    def atualizarTelefone(self):
        print("Informe o código do dado que será atualizado:")
        codigo = int(input())
        print("Informe o novo telefone:")
        tel = input()
        print(self.modelo.atualizar("telefone", tel, codigo))

    def atualizarEndereco(self):
        print("Informe o código do dado que será atualizado:")
        codigo = int(input())
        print("Informe o novo endereço:")
        end = input()
        print(self.modelo.atualizar("endereco", end, codigo))

    def atualizarData(self):
        print("Informe o código do dado que será atualizado:")
        codigo = int(input())
        print("Informe  a nova data de nascimento:")
        data = self.transformarData(input())
        print(self.modelo.atualizar("dataDeNascimento", data, codigo))

    def excluir(self):
        print("Informe o código do dado que deseja excluir:")
        cod = int(input())
        print(self.modelo.excluir(cod))


