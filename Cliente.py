class Cliente:
    def __init__(self, nome, endereco, cpf, id=None):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__id = id
    
    @property
    def nome(self):  
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        if self.cpfValido(cpf):
            self.__cpf = cpf
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
        
    def cpfValido(self, cpf):
        return len(cpf) == 11