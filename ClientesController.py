from model.Cliente import Cliente
from data.ClienteBd import ClienteBd
from data.Connect import Connect


class ClientesController:
    def __init__(self, cadastroCliente):
        self.cadastroCliente = cadastroCliente
    
        self.cadastroCliente.cadastrar["command"] = self.validarDadosCliente
        
    def validarDadosCliente(self):
        nome = self.cadastroCliente.nome.get()
        cpf = self.cadastroCliente.cpf.get()
        endereco = self.cadastroCliente.endereco.get()
        cliente = Cliente(nome, endereco, cpf)
        if not cliente.cpfValido(cpf):
            self.cadastroCliente.mensagem["text"] = "CPF inválido!"
        else:
            if nome == "":
                self.cadastroCliente.mensagem["text"] = "Nome não pode ser vazio!"
            else:
                con = Connect()
                c, ok = con.conectar()
                if ok:
                    clientebd = ClienteBd(c)
                    clientebd.inserirCliente(cliente)
                    self.cadastroCliente.mensagem["text"] = "Deu tudo certo!"
                else:
                    self.cadastroCliente.mensagem["text"] = "Estamos tendo problemas com o banco, tente mais tarde!"
                    print("Erro: ", c)