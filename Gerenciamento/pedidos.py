from Validacao.validadores import gerenciar_entrada_numerica, validar_id_entregador, validar_id_pedido, validar_nome
from utils import limpar_tela, confirmacao
from Menu.sub_menus import sub_menu_estados, sub_menu_regiao
import random
from cores import BRANCO, VERDE, VERMELHO, AMARELO

MAPA_ESTADOS = {1: "AC", 2: "AP", 3: "AM", 4: "PA", 5: "RO", 6: "RR", 7: "TO"}
MAPA_REGIOES = {1: "ZONA NORTE", 2: "ZONA SUL", 3: "ZONA LEST", 4: "ZONA OEST", 5: "CENTRO"}
MAPA_PRIORIDADES = {1: "ALTA", 2: "NORMAL"}
MAPA_PORTES = {1: "PEQUENO", 2: "MÉDIO", 3: "GRANDE"}
MAPA_STATUS_PEDIDO = {1: "PENDENTE", 2: "EM ROTA", 3: "ENTREGUE", 4: "CANCELADO", 5: "REEMBOLSADO"}
MAPA_STATUS_PAGO = {1: "PAGO", 2: "NAO PAGO", 3: "REEMBOLSADO"}


def gerar_id_pedido():
    letras_aleatorias = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))
    numeros_aleatorios = random.randint(1000, 9999)
    return letras_aleatorias + str(numeros_aleatorios)


def cadastrar_nome():
    limpar_tela()
    nome = input(BRANCO + "Insira o nome do cliente: ")
    while not validar_nome(nome):
        limpar_tela()
        nome = input(AMARELO + "Insira o nome do cliente novamente: ")
    limpar_tela()
    return nome.upper()


def cadastrar_estado():
    limpar_tela()
    sub_menu_estados()
    estado = gerenciar_entrada_numerica(1, 7, BRANCO + "Digite uma opção: ")
    while not estado:
        estado = gerenciar_entrada_numerica(1, 7, BRANCO + "Digite uma opção novamente: ")
    return estado


def cadastrar_endereco():
    limpar_tela()
    endereco = input(BRANCO + "Digite o endereço do pedido: ")
    limpar_tela()
    return endereco.upper()


def cadastrar_regiao():
    limpar_tela()
    sub_menu_regiao()
    regiao_pedido = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
    while not regiao_pedido:
        limpar_tela()
        sub_menu_regiao()
        regiao_pedido = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")
    return regiao_pedido


def cadastrar_prioridade():
    limpar_tela()
    prioridade = gerenciar_entrada_numerica(1, 2, BRANCO + "\nPRIORIDADE \n[1] ALTA \n[2] NORMAL \nDigite uma opção: ")
    while not prioridade:
        limpar_tela()
        prioridade = gerenciar_entrada_numerica(1, 2,
                                                BRANCO + "\nPRIORIDADE \n[1] ALTA \n[2] NORMAL \nDigite uma opção novamente: ")
    return prioridade


def cadastrar_descricao():
    limpar_tela()
    return input(BRANCO + "Insira a descrição do product: ")


def cadastrar_porte():
    limpar_tela()
    porte = gerenciar_entrada_numerica(1, 3,
                                       BRANCO + "\nPORTE \n[1] BAIXO \n[2] MEDIO \n[3] GRANDE \nDigite uma opção: ")
    while not porte:
        limpar_tela()
        porte = gerenciar_entrada_numerica(1, 3,
                                           BRANCO + "\nPORTE \n[1] BAIXO \n[2] MEDIO \n[3] GRANDE \nDigite uma opção novamente: ")
    return porte


def cadastrar_valor():
    limpar_tela()
    valor_texto = input(BRANCO + "Insira o valor do produto: ")
    valor_texto = valor_texto.replace(",", ".")
    while not valor_texto.replace(".", "", 1).strip().isdigit():
        limpar_tela()
        print(AMARELO + "Valor deve ser um número válido")
        valor_texto = input(BRANCO + "Insira o valor do produto novamente: ")
        valor_texto = valor_texto.replace(",", ".")
    return float(valor_texto)


def cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao):
    limpar_tela()
    id_entregador = input(BRANCO + "Insira o ID do entregador responsável: ")
    while not validar_id_entregador(id_entregador):
        limpar_tela()
        id_entregador = input(BRANCO + "Insira o ID do entregador responsável novamente: ")

    estado_sigla = MAPA_ESTADOS.get(estado, "ID_INVALIDO")

    if not lista_entregadores:
        print(
            AMARELO + "\nNenhum entregador cadastrado, pedido ficará como Pendente.\nApós cadastrar um entregador atualize esse pedido.")
        input(BRANCO + "\nPressione Enter para continuar...")
        return "0000"

    contagem = 0
    for pedidos in lista_pedidos:
        if pedidos["id_entregador"] == id_entregador:
            if pedidos["status_pedido"] in [1, 2]:
                contagem += 1

    if contagem >= 5:
        print(AMARELO + "\nUm entregador só pode assumir 5 entregas simultâneas")
        confirmacao()
        return False

    for entregador in lista_entregadores:
        if entregador["id_entregador"] == id_entregador:
            if entregador["estado"] != estado_sigla:
                print(AMARELO + "Este entregador não pertence a esse estado!")
                confirmacao()
                return False

            if entregador["regiao"] != regiao:
                print(AMARELO + "Este entregador pertence ao estado, mas não a essa região!")
                confirmacao()
                return False

            print(VERDE + "Entregador verificado e confirmado para esta rota!")
            confirmacao()
            return id_entregador

    print(VERMELHO + "Entregador não encontrado no sistema.")
    confirmacao()
    return False


def cadastrar_status(lista_entregadores):
    limpar_tela()
    if not lista_entregadores:
        print(AMARELO + "Nenhum entregador cadastrado \nPedido ficara como PENDENTE...")
        return 1
    status = gerenciar_entrada_numerica(1, 4,
                                        BRANCO + "\nSTATUS DO PEDIDO \n[1] PENDENTE \n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO \nDigite uma opção: ")
    while not status:
        limpar_tela()
        status = gerenciar_entrada_numerica(1, 4,
                                            BRANCO + "\nSTATUS DO PEDIDO \n[1] PENDENTE \n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO \nDigite uma opção novamente: ")
    return status


def cadastrar_status_pago():
    status_pago = gerenciar_entrada_numerica(1, 2,
                                             BRANCO + "STATUS FINANCEIRO \n[1] SIM (PAGO) \n[2] NÃO (A PAGAR) \nDigite uma opção: ")
    while not status_pago:
        status_pago = gerenciar_entrada_numerica(1, 2,
                                                 BRANCO + "STATUS FINANCEIRO \n[1] SIM (PAGO) \n[2] NÃO (A PAGAR) \nDigite uma opção novamente: ")
    return status_pago


def cadastrar_pedido(lista_pedidos, lista_entregadores):
    campos = ["id_pedido", "nome_cliente", "estado", "endereco", "regiao", "prioridade", "descricao_pedido",
              "porte_pedido", "valor_pedido", "status_pago", "id_entregador", "status_pedido"]
    pedido = dict.fromkeys(campos)

    pedido["id_pedido"] = gerar_id_pedido()
    pedido["nome_cliente"] = cadastrar_nome()

    estado = cadastrar_estado()
    pedido["estado"] = estado

    pedido["endereco"] = cadastrar_endereco()

    regiao = cadastrar_regiao()
    pedido["regiao"] = regiao

    pedido["prioridade"] = cadastrar_prioridade()
    pedido["descricao_pedido"] = cadastrar_descricao()

    pedido["porte_pedido"] = cadastrar_porte()
    pedido["valor_pedido"] = cadastrar_valor()

    pedido["status_pago"] = cadastrar_status_pago()
    pedido["id_entregador"] = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao)
    pedido["status_pedido"] = cadastrar_status(lista_entregadores)

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
    id_pedido = input(BRANCO + "Digite o ID do pedido que deseja atualizar: ").upper()
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(BRANCO + "Digite o ID do pedido que deseja atualizar novamente: ").upper()
    return id_pedido


def atualizar_pedido(lista_pedidos, lista_entregadores):
    if not lista_pedidos:
        print(AMARELO + "Sem pedidos para atualizar...")
        confirmacao()
        return False

    id_pedido = buscar_id_pedido_atualizar()
    posicao = buscar_posicao_por_id(id_pedido, lista_pedidos)

    if posicao == -1:
        limpar_tela()
        print(AMARELO + "Pedido não encontrado na base de dados.")
        confirmacao()
        return False

    limpar_tela()
    escolha = gerenciar_entrada_numerica(
        1, 4,
        BRANCO + "\n--- MENU DE ATUALIZAÇÃO ---\n"
                 "[1] Alterar Status do Pedido \n"
                 "[2] Associar Entregador \n"
                 "[3] Desassociar Entregador\n"
                 "[4] Atualizar Pagamento\n"
                 "Escolha uma opção: "
    )

    match escolha:
        case 1:
            limpar_tela()
            escolha_status = gerenciar_entrada_numerica(1, 4,
                                                        BRANCO + "\nSTATUS DO PEDIDO \n[1] PENDENTE \n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO \nDigite uma opção: ")
            while not escolha_status:
                limpar_tela()
                escolha_status = gerenciar_entrada_numerica(1, 4,
                                                            BRANCO + "\nSTATUS DO PEDIDO \n[1] PENDENTE \n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO \nDigite uma opção novamente: ")

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
            estado = lista_pedidos[posicao]["estado"]
            regiao = lista_pedidos[posicao]["regiao"]

            id_novo_entregador = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao)

            if id_novo_entregador == False:
                return False

            if lista_pedidos[posicao]["id_entregador"] == id_novo_entregador:
                limpar_tela()
                print(AMARELO + "Este entregador já é o responsável por este pedido. Nenhuma alteração feita.")
                confirmacao()
                return False

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = id_novo_entregador
            print(VERDE + "Entregador updated com sucesso!")
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
            escolha_pagamento = gerenciar_entrada_numerica(1, 2,
                                                           BRANCO + "[1] SETAR PAGO \n[2] SETAR NÃO PAGO \nDigite uma opção: ")
            while not escolha_pagamento:
                escolha_pagamento = gerenciar_entrada_numerica(1, 2,
                                                               BRANCO + "[1] SETAR PAGO \n[2] SETAR NÃO PAGO \nDigite uma opção novamente: ")

            if escolha_pagamento == 1:
                limpar_tela()
                if lista_pedidos[posicao]["status_pago"] == 1:  # 1 = PAGO
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
                if lista_pedidos[posicao]["status_pago"] == 2:  # 2 = NAO PAGO
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
    id_pedido = input(BRANCO + 'Digite o ID do pedido que deseja reativar: ').upper()
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(AMARELO + 'Digite o ID do pedido novamente: ').upper()

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

    id_entregador = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao)

    if id_entregador == False:
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

    confirmar = gerenciar_entrada_numerica(1, 2,
                                           BRANCO + '\nDeseja reativar esse pedido? \n[1] SIM \n[2] NÃO \nDigite uma opção: ')

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
    id_pedido = input(BRANCO + "Digite o ID do pedido a reembolsar: ").upper()
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(BRANCO + "Digite o ID do pedido a reembolsar novamente: ").upper()

    posicao = buscar_posicao_por_id(id_pedido, lista_pedidos)

    if posicao == -1:
        limpar_tela()
        print(AMARELO + "Pedido não encontrado na base de dados.")
        confirmacao()
        return False

    status_atual = lista_pedidos[posicao]["status_pedido"]

    if status_atual == 5:  # 5 = REEMBOLSADO
        limpar_tela()
        print(AMARELO + "Este pedido já foi reembolsado anteriormente!")
        confirmacao()
        return False

    if status_atual != 4 and status_atual != 1:
        limpar_tela()
        print(
            AMARELO + f"Não é possível reembolsar um pedido com o status '{MAPA_STATUS_PEDIDO.get(status_atual, 'DESCONHECIDO')}'.")
        print("O pedido precisa estar pendente ou cancelado antes de solicitar o reembolso.")
        confirmacao()
        return False

    if lista_pedidos[posicao]["status_pago"] == 2:
        limpar_tela()
        print(AMARELO + "Pedido não foi pago, reembolso cancelado.")
        confirmacao()
        return False

    justificativa = input("Por que está solicitando o reembolso? ")

    confirmacao_reembolso = gerenciar_entrada_numerica(
        1, 2,
        BRANCO + "\nConfirmar reembolso? \n[1] Sim \n[2] Não \nDigite uma opção: "
    )

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