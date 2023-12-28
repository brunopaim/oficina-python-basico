from datetime import datetime
from item_os import ItemOS

class OrdemServico:
    proximoNumero = 1

    def __init__(self, placa_carro, cliente, data_prev_termino):
        self.__numeroOS = OrdemServico.proximoNumero
        OrdemServico.proximoNumero += 1
        self.__dataOS = datetime.now()
        self.__dataPrevTermino = data_prev_termino
        self.__dataTermino = None
        self.__placaCarro = placa_carro
        self.__situacao = "A"  # A-Aberta, C-Cancelada, F-Finalizada
        self.__cliente = cliente
        self.__itens = []

    # Métodos de acesso (getters)
    def get_numero_os(self):
        return self.__numeroOS

    def get_data_os(self):
        return self.__dataOS

    def get_data_prev_termino(self):
        return self.__dataPrevTermino

    def get_data_termino(self):
        return self.__dataTermino

    def get_placa_carro(self):
        return self.__placaCarro

    def get_situacao(self):
        return self.__situacao

    def get_cliente(self):
        return self.__cliente

    def get_itens(self):
        return self.__itens

    # Método para adicionar um item (peça) à ordem de serviço
    def adicionar_item_peca(self, peca, quantidade):
        if self.__situacao == "A":
            if quantidade > 0 and peca.get_qtde_estoque() >= quantidade:
                item = ItemOS(peca=peca, quantidade=quantidade)
                self.__itens.append(item)
                peca.decrementar_estoque(quantidade)
                return True
            else:
                print("Erro: Quantidade inválida ou insuficiente em estoque.")
        else:
            print("Erro: Não é possível adicionar itens a uma OS não aberta.")
        return False

    # Método para excluir um item (peça) da ordem de serviço
    def excluir_item_peca(self, peca):
        if self.__situacao == "A":
            for item in self.__itens:
                if item.get_tipo_item() == "P" and item.get_peca() == peca:
                    self.__itens.remove(item)
                    peca.incrementar_estoque(item.get_quantidade())
                    return True
            print("Erro: Peça não encontrada na OS.")
        else:
            print("Erro: Não é possível excluir itens de uma OS não aberta.")
        return False

    # Método para adicionar um item (serviço) à ordem de serviço
    def adicionar_item_servico(self, servico):
        if self.__situacao == "A":
            item = ItemOS(servico=servico)
            self.__itens.append(item)
            return True
        else:
            print("Erro: Não é possível adicionar itens a uma OS não aberta.")
        return False
    
     # Método para definir a data de término
    def set_data_termino(self, data_termino):
        self.__dataTermino = data_termino

    # Método para definir a situação
    def set_situacao(self, situacao):
        self.__situacao = situacao

    # Métodos para finalizar ou cancelar uma ordem de serviço
    def finalizar_ordem_servico(self):
        if self.__situacao == "A":
            self.set_situacao("F")
            return True
        else:
            print("Erro: Não é possível finalizar uma OS não aberta.")
        return False

    def cancelar_ordem_servico(self):
        if self.__situacao == "A":
            for item in self.__itens:
                if item.get_tipo_item() == "P":
                    item.get_peca().incrementar_estoque(item.get_quantidade())
            self.set_situacao("C")
            return True
        else:
            print("Erro: Não é possível cancelar uma OS não aberta.")
        return False
    
    def __str__(self):
        return f"Número OS: {self.__numeroOS}, Data OS: {self.__dataOS}, Data Prevista Término: {self.__dataPrevTermino}, Placa Carro: {self.__placaCarro}, Situação: {self.__situacao}"
