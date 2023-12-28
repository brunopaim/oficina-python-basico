class Cliente:
    def __init__(self, nome, cpf, endereco, fone):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__fone = fone

    # Métodos de acesso (getters)
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_endereco(self):
        return self.__endereco

    def get_fone(self):
        return self.__fone

    # Métodos de modificação (setters)
    def set_nome(self, nome):
        self.__nome = nome

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_fone(self, fone):
        self.__fone = fone

    def __str__(self):
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Endereço: {self.__endereco}, Telefone: {self.__fone}"