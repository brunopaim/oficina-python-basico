from cliente import Cliente
from peca import Peca
from servico import Servico
from ordem_servico import OrdemServico
from item_os import ItemOS
from oficina import Oficina
from datetime import datetime

class Interface:
    def __init__(self):
        self.oficina = Oficina()

    def exibir_menu_principal(self):
        while True:
            print("\n---- Menu Principal ----")
            print("1. Cliente")
            print("2. Peça")
            print("3. Serviço")
            print("4. Ordem de Serviço")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.exibir_menu_cliente()
            elif opcao == "2":
                self.exibir_menu_peca()
            elif opcao == "3":
                self.exibir_menu_servico()
            elif opcao == "4":
                self.exibir_menu_ordem_servico()
            elif opcao == "5":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def exibir_menu_cliente(self):
        while True:
            print("\n---- Menu Cliente ----")
            print("1. Cadastrar novo cliente")
            print("2. Excluir cliente")
            print("3. Listar todos os clientes")
            print("4. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_novo_cliente()
            elif opcao == "2":
                self.excluir_cliente()
            elif opcao == "3":
                self.listar_todos_clientes()
            elif opcao == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def exibir_menu_peca(self):
        while True:
            print("\n---- Menu Peça ----")
            print("1. Cadastrar nova peça")
            print("2. Excluir peça")
            print("3. Listar todas as peças")
            print("4. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_nova_peca()
            elif opcao == "2":
                self.excluir_peca()
            elif opcao == "3":
                self.listar_todas_pecas()
            elif opcao == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def exibir_menu_servico(self):
        while True:
            print("\n---- Menu Serviço ----")
            print("1. Cadastrar novo serviço")
            print("2. Excluir serviço")
            print("3. Listar todos os serviços")
            print("4. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_novo_servico()
            elif opcao == "2":
                self.excluir_servico()
            elif opcao == "3":
                self.listar_todos_servicos()
            elif opcao == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def exibir_menu_ordem_servico(self):
        while True:
            print("\n---- Menu Ordem de Serviço ----")
            print("1. Cadastrar nova ordem de serviço")
            print("2. Inserir item (Peça) em ordem de serviço")
            print("3. Inserir item (Serviço) em ordem de serviço")
            print("4. Excluir item (Peça) de ordem de serviço")
            print("5. Excluir item (Serviço) de ordem de serviço")
            print("6. Finalizar ordem de serviço")
            print("7. Cancelar ordem de serviço")
            print("8. Listar todas as ordens de serviço e itens")
            print("9. Voltar ao menu principal")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.cadastrar_nova_ordem_servico()
            elif opcao == "2":
                self.inserir_item_peca_ordem_servico()
            elif opcao == "3":
                self.inserir_item_servico_ordem_servico()
            elif opcao == "4":
                self.excluir_item_peca_ordem_servico()
            elif opcao == "5":
                self.excluir_item_servico_ordem_servico()
            elif opcao == "6":
                self.finalizar_ordem_servico()
            elif opcao == "7":
                self.cancelar_ordem_servico()
            elif opcao == "8":
                self.listar_todas_ordens_servico_itens()
            elif opcao == "9":
                break
            else:
                print("Opção inválida. Tente novamente.")

    # Métodos correspondentes ao menu
    def cadastrar_novo_cliente(self):
        nome = input("Nome do cliente: ")
        cpf = input("CPF do cliente: ")
        endereco = input("Endereço do cliente: ")
        telefone = input("Telefone do cliente: ")
        cliente = Cliente(nome, cpf, endereco, telefone)
        if self.oficina.inserir_novo_cliente(cliente):
            print("Cliente cadastrado com sucesso.")
        else:
            print("Erro ao cadastrar cliente.")

    def cadastrar_nova_peca(self):
        print("\n------ Cadastrar Nova Peça ------")
        cdg = input("Código da peça: ")
        descricao = input("Descrição da peça: ")
        preco = float(input("Preço da peça: "))
        qtde_estoque = int(input("Quantidade em estoque: "))

        nova_peca = Peca(cdg, descricao, preco, qtde_estoque)
        self.oficina.inserir_nova_peca(nova_peca)
        print("Peça cadastrada com sucesso!")

    def cadastrar_novo_servico(self):
        cdg = input("Código do serviço: ")
        descricao = input("Descrição do serviço: ")
        preco = float(input("Preço do serviço: "))
        tempo_execucao = input("Tempo de execução do serviço (minutos): ")
        servico = Servico(cdg, descricao, preco, tempo_execucao)
        if self.oficina.inserir_novo_servico(servico):
            print("Serviço cadastrado com sucesso.")
        else:
            print("Erro ao cadastrar serviço.")

    def cadastrar_nova_ordem_servico(self):
        placa_carro = input("Placa do carro: ")
        cliente_cpf = input("CPF do cliente: ")
        data_prev_termino = input("Data previsão de término: ")
        cliente = self.oficina.encontrar_cliente_por_cpf(cliente_cpf)

        if cliente:
            ordem_servico = OrdemServico(placa_carro, cliente, data_prev_termino)
            if self.oficina.inserir_nova_ordem_servico(ordem_servico):
                print("Ordem de serviço cadastrada com sucesso.")
            else:
                print("Erro ao cadastrar ordem de serviço.")
        else:
            print("Cliente não encontrado. Cadastre o cliente primeiro.")

    def inserir_novo_item_peca_os(self):
        numero_os = int(input("Número da Ordem de Serviço: "))
        peca_codigo = int(input("Código da Peça: "))
        quantidade = int(input("Quantidade: "))

        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)
        peca = self.oficina.encontrar_peca_por_codigo(peca_codigo)

        if ordem_servico and peca:
            if ordem_servico.get_situacao() == "A":
                if self.oficina.inserir_novo_item_peca_os(ordem_servico, peca, quantidade):
                    print("Item (peça) inserido com sucesso na Ordem de Serviço.")
                else:
                    print("Erro ao inserir item (peça) na Ordem de Serviço.")
            else:
                print("Não é possível adicionar item em uma Ordem de Serviço não aberta.")
        else:
            print("Ordem de Serviço ou Peça não encontrada.")

    def inserir_novo_item_servico_os(self):
        numero_os = int(input("Número da Ordem de Serviço: "))
        servico_codigo = int(input("Código do Serviço: "))

        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)
        servico = self.oficina.encontrar_servico_por_codigo(servico_codigo)

        if ordem_servico and servico:
            if ordem_servico.get_situacao() == "A":
                if self.oficina.inserir_novo_item_servico_os(ordem_servico, servico):
                    print("Item (serviço) inserido com sucesso na Ordem de Serviço.")
                else:
                    print("Erro ao inserir item (serviço) na Ordem de Serviço.")
            else:
                print("Não é possível adicionar item em uma Ordem de Serviço não aberta.")
        else:
            print("Ordem de Serviço ou Serviço não encontrada.")

    def inserir_item_peca_ordem_servico(self):
        print("\n------ Inserir Item (Peça) em Ordem de Serviço ------")
        
        numero_os = int(input("Número da Ordem de Serviço: "))
        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)

        if ordem_servico is not None and ordem_servico.get_situacao() == "A":
            codigo_peca = int(input("Código da Peça: "))
            quantidade = int(input("Quantidade: "))

            peca = self.oficina.encontrar_peca_por_codigo(codigo_peca)

            if peca is not None and peca.get_qtde_estoque() >= quantidade:
                item_peca = ItemOS("P", quantidade, peca)
                self.oficina.inserir_novo_item_peca_os(ordem_servico, item_peca, quantidade)
                print("Item (Peça) inserido na Ordem de Serviço com sucesso!")
            else:
                print("Peça não encontrada ou quantidade insuficiente em estoque.")
        else:
            print("Ordem de Serviço não encontrada ou não está aberta.")

    def inserir_item_servico_ordem_servico(self):
        print("\n------ Inserir Item (Serviço) em Ordem de Serviço ------")
        
        numero_os = int(input("Número da Ordem de Serviço: "))
        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)

        if ordem_servico is not None and ordem_servico.get_situacao() == "A":
            codigo_servico = int(input("Código do Serviço: "))

            servico = self.oficina.encontrar_servico_por_codigo(codigo_servico)

            if servico is not None:
                item_servico = ItemOS("S", 1, None, servico)
                self.oficina.inserir_novo_item_servico_os(ordem_servico, item_servico)
                print("Item (Serviço) inserido na Ordem de Serviço com sucesso!")
            else:
                print("Serviço não encontrado.")
        else:
            print("Ordem de Serviço não encontrada ou não está aberta.")
    
    def excluir_cliente(self):
        cpf_cliente = input("Digite o CPF do cliente a ser excluído: ")
        cliente = self.oficina.encontrar_cliente_por_cpf(cpf_cliente)

        if cliente:
            if not self.oficina.excluir_cliente(cliente):
                print("Cliente não pode ser excluído devido a ordens de serviço associadas.")
            else:
                print("Cliente excluído com sucesso.")
        else:
            print("Cliente não encontrado.")

    def excluir_peca(self):
        codigo_peca = int(input("Digite o código da peça a ser excluída: "))
        peca = self.oficina.encontrar_peca_por_codigo(codigo_peca)

        if peca:
            if not self.oficina.excluir_peca(peca):
                print("Peça não pode ser excluída devido a ordens de serviço associadas.")
            else:
                print("Peça excluída com sucesso.")
        else:
            print("Peça não encontrada.")

    def excluir_servico(self):
        codigo_servico = int(input("Digite o código do serviço a ser excluído: "))
        servico = self.oficina.encontrar_servico_por_codigo(codigo_servico)

        if servico:
            if not self.oficina.excluir_servico(servico):
                print("Serviço não pode ser excluído devido a ordens de serviço associadas.")
            else:
                print("Serviço excluído com sucesso.")
        else:
            print("Serviço não encontrado.")

    def excluir_ordem_servico(self):
        numero_os = int(input("Digite o número da ordem de serviço a ser excluída: "))
        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)

        if ordem_servico:
            if ordem_servico.get_situacao() == "A":
                if not self.oficina.excluir_ordem_servico(ordem_servico):
                    print("Erro ao excluir ordem de serviço.")
                else:
                    print("Ordem de serviço excluída com sucesso.")
            else:
                print("Não é possível excluir uma ordem de serviço não aberta.")
        else:
            print("Ordem de serviço não encontrada.")

    def excluir_item_peca_os(self):
        numero_os = int(input("Número da Ordem de Serviço: "))
        codigo_peca = int(input("Código da Peça a ser excluída: "))

        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)
        peca = self.oficina.encontrar_peca_por_codigo(codigo_peca)

        if ordem_servico and peca:
            if ordem_servico.get_situacao() == "A":
                if not self.oficina.excluir_item_peca_os(ordem_servico, peca):
                    print("Erro ao excluir item (peça) da Ordem de Serviço.")
                else:
                    print("Item (peça) excluído com sucesso da Ordem de Serviço.")
            else:
                print("Não é possível excluir item de uma Ordem de Serviço não aberta.")
        else:
            print("Ordem de Serviço ou Peça não encontrada.")

    def excluir_item_servico_os(self):
        numero_os = int(input("Número da Ordem de Serviço: "))
        codigo_servico = int(input("Código do Serviço a ser excluído: "))

        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)
        servico = self.oficina.encontrar_servico_por_codigo(codigo_servico)

        if ordem_servico and servico:
            if ordem_servico.get_situacao() == "A":
                if not self.oficina.excluir_item_servico_os(ordem_servico, servico):
                    print("Erro ao excluir item (serviço) da Ordem de Serviço.")
                else:
                    print("Item (serviço) excluído com sucesso da Ordem de Serviço.")
            else:
                print("Não é possível excluir item de uma Ordem de Serviço não aberta.")
        else:
            print("Ordem de Serviço ou Serviço não encontrada.")

    def excluir_item_peca_ordem_servico(self):
        print("\n------ Excluir Item (Peça) de Ordem de Serviço ------")

        numero_os = int(input("Número da Ordem de Serviço: "))
        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)

        if ordem_servico is not None and ordem_servico.get_situacao() == "A":
            codigo_peca = int(input("Código da Peça a ser excluída: "))

            peca = self.oficina.encontrar_peca_por_codigo(codigo_peca)

            if peca is not None:
                self.oficina.excluir_item_peca_os(ordem_servico, peca)
                print("Item (Peça) excluído da Ordem de Serviço com sucesso!")
            else:
                print("Peça não encontrada na Ordem de Serviço.")
        else:
            print("Ordem de Serviço não encontrada ou não está aberta.")

    def excluir_item_servico_ordem_servico(self):
        print("\n------ Excluir Item (Serviço) de Ordem de Serviço ------")

        numero_os = int(input("Número da Ordem de Serviço: "))
        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)

        if ordem_servico is not None and ordem_servico.get_situacao() == "A":
            codigo_servico = int(input("Código do Serviço a ser excluído: "))

            servico = self.oficina.encontrar_servico_por_codigo(codigo_servico)

            if servico is not None:
                self.oficina.excluir_item_servico_os(ordem_servico, servico)
                print("Item (Serviço) excluído da Ordem de Serviço com sucesso!")
            else:
                print("Serviço não encontrado na Ordem de Serviço.")
        else:
            print("Ordem de Serviço não encontrada ou não está aberta.")
    
    def finalizar_ordem_servico(self):
        numero_os = int(input("Número da Ordem de Serviço a ser finalizada: "))
        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)

        if ordem_servico:
            if ordem_servico.get_situacao() == "A":
                ordem_servico.finalizar_ordem_servico()
                print("Ordem de Serviço finalizada com sucesso.")
            else:
                print("Apenas Ordens de Serviço abertas podem ser finalizadas.")
        else:
            print("Ordem de Serviço não encontrada.")

    def cancelar_ordem_servico(self):
        numero_os = int(input("Número da Ordem de Serviço a ser cancelada: "))
        ordem_servico = self.oficina.encontrar_ordem_servico_por_numero(numero_os)

        if ordem_servico:
            if ordem_servico.get_situacao() == "A":
                self.oficina.cancelar_ordem_servico(ordem_servico)
                print("Ordem de Serviço cancelada com sucesso.")
            else:
                print("Apenas Ordens de Serviço abertas podem ser canceladas.")
        else:
            print("Ordem de Serviço não encontrada.")

    def listar_todos_clientes(self):
        print("\n------ Lista de Clientes ------")
        for cliente in self.oficina.obter_lista_clientes():
            print(cliente)

    def listar_todas_pecas(self):
        print("\n------ Lista de Peças ------")
        for peca in self.oficina.obter_lista_pecas():
            print(peca)

    def listar_todos_servicos(self):
        print("\n------ Lista de Serviços ------")
        for servico in self.oficina.obter_lista_servicos():
            print(servico)

    def listar_todas_ordens_servico(self):
        print("\n------ Lista de Ordens de Serviço ------")
        for os in self.oficina.obter_lista_ordens_servico():
            print(os)
            print("Itens:")
            for item in os.obter_itens():
                print(item)

    def listar_todas_ordens_servico_itens(self):
        print("\n------ Lista de Todas as Ordens de Serviço com Itens ------")
        for ordem_servico in self.oficina.obter_lista_ordens_servico():
            print(ordem_servico)
            for item in ordem_servico.get_itens():
                print(f"  - {item}")

if __name__ == "__main__":
    interface = Interface()
    interface.exibir_menu_principal()
