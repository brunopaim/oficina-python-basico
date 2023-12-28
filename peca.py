class Peca:
    def __init__(self, codPeca, descricao, preco, qtde_estoque):
        self.__codPeca = codPeca
        self.__descricao = descricao
        self.__preco = preco
        self.__qtdeEstoque = qtde_estoque

    # Métodos de acesso (getters)
    def get_cod_peca(self):
        return self.__codPeca

    def get_descricao(self):
        return self.__descricao

    def get_preco(self):
        return self.__preco

    def get_qtde_estoque(self):
        return self.__qtdeEstoque

    # Métodos de modificação (setters)
    def set_cod_peca(self, codPeca):
        self.__codPeca = codPeca

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_preco(self, preco):
        self.__preco = preco

    def set_qtde_estoque(self, qtde_estoque):
        self.__qtdeEstoque = qtde_estoque

    # Método para incrementar a quantidade em estoque
    def incrementar_estoque(self, quantidade):
        self.__qtdeEstoque += quantidade

    # Método para decrementar a quantidade em estoque
    def decrementar_estoque(self, quantidade):
        if self.__qtdeEstoque >= quantidade:
            self.__qtdeEstoque -= quantidade
        else:
            print("Erro: Quantidade em estoque insuficiente.")

    def __str__(self):
        return f"Código: {self.__codPeca}, Descrição: {self.__descricao}, Preço: {self.__preco},  Estoque: {self.__qtdeEstoque}"