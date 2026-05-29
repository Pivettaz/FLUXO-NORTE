from Validacao.validadores import gerenciar_entrada_numerica, validar_id_entregador, validar_id_pedido, validar_nome
from utils import limpar_tela, confirmacao
from Menu.sub_menus import (sub_menu_estados, sub_menu_regiao, sub_menu_prioridade,
                            sub_menu_porte, sub_menu_status_pedido, sub_menu_status_pago,
                            sub_menu_atualizacao, sub_menu_pagamento, sub_menu_confirmar)
import random
from cores import BRANCO, VERDE, VERMELHO, AMARELO
from time import sleep

MAPA_ESTADOS = {1: "AC", 2: "AP", 3: "AM", 4: "PA", 5: "RO", 6: "RR", 7: "TO"}
MAPA_REGIOES = {1: "ZONA NORTE", 2: "ZONA SUL", 3: "ZONA LEST", 4: "ZONA OEST", 5: "CENTRO"}
MAPA_PRIORIDADES = {1: "ALTA", 2: "NORMAL"}
MAPA_PORTES = {1: "PEQUENO", 2: "MÉDIO", 3: "GRANDE"}
MAPA_STATUS_PEDIDO = {1: "PENDENTE", 2: "EM ROTA", 3: "ENTREGUE", 4: "CANCELADO", 5: "REEMBOLSADO"}
MAPA_STATUS_PAGO = {1: "PAGO", 2: "NAO PAGO", 3: "REEMBOLSADO"}
MAPA_VEICULOS = {1: "MOTO", 2: "CARRO", 3: "VAN"}

PONTOS_PORTE = {1: 1, 2: 2, 3: 3}
CAPACIDADE_PONTOS_VEICULO = {1: 3, 2: 9, 3: 15}


def gerar_id_pedido():
    letras_aleatorias = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))
    numeros_aleatorios = random.randint(1000, 9999)
    return letras_aleatorias + str(numeros_aleatorios)


def cadastrar_nome():
    limpar_tela()
    nome = input(BRANCO + "Insira o nome do cliente (X para cancelar): ")
    if nome.lower() == 'x':
        return None
    while not validar_nome(nome):
        limpar_tela()
        nome = input(BRANCO + "Insira o nome do cliente novamente (X para cancelar): ")
        if nome.lower() == 'x':
            return None
    limpar_tela()
    return nome.upper()


def cadastrar_estado():
    limpar_tela()
    sub_menu_estados()
    estado = gerenciar_entrada_numerica(1, 7, BRANCO + "Digite uma opção: ")
    while estado is False:
        limpar_tela()
        sub_menu_estados()
        estado = gerenciar_entrada_numerica(1, 7, BRANCO + "Digite uma opção novamente: ")
    return estado


def cadastrar_endereco():
    limpar_tela()
    endereco = input(BRANCO + "Digite [BAIRRO - RUA - NÚMERO] (X para cancelar): ").strip()

    if endereco.lower() == 'x':
        return None

    rodando_loop = 1
    while rodando_loop:
        partes_endereco = endereco.split("-")

        if len(partes_endereco) == 3 and partes_endereco[0].strip() and partes_endereco[1].strip() and partes_endereco[2].strip():
            break

        limpar_tela()
        print(AMARELO + "Use o padrão de traços. Exemplo: Centro - Rua Flores - 123\n")

        endereco = input(BRANCO + "\nDigite novamente (X para cancelar): ").strip()

        if endereco.lower() == 'x':
            return None

    return endereco.upper()


def cadastrar_regiao():
    limpar_tela()
    sub_menu_regiao()
    regiao_pedido = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
    while regiao_pedido is False:
        limpar_tela()
        sub_menu_regiao()
        regiao_pedido = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")
    return regiao_pedido


def cadastrar_prioridade():
    limpar_tela()
    sub_menu_prioridade()
    prioridade = gerenciar_entrada_numerica(1, 2, BRANCO + "\nDigite uma opção: ")
    while prioridade is False:
        limpar_tela()
        sub_menu_prioridade()
        prioridade = gerenciar_entrada_numerica(1, 2, BRANCO + "\nDigite uma opção novamente: ")
    return prioridade


def cadastrar_descricao():
    limpar_tela()
    descricao = input(BRANCO + "Insira a descrição do produto (X para cancelar): ").strip()

    if descricao.lower() == 'x':
        return None

    while len(descricao) < 10:
        limpar_tela()
        print(AMARELO + "Descrição insuficiente! Deve conter pelo menos 10 caracteres.")

        descricao = input(BRANCO + "\nInsira a descrição do produto (X para cancelar): ").strip()

        if descricao.lower() == 'x':
            return None
    return descricao


def cadastrar_porte():
    limpar_tela()
    sub_menu_porte()
    porte = gerenciar_entrada_numerica(1, 3, BRANCO + "\nDigite uma opção: ")
    while porte is False:
        limpar_tela()
        sub_menu_porte()
        porte = gerenciar_entrada_numerica(1, 3, BRANCO + "\nDigite uma opção novamente: ")
    return porte


def cadastrar_valor():
    limpar_tela()
    valor_texto = input(BRANCO + "Insira o valor do produto (X para cancelar): ")
    if valor_texto.lower() == 'x':
        return None
    valor_texto = valor_texto.replace(",", ".")
    while not valor_texto.replace(".", "", 1).strip().isdigit():
        limpar_tela()
        print(AMARELO + "Valor deve ser um número válido")
        sleep(1.5)
        limpar_tela()
        valor_texto = input(BRANCO + "Insira o valor do produto novamente (X para cancelar): ")
        if valor_texto.lower() == 'x':
            return None
        valor_texto = valor_texto.replace(",", ".")
    return float(valor_texto)


def cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao, porte_pedido):
    limpar_tela()
    id_entregador = input(BRANCO + "Insira o ID do entregador responsável (X para cancelar): ")
    if id_entregador.lower() == 'x':
        return None
    while not validar_id_entregador(id_entregador):
        limpar_tela()
        id_entregador = input(BRANCO + "Insira o ID do entregador responsável novamente (X para cancelar): ")
        if id_entregador.lower() == 'x':
            return None

    estado_sigla = MAPA_ESTADOS.get(estado, "ID_INVALIDO")

    if not lista_entregadores:
        print(
            AMARELO + "\nNenhum entregador cadastrado, pedido ficará como Pendente.\nApós cadastrar um entregador atualize esse pedido.")
        input(BRANCO + "\nPressione Enter para continuar...")
        return "0000"

    entregador_encontrado = None
    for entregador in lista_entregadores:
        if entregador["id_entregador"] == id_entregador:
            entregador_encontrado = entregador
            break
    if entregador_encontrado is None:
        print(VERMELHO + "Entregador não encontrado no sistema.")
        confirmacao()
        return False

    contagem = 0
    pontos_em_uso = 0
    for pedido in lista_pedidos:
        if pedido["id_entregador"] == id_entregador and pedido["status_pedido"] in [1, 2]:
            contagem += 1
            pontos_em_uso += PONTOS_PORTE[pedido["porte_pedido"]]

    if contagem >= 5:
        print(AMARELO + "\nUm entregador só pode assumir 5 entregas simultâneas")
        confirmacao()
        return False

    nome_veiculo = MAPA_VEICULOS.get(entregador_encontrado["veiculo"], "VEÍCULO")
    limite_pontos = CAPACIDADE_PONTOS_VEICULO[entregador_encontrado["veiculo"]]
    pontos_pedido_atual = PONTOS_PORTE[porte_pedido]

    if pontos_em_uso + pontos_pedido_atual > limite_pontos:
        print(AMARELO + f"\nCapacidade de carga excedida para {nome_veiculo}!")
        print(AMARELO + f"Limite: {limite_pontos} ponto(s) | Em uso: {pontos_em_uso} | Este pedido: +{pontos_pedido_atual} ({MAPA_PORTES[porte_pedido]})")
        confirmacao()
        return False

    if entregador_encontrado["estado"] != estado_sigla:
        print(AMARELO + "Este entregador não pertence a esse estado!")
        confirmacao()
        return False

    if entregador_encontrado["regiao"] != regiao:
        print(AMARELO + "Este entregador pertence ao estado, mas não a essa região!")
        confirmacao()
        return False

    print(VERDE + "Entregador verificado e confirmado para esta rota!")
    confirmacao()
    return id_entregador


def cadastrar_status(lista_entregadores):
    limpar_tela()
    if not lista_entregadores:
        return 1
    sub_menu_status_pedido()
    status = gerenciar_entrada_numerica(1, 4, BRANCO + "\nDigite uma opção: ")
    while status is False:
        limpar_tela()
        sub_menu_status_pedido()
        status = gerenciar_entrada_numerica(1, 4, BRANCO + "\nDigite uma opção novamente: ")
    return status


def cadastrar_status_pago():
    limpar_tela()
    sub_menu_status_pago()
    status_pago = gerenciar_entrada_numerica(1, 2, BRANCO + "\nDigite uma opção: ")
    while status_pago is False:
        limpar_tela()
        sub_menu_status_pago()
        status_pago = gerenciar_entrada_numerica(1, 2, BRANCO + "\nDigite uma opção novamente: ")
    return status_pago


def cadastrar_pedido(lista_pedidos, lista_entregadores):
    campos = ["id_pedido", "nome_cliente", "estado", "endereco", "regiao", "prioridade", "descricao_pedido",
              "porte_pedido", "valor_pedido", "status_pago", "id_entregador", "status_pedido"]
    pedido = dict.fromkeys(campos)

    pedido["id_pedido"] = gerar_id_pedido()

    pedido["nome_cliente"] = cadastrar_nome()
    if pedido["nome_cliente"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    estado = cadastrar_estado()
    if estado is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False
    pedido["estado"] = estado

    pedido["endereco"] = cadastrar_endereco()
    if pedido["endereco"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    regiao = cadastrar_regiao()
    if regiao is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False
    pedido["regiao"] = regiao

    pedido["prioridade"] = cadastrar_prioridade()
    if pedido["prioridade"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    pedido["descricao_pedido"] = cadastrar_descricao()
    if pedido["descricao_pedido"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    pedido["porte_pedido"] = cadastrar_porte()
    if pedido["porte_pedido"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    pedido["valor_pedido"] = cadastrar_valor()
    if pedido["valor_pedido"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    pedido["status_pago"] = cadastrar_status_pago()
    if pedido["status_pago"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    pedido["id_entregador"] = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao, pedido["porte_pedido"])
    if pedido["id_entregador"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    pedido["status_pedido"] = cadastrar_status(lista_entregadores)
    if pedido["status_pedido"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    lista_pedidos.append(pedido)

    porte_texto = MAPA_PORTES.get(pedido["porte_pedido"], "DESCONHECIDO")
    estado_texto = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
    prioridade_texto = MAPA_PRIORIDADES.get(pedido["prioridade"], "DESCONHECIDO")
    status_texto = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")
    status_pago_texto = MAPA_STATUS_PAGO.get(pedido["status_pago"], "DESCONHECIDO")

    print("\n" + BRANCO + "----- PEDIDO CADASTRADO -----")
    print(BRANCO + f"ID -> {pedido['id_pedido']}")
    print(BRANCO + f"CLIENTE -> {pedido['nome_cliente']}")
    print(BRANCO + f"ESTADO -> {estado_texto}")
    print(BRANCO + f"ENDEREÇO -> {pedido['endereco']}")
    print(BRANCO + f"REGIÃO -> {MAPA_REGIOES.get(pedido['regiao'], 'DESCONHECIDA')}")
    print(BRANCO + f"PRIORIDADE -> {prioridade_texto}")
    print(BRANCO + f"DESCRIÇÃO -> {pedido['descricao_pedido']}")
    print(BRANCO + f"PORTE -> {porte_texto}")
    print(BRANCO + f"VALOR -> R$ {pedido['valor_pedido']:.2f}")
    print(BRANCO + f"STATUS PAGAMENTO -> {status_pago_texto}")
    print(BRANCO + f"STATUS -> {status_texto}")
    print(BRANCO + f"ID ENTREGADOR -> {pedido['id_entregador']}")

    confirmacao()
    return True


def buscar_posicao_por_id(id_procurado, lista_pedidos):
    for i, pedido in enumerate(lista_pedidos):
        if pedido['id_pedido'] == id_procurado:
            return i
    return -1


def buscar_id_pedido_atualizar():
    id_pedido = input(BRANCO + "Digite o ID do pedido que deseja atualizar (X para cancelar): ").upper()
    if id_pedido == 'X':
        return None
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(BRANCO + "Digite o ID do pedido que deseja atualizar novamente (X para cancelar): ").upper()
        if id_pedido == 'X':
            return None
    return id_pedido


def atualizar_pedido(lista_pedidos, lista_entregadores):
    if not lista_pedidos:
        print(AMARELO + "Sem pedidos para atualizar...")
        confirmacao()
        return False

    id_pedido = buscar_id_pedido_atualizar()
    if id_pedido is None:
        print(AMARELO + "\nOperação cancelada.")
        confirmacao()
        return False

    posicao = buscar_posicao_por_id(id_pedido, lista_pedidos)

    if posicao == -1:
        limpar_tela()
        print(AMARELO + "Pedido não encontrado na base de dados.")
        confirmacao()
        return False

    limpar_tela()
    sub_menu_atualizacao()
    escolha = gerenciar_entrada_numerica(1, 4, BRANCO + "\nEscolha uma opção: ")

    match escolha:
        case None:
            limpar_tela()
            print(AMARELO + "\nOperação cancelada.")
            confirmacao()
            return False
        case 1:
            limpar_tela()
            if lista_pedidos[posicao]["status_pedido"] == 5:
                print(AMARELO + "Pedido reembolsado, sem alterações a fazer...")
                confirmacao()
                return False
            sub_menu_status_pedido()
            escolha_status = gerenciar_entrada_numerica(1, 4, BRANCO + "\nDigite uma opção: ")
            while escolha_status is False:
                limpar_tela()
                sub_menu_status_pedido()
                escolha_status = gerenciar_entrada_numerica(1, 4, BRANCO + "\nDigite uma opção novamente: ")
            if escolha_status is None:
                print(AMARELO + "\nOperação cancelada.")
                confirmacao()
                return False

            if lista_pedidos[posicao]["status_pedido"] == escolha_status:
                limpar_tela()
                print(
                    AMARELO + f"O pedido já está com o status '{MAPA_STATUS_PEDIDO[escolha_status]}'. Nenhuma alteração foi feita.")
                confirmacao()
                return False

            if escolha_status == 4:
                lista_pedidos[posicao]["id_entregador"] = "0000"

            limpar_tela()
            lista_pedidos[posicao]["status_pedido"] = escolha_status
            print(VERDE + f"Status do pedido atualizado com sucesso para: {MAPA_STATUS_PEDIDO[escolha_status]}")
            confirmacao()
            return True

        case 2:
            limpar_tela()
            if lista_pedidos[posicao]["status_pedido"] == 5:
                print(AMARELO + "Pedido reembolsado, entregadores não podem ser associados a ele...")
                confirmacao()
                return False
            estado = lista_pedidos[posicao]["estado"]
            regiao = lista_pedidos[posicao]["regiao"]

            if not lista_entregadores:
                limpar_tela()
                print(AMARELO + "Nenhum entregador cadastrado no sistema.")
                confirmacao()
                return False

            id_novo_entregador = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao, lista_pedidos[posicao]["porte_pedido"])

            if not id_novo_entregador:
                return False

            if lista_pedidos[posicao]["id_entregador"] == id_novo_entregador and lista_pedidos[posicao]["id_entregador"] != "0000":
                limpar_tela()
                print(AMARELO + "Este entregador já é o responsável por este pedido. Nenhuma alteração feita.")
                confirmacao()
                return False

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = id_novo_entregador
            print(VERDE + "Entregador atualizado com sucesso!")
            confirmacao()
            return True

        case 3:
            if lista_pedidos[posicao]["id_entregador"] == "0000":
                limpar_tela()
                print(AMARELO + "O pedido já está sem nenhum entregador associado.")
                confirmacao()
                return False

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = "0000"
            print(VERDE + "Entregador desassociado do pedido com sucesso.")
            confirmacao()
            return True

        case 4:
            limpar_tela()
            if lista_pedidos[posicao]["status_pedido"] == 5:
                print(AMARELO + "Pedido reembolsado, não há como atualizar o pagamento")
                confirmacao()
                return False
            sub_menu_pagamento()
            escolha_pagamento = gerenciar_entrada_numerica(1, 2, BRANCO + "\nDigite uma opção: ")
            while escolha_pagamento is False:
                limpar_tela()
                sub_menu_pagamento()
                escolha_pagamento = gerenciar_entrada_numerica(1, 2, BRANCO + "\nDigite uma opção novamente: ")
            if escolha_pagamento is None:
                print(AMARELO + "\nOperação cancelada.")
                confirmacao()
                return False

            if escolha_pagamento == 1:
                limpar_tela()
                if lista_pedidos[posicao]["status_pago"] == 1:
                    print(AMARELO + "Pedido já está pago")
                    confirmacao()
                    return False
                else:
                    lista_pedidos[posicao]["status_pago"] = 1
                    print(VERDE + "Pedido pago com sucesso!")
                    confirmacao()
                    return True
            else:
                limpar_tela()
                if lista_pedidos[posicao]["status_pago"] == 2:
                    print(AMARELO + "Pedido já está como NÃO PAGO")
                    confirmacao()
                    return False
                else:
                    lista_pedidos[posicao]["status_pago"] = 2
                    print(VERDE + "Pedido alterado para NÃO PAGO com sucesso!")
                    confirmacao()
                    return True
        case _:
            limpar_tela()
            print(VERMELHO + "Opção inválida detectada pelo sistema.")
            confirmacao()
            return False


def reativar_pedido(lista_pedidos, lista_entregadores):
    if not lista_pedidos:
        print(AMARELO + "Sem pedidos para reativar...")
        confirmacao()
        return False

    id_pedido = input(BRANCO + 'Digite o ID do pedido que deseja reativar (X para cancelar): ').upper()
    if id_pedido == 'X':
        print(AMARELO + "\nOperação cancelada.")
        confirmacao()
        return False
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(AMARELO + 'Digite o ID do pedido novamente (X para cancelar): ').upper()
        if id_pedido == 'X':
            print(AMARELO + "\nOperação cancelada.")
            confirmacao()
            return False

    posicao = buscar_posicao_por_id(id_pedido, lista_pedidos)

    if posicao == -1:
        limpar_tela()
        print(AMARELO + 'Pedido não encontrado na base de dados.')
        confirmacao()
        return False

    if lista_pedidos[posicao]['status_pedido'] != 4:
        limpar_tela()
        print(AMARELO + 'Este pedido não está cancelado e não pode ser reativado.')
        confirmacao()
        return False

    estado = lista_pedidos[posicao]['estado']
    regiao = lista_pedidos[posicao]['regiao']

    id_entregador = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao, lista_pedidos[posicao]['porte_pedido'])

    if not id_entregador:
        limpar_tela()
        print(AMARELO + 'Não foi possível reativar o pedido devido a problemas com o entregador.')
        confirmacao()
        return False

    valor_original = lista_pedidos[posicao]['valor_pedido']
    valor_reativado = float(f"{valor_original * 1.10:.2f}")

    limpar_tela()
    print(BRANCO + '--- CONFIRMAÇÃO DE REATIVAÇÃO ---')
    print(BRANCO + f"ID:             {lista_pedidos[posicao]['id_pedido']}")
    print(BRANCO + f"Cliente:        {lista_pedidos[posicao]['nome_cliente']}")
    print(BRANCO + f"Valor original: R$ {valor_original:.2f}")
    print(BRANCO + f"Valor com +10%: R$ {valor_reativado:.2f}")

    sub_menu_confirmar("DESEJA REATIVAR ESTE PEDIDO?")
    confirmar = gerenciar_entrada_numerica(1, 2, BRANCO + '\nDigite uma opção: ')

    if confirmar != 1:
        limpar_tela()
        print(AMARELO + 'Reativação cancelada.')
        confirmacao()
        return False

    lista_pedidos[posicao]['status_pedido'] = 1
    lista_pedidos[posicao]['valor_pedido'] = valor_reativado
    lista_pedidos[posicao]['id_entregador'] = id_entregador

    limpar_tela()
    print(VERDE + 'Pedido reativado com sucesso!')
    print(f'Novo status: PENDENTE | Novo valor: R$ {valor_reativado:.2f}')
    confirmacao()
    return True


def solicitar_reembolso(lista_pedidos):
    if not lista_pedidos:
        print(AMARELO + "Sem pedidos para reembolsar..")
        confirmacao()
        return False

    id_pedido = input(BRANCO + "Digite o ID do pedido a reembolsar (X para cancelar): ").upper()
    if id_pedido == 'X':
        print(AMARELO + "\nOperação cancelada.")
        confirmacao()
        return False
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(BRANCO + "Digite o ID do pedido a reembolsar novamente (X para cancelar): ").upper()
        if id_pedido == 'X':
            print(AMARELO + "\nOperação cancelada.")
            confirmacao()
            return False

    posicao = buscar_posicao_por_id(id_pedido, lista_pedidos)

    if posicao == -1:
        limpar_tela()
        print(AMARELO + "\nPedido não encontrado na base de dados.")
        confirmacao()
        return False

    status_atual = lista_pedidos[posicao]["status_pedido"]

    if status_atual == 5:
        limpar_tela()
        print(AMARELO + "\nEste pedido já foi reembolsado anteriormente!")
        confirmacao()
        return False

    if status_atual != 4 and status_atual != 1:
        limpar_tela()
        print(
            AMARELO + f"\nNão é possível reembolsar um pedido com o status '{MAPA_STATUS_PEDIDO.get(status_atual, 'DESCONHECIDO')}'.")
        print(BRANCO + "O pedido precisa estar pendente ou cancelado antes de solicitar o reembolso.")
        confirmacao()
        return False

    if lista_pedidos[posicao]["status_pago"] == 2:
        limpar_tela()
        print(AMARELO + "\nPedido não foi pago, reembolso cancelado.")
        confirmacao()
        return False

    justificativa = input(BRANCO + "Por que está solicitando o reembolso? ")

    sub_menu_confirmar("CONFIRMAR REEMBOLSO?")
    confirmacao_reembolso = gerenciar_entrada_numerica(1, 2, BRANCO + "\nDigite uma opção: ")

    if confirmacao_reembolso == 1:
        lista_pedidos[posicao]["status_pedido"] = 5
        lista_pedidos[posicao]["status_pago"] = 3
        lista_pedidos[posicao]["id_entregador"] = "0000"
        valor = lista_pedidos[posicao]["valor_pedido"]

        limpar_tela()
        print(VERDE + "Reembolso Confirmado com Sucesso!")
        print(BRANCO + f"Motivo do reembolso: {justificativa}")
        print(BRANCO + f"Valor a ser reembolsado: R$ {valor:.2f}")
        confirmacao()
        return True

    limpar_tela()
    print(AMARELO + "Operação de reembolso cancelada.")
    confirmacao()
    return False