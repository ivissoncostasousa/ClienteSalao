from tkinter import *

class CadastroCliente:
    def __init__(self, master=None):
        
        ###### primeiroContainer ######
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        ###### segundoContainer ######
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        ###### terceiroContainer ######
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        ###### quartoContainer ######
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()
        
        ###### quintoContainer ######
        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()
        
        ###### sextoContainer ######
        self.sextoContainer = Frame(master)
        self.sextoContainer["padx"] = 20
        self.sextoContainer.pack()

        ###### primeiroContainer ######
        self.titulo = Label(self.primeiroContainer, text="Cadastro de Clientes")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        
        ###### segundoContainer ######
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=TOP)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        ###### terceiroContainer ######
        self.cpfLabel = Label(self.terceiroContainer, text="CPF", font=self.fontePadrao)
        self.cpfLabel.pack(side=TOP)

        self.cpf = Entry(self.terceiroContainer)
        self.cpf["width"] = 30
        self.cpf["font"] = self.fontePadrao
        #self.senha["show"] = "*"
        self.cpf.pack(side=LEFT)
        
        ###### quartoContainer ######
        self.enderecoLabel = Label(self.quartoContainer, text="Endereço", font=self.fontePadrao)
        self.enderecoLabel.pack(side=TOP)

        self.endereco = Entry(self.quartoContainer)
        self.endereco["width"] = 30
        self.endereco["font"] = self.fontePadrao
        #self.senha["show"] = "*"
        self.endereco.pack(side=LEFT)
        
        
        ###### quintoContainer ######
        self.cadastrar = Button(self.quintoContainer)
        self.cadastrar["text"] = "Cadastrar"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 12
        # self.cadastrar["command"] = self.cadastrarAtleta
        self.cadastrar.pack()

        ###### sextoContainer ######
        self.mensagem = Label(self.sextoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()
        
