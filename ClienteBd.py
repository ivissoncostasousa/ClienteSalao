from mysql.connector.errors import Error
from model.Cliente import Cliente

class ClienteBd:
    def __init__(self, conexao):
        self.conexao = conexao
        
    def inserirCliente(self,cliente):
        try:
            cursor = self.conexao.cursor()
            sql = 'insert into cliente (nome, cpf, endereco) values (%s, %s, %s)'
            cursor.execute(sql, (cliente.nome, cliente.cpf, cliente.endereco ))
            print(cliente.nome)
            print(sql)
            self.conexao.commit()
        except Error as e:
            return e
        
    def listarClientes(self):
        listaClientes = []
        try:
            cursor = self.conexao.cursor()
            sql = 'SELECT * FROM cliente'
            cursor.execute(sql)
            for c in cursor:
                cliente = Cliente(c[1], c[3], c[2], c[0])
                listaClientes.append(cliente)
            return listaClientes, None
        except Error as e:
            return None,e
        
    def atualizarCliente(self, cliente):
        try:
            cursor = self.conexao.cursor()
            sql = 'update cliente set nome=%s, cpf=%s, endereco=%s where idcliente = %s'
            cursor.execute(sql, (cliente.nome, cliente.cpf, cliente.endereco, cliente.id))
            self.conexao.commit()
        except Error as e:
            return e
        
    def excluirCliente(self, id):
        try:
            cursor = self.conexao.cursor()
            sql = 'delete from cliente where idcliente = %s'%id
            cursor.execute(sql)
            self.conexao.commit()
        except Error as e:
            return e



