class Servico:
    def __init__(self, codServico, descricao, preco, tempoExecucao):
        self.__codServico = codServico
        self.__descricao = descricao
        self.__preco = preco
        self.__tempoExecucao = tempoExecucao

    # Métodos de acesso (getters)
    def get_cod_servico(self):
        return self.__codServico

    def get_descricao(self):
        return self.__descricao

    def get_preco(self):
        return self.__preco

    def get_tempo_execucao(self):
        return self.__tempoExecucao

    # Métodos de modificação (setters)
    def set_cod_servico(self, codServico):
        self.__codServico = codServico

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_preco(self, preco):
        self.__preco = preco

    def set_tempo_execucao(self, tempoExecucao):
        self.__tempoExecucao = tempoExecucao

    def __str__(self):
        return f"Código: {self.__codServico}, Descrição: {self.__descricao}, Preço: {self.__preco}, Tempo de Execução: {self.__tempoExecucao} minutos"