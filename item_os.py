class ItemOS:
    def __init__(self, tipoItem="", quantidade=0, peca=None, servico=None):
        self.__tipoItem = tipoItem
        self.__peca = None
        self.__servico = None
        self.__preco = 0
        self.__qtde = 0

        if peca is not None:
            self.__tipoItem = "P"
            self.__peca = peca
            self.__preco = peca.get_preco()
            self.__qtde = quantidade
        elif servico is not None:
            self.__tipoItem = "S"
            self.__servico = servico
            self.__preco = servico.get_preco()
            self.__qtde = 1

    # Métodos de acesso (getters)
    def get_tipo_item(self):
        return self.__tipoItem

    def get_peca(self):
        return self.__peca

    def get_servico(self):
        return self.__servico

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__qtde
    
    def __str__(self):
        if self.__tipoItem == "P":
            return f"Tipo: Peça, Descrição: {self.__peca.get_descricao()}, Preço: {self.__preco}, Quantidade: {self.__qtde}"
        elif self.__tipoItem == "S":
            return f"Tipo: Serviço, Descrição: {self.__servico.get_descricao()}, Preço: {self.__preco}, Quantidade: {self.__qtde}"
        else:
            return "Item inválido"
