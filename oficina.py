from cliente import Cliente
from peca import Peca
from servico import Servico
from ordem_servico import OrdemServico
from item_os import ItemOS
import pickle
from datetime import datetime

class Oficina:
    def __init__(self):
        self.__clientes = []
        self.__pecas = []
        self.__servicos = []
        self.__oss = []

    # Métodos para inserir novos elementos nas listas
    def inserir_novo_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__clientes.append(cliente)
            return True
        return False

    def inserir_nova_peca(self, peca):
        if isinstance(peca, Peca):
            self.__pecas.append(peca)
            return True
        return False

    def inserir_novo_servico(self, servico):
        if isinstance(servico, Servico):
            self.__servicos.append(servico)
            return True
        return False

    def inserir_nova_ordem_servico(self, ordem_servico):
        if isinstance(ordem_servico, OrdemServico):
            self.__oss.append(ordem_servico)
            return True
        return False

    # Métodos para inserir novos itens em uma ordem de serviço
    def inserir_novo_item_peca_os(self, ordem_servico, peca, quantidade):
        if isinstance(ordem_servico, OrdemServico) and isinstance(peca, Peca):
            return ordem_servico.adicionar_item_peca(peca, quantidade)
        return False

    def inserir_novo_item_servico_os(self, ordem_servico, servico):
        if isinstance(ordem_servico, OrdemServico) and isinstance(servico, Servico):
            return ordem_servico.adicionar_item_servico(servico)
        return False

    # Métodos para excluir elementos das listas
    def excluir_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            if not any(os.get_cliente() == cliente for os in self.__oss):
                self.__clientes.remove(cliente)
                return True
            else:
                print("Erro: Não é possível excluir um cliente com OS associada.")
        return False

    def excluir_peca(self, peca):
        if isinstance(peca, Peca):
            if not any(item.get_tipo_item() == "P" and item.get_peca() == peca for os in self.__oss for item in os.get_itens()):
                self.__pecas.remove(peca)
                return True
            else:
                print("Erro: Não é possível excluir uma peça com OS associada.")
        return False

    def excluir_servico(self, servico):
        if isinstance(servico, Servico):
            if not any(item.get_tipo_item() == "S" and item.get_servico() == servico for os in self.__oss for item in os.get_itens()):
                self.__servicos.remove(servico)
                return True
            else:
                print("Erro: Não é possível excluir um serviço com OS associada.")
        return False

    def excluir_ordem_servico(self, ordem_servico):
        if isinstance(ordem_servico, OrdemServico) and ordem_servico.get_situacao() == "A":
            for item in ordem_servico.get_itens():
                if item.get_tipo_item() == "P":
                    item.get_peca().incrementar_estoque(item.get_quantidade())
            self.__oss.remove(ordem_servico)
            return True
        else:
            print("Erro: Não é possível excluir uma OS não aberta.")
        return False

    # Métodos para excluir itens de uma ordem de serviço
    def excluir_item_peca_os(self, ordem_servico, peca):
        if isinstance(ordem_servico, OrdemServico):
            return ordem_servico.excluir_item_peca(peca)
        return False

    def excluir_item_servico_os(self, ordem_servico, servico):
        if isinstance(ordem_servico, OrdemServico):
            # Considerando que um serviço não pode ser removido de uma OS
            print("Erro: Não é possível excluir um serviço de uma OS.")
            return False
        return False

    # Métodos para finalizar ou cancelar uma ordem de serviço
    def finalizar_ordem_servico(self, ordem_servico):
        if isinstance(ordem_servico, OrdemServico) and ordem_servico.get_situacao() == "A":
            ordem_servico.set_data_termino(datetime.now())
            ordem_servico.set_situacao("F")

            return True
        else:
            print("Erro: Não é possível finalizar uma OS não aberta.")
        return False

    def cancelar_ordem_servico(self, ordem_servico):
        if isinstance(ordem_servico, OrdemServico) and ordem_servico.get_situacao() == "A":
            for item in ordem_servico.get_itens():
                if item.get_tipo_item() == "P":
                    item.get_peca().incrementar_estoque(item.get_quantidade())
            ordem_servico.set_situacao("C")
            return True
        else:
            print("Erro: Não é possível cancelar uma OS não aberta.")
        return False

    # Métodos para obter listas
    def obter_lista_clientes(self):
        return self.__clientes

    def obter_lista_pecas(self):
        return self.__pecas

    def obter_lista_servicos(self):
        return self.__servicos

    def obter_lista_ordens_servico(self):
        return self.__oss

    # Métodos para gravar e ler dados em arquivo
    def gravar_dados_em_arquivo(self, nome_arquivo):
        dados = {
            'clientes': self.__clientes,
            'pecas': self.__pecas,
            'servicos': self.__servicos,
            'ordens_servico': self.__oss
        }

        with open(nome_arquivo, 'wb') as file:
            pickle.dump(dados, file)
        print("Dados gravados com sucesso!")

    def ler_dados_de_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'rb') as file:
                dados = pickle.load(file)

                self.__clientes = dados.get('clientes', [])
                self.__pecas = dados.get('pecas', [])
                self.__servicos = dados.get('servicos', [])
                self.__oss = dados.get('ordens_servico', [])

            print("Dados lidos com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado. Inicializando com listas vazias.")
        except Exception as e:
            print(f"Erro ao ler dados do arquivo: {e}")

    def encontrar_cliente_por_cpf(self, cpf):
        for cliente in self.__clientes:
            if cliente.get_cpf() == cpf:
                return cliente
        return None
    
    def encontrar_peca_por_codigo(self, codigo):
        for peca in self.__pecas:
            if int(peca.get_cod_peca()) == codigo:
                return peca
        return None
    
    def encontrar_servico_por_codigo(self, codigo):
        for servico in self.__servicos:
            if int(servico.get_cod_servico()) == codigo:
                return servico
        return None
    
    def encontrar_ordem_servico_por_numero(self, numero):
        for ordem_servico in self.__oss:
            if ordem_servico.get_numero_os() == numero:
                return ordem_servico
        return None