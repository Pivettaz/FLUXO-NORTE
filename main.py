import os
import random
from time import sleep

import pyfiglet
from colorama import init

BRANCO   = "\033[38;2;245;245;245m"
AMARELO  = "\033[38;2;255;217;61m"
VERDE    = "\033[38;2;74;222;128m"
VERMELHO = "\033[38;2;255;85;85m"
CIANO    = "\033[38;2;34;211;238m"

PALETA = [
    "\033[38;2;34;211;238m",
    "\033[38;2;74;222;128m",
    "\033[38;2;251;191;36m",
    "\033[38;2;251;146;60m",
    "\033[38;2;167;139;250m",
    "\033[38;2;244;114;182m",
    "\033[38;2;96;165;250m",
    "\033[38;2;52;211;153m",
]

MAPA_ESTADOS = {1: "AC", 2: "AP", 3: "AM", 4: "PA", 5: "RO", 6: "RR", 7: "TO"}
MAPA_REGIOES = {1: "ZONA NORTE", 2: "ZONA SUL", 3: "ZONA LEST", 4: "ZONA OEST", 5: "CENTRO"}
MAPA_PRIORIDADES = {1: "ALTA", 2: "NORMAL"}
MAPA_PORTES = {1: "PEQUENO", 2: "MÉDIO", 3: "GRANDE"}
MAPA_STATUS_PEDIDO = {1: "PENDENTE", 2: "EM ROTA", 3: "ENTREGUE", 4: "CANCELADO", 5: "REEMBOLSADO"}
MAPA_STATUS_PAGO = {1: "PAGO", 2: "NAO PAGO", 3: "REEMBOLSADO"}
MAPA_VEICULOS = {1: "MOTO", 2: "CARRO", 3: "VAN"}
MAPA_TURNOS = {1: "MANHÃ", 2: "TARDE", 3: "NOITE"}

PONTOS_PORTE = {1: 1, 2: 2, 3: 3}
CAPACIDADE_PONTOS_VEICULO = {1: 3, 2: 9, 3: 15}

LARGURA = 44
NAVEGACAO = ("VOLTAR", "FINALIZAR SISTEMA")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def confirmacao():
    input(BRANCO + "\nPressione Enter para voltar ao menu...")

def gerenciar_entrada_numerica(min_val, max_val, mensagem):
    escolha = input(mensagem)

    if escolha.lower() == 'x':
        return None
    if not escolha.isdigit():
        print(AMARELO + f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        sleep(1.5)
        return False
    elif min_val <= int(escolha) <= max_val:
        return int(escolha)
    else:
        print(AMARELO + f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        sleep(1.5)
        return False

def validar_nome(nome):
    partes = nome.split()

    if len(partes) < 2:
        print(AMARELO + "Informe nome e sobrenome.")
        sleep(1.5)
        return False

    for parte in partes:
        if len(parte) < 2 or not parte.isalpha():
            print(AMARELO + "Nome e sobrenome devem conter pelo menos 2 letras cada e não conter símbolos ou números.")
            sleep(1.5)
            return False

    return True

def validar_id_entregador(id_entregador):
    if not id_entregador.isdigit():
        print(AMARELO + "\nID do entregador não deve conter letras")
        sleep(1.5)
        return False
    elif len(id_entregador) != 4:
        print(AMARELO + "\nID do entregador deve conter apenas 4 dígitos")
        sleep(1.5)
        return False
    return True

def validar_id_pedido(id_pedido):
    if len(id_pedido) != 5:
        print(AMARELO + "ID deve conter 5 dígitos")
        sleep(1.5)
        return False
    elif not id_pedido[0].isalpha():
        print(AMARELO + "Primeiro dígito do ID deve ser uma letra")
        sleep(1.5)
        return False
    elif not id_pedido[1:].isdigit():
        print(AMARELO + "\nQuatro últimos dígitos do ID devem ser um número")
        sleep(1.5)
        return False
    return id_pedido.upper()

def desenhar_menu(titulo, opcoes, cancelar=False):
    print(BRANCO + "╔" + "═" * LARGURA + "╗")
    print(BRANCO + "║" + AMARELO + titulo.center(LARGURA) + BRANCO + "║")
    print(BRANCO + "╠" + "═" * LARGURA + "╣")
    numero = 1
    for opcao in opcoes:
        icone = opcao[0]
        texto = opcao[1]
        if texto in NAVEGACAO:
            cor_texto = VERMELHO
        else:
            cor_texto = PALETA[(numero - 1) % len(PALETA)]
        print(f"  {CIANO}[{numero}]{cor_texto} {icone} {texto}")
        numero = numero + 1
    if cancelar:
        print(f"  {VERMELHO}[X] ❌ CANCELAR")
    print(BRANCO + "╚" + "═" * LARGURA + "╝")

def sub_menu_principal():
    banner = pyfiglet.figlet_format("FLUXO NORTE", font="standard")
    print(AMARELO + banner)
    desenhar_menu("SISTEMA DE LOGÍSTICA", [
        ["📦", "PEDIDOS"],
        ["🛵", "ENTREGADORES"],
        ["🔎", "CONSULTAS"],
        ["📊", "RELATÓRIOS"],
        ["🚪", "FINALIZAR SISTEMA"],
    ])

def sub_menu_pedidos():
    desenhar_menu("GERENCIAMENTO DE PEDIDOS", [
        ["📝", "CADASTRO"],
        ["🔄", "ATUALIZAÇÕES"],
        ["🔁", "REATIVAR PEDIDO"],
        ["💸", "REEMBOLSAR PEDIDO"],
        ["🔙", "VOLTAR"],
    ])

def sub_menu_entregadores():
    desenhar_menu("GERENCIAMENTO DE ENTREGADORES", [
        ["➕", "CADASTRO"],
        ["🔙", "VOLTAR"],
    ])

def sub_menu_consultas():
    desenhar_menu("PAINEL DE CONSULTAS", [
        ["⏳", "PEDIDOS PENDENTES (POR PRIORIDADE)"],
        ["🛵", "PEDIDOS EM ROTA (POR PRIORIDADE)"],
        ["✅", "PEDIDOS ENTREGUES"],
        ["🚫", "PEDIDOS CANCELADOS"],
        ["💸", "PEDIDOS REEMBOLSADOS"],
        ["🔍", "BUSCAR PEDIDO POR ID"],
        ["🟢", "ENTREGADORES DISPONÍVEIS"],
        ["📋", "HISTÓRICO DE ENTREGAS POR ENTREGADOR"],
        ["🔙", "VOLTAR"],
    ])

def sub_menu_relatorios():
    desenhar_menu("RELATÓRIOS GERENCIAIS", [
        ["🧾", "TOTAL DE PEDIDOS CADASTRADOS"],
        ["📊", "QUANTIDADE DE PEDIDOS POR STATUS"],
        ["🌟", "PEDIDOS DE ALTA PRIORIDADE"],
        ["🏆", "ENTREGADOR LÍDER DE ENTREGAS"],
        ["🔙", "VOLTAR"],
    ])

def sub_menu_alta_prioridade():
    desenhar_menu("RELATÓRIOS GERENCIAIS", [
        ["🌟", "GERAL"],
        ["⏳", "PENDENTE"],
        ["🛵", "EM ROTA"],
        ["🔙", "VOLTAR"],
    ])

def sub_menu_estados():
    desenhar_menu("SELECIONE O ESTADO", [
        ["📍", "Acre (AC)"],
        ["📍", "Amapá (AP)"],
        ["📍", "Amazonas (AM)"],
        ["📍", "Pará (PA)"],
        ["📍", "Rondônia (RO)"],
        ["📍", "Roraima (RR)"],
        ["📍", "Tocantins (TO)"],
    ], cancelar=True)

def sub_menu_veiculo():
    desenhar_menu("SELECIONE O VEÍCULO", [
        ["🛵", "MOTO"],
        ["🚗", "CARRO"],
        ["🚐", "VAN"],
    ], cancelar=True)

def sub_menu_regiao():
    desenhar_menu("SELECIONE A REGIÃO", [
        ["🧭", "ZONA NORTE"],
        ["🧭", "ZONA SUL"],
        ["🧭", "ZONA LESTE"],
        ["🧭", "ZONA OESTE"],
        ["🧭", "CENTRO"],
    ], cancelar=True)

def sub_menus_turno():
    desenhar_menu("SELECIONE O TURNO", [
        ["🌅", "MATUTINO   -> (07h às 16h)"],
        ["🌇", "VESPERTINO -> (14h às 23h)"],
        ["🌙", "NOTURNO    -> (23h às 07h)"],
    ], cancelar=True)

def sub_menu_prioridade():
    desenhar_menu("PRIORIDADE", [
        ["🔴", "ALTA"],
        ["🟢", "NORMAL"],
    ], cancelar=True)

def sub_menu_porte():
    desenhar_menu("PORTE DO PEDIDO", [
        ["🟦", "BAIXO"],
        ["🟨", "MEDIO"],
        ["🟥", "GRANDE"],
    ], cancelar=True)

def sub_menu_status_pedido():
    desenhar_menu("STATUS DO PEDIDO", [
        ["⏳", "PENDENTE"],
        ["🛵", "EM ROTA"],
        ["✅", "ENTREGUE"],
        ["🚫", "CANCELADO"],
    ], cancelar=True)

def sub_menu_status_pago():
    desenhar_menu("STATUS FINANCEIRO", [
        ["✅", "SIM (PAGO)"],
        ["💵", "NÃO (A PAGAR)"],
    ], cancelar=True)

def sub_menu_atualizacao():
    desenhar_menu("MENU DE ATUALIZAÇÃO", [
        ["🔄", "ALTERAR STATUS DO PEDIDO"],
        ["🔗", "ASSOCIAR ENTREGADOR"],
        ["➖", "DESASSOCIAR ENTREGADOR"],
        ["💰", "ATUALIZAR PAGAMENTO"],
    ], cancelar=True)

def sub_menu_pagamento():
    desenhar_menu("ATUALIZAR PAGAMENTO", [
        ["✅", "SETAR COMO PAGO"],
        ["💵", "SETAR COMO NÃO PAGO"],
    ], cancelar=True)

def sub_menu_confirmar(pergunta):
    desenhar_menu(pergunta, [
        ["✅", "SIM"],
        ["❌", "NÃO"],
    ])

def gerar_id_pedido(lista_pedidos):
    letras_aleatorias = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))
    numeros_aleatorios = random.randint(1000, 9999)
    id_pedido = letras_aleatorias + str(numeros_aleatorios)

    while buscar_posicao_por_id(id_pedido, lista_pedidos) != -1:
        letras_aleatorias = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1))
        numeros_aleatorios = random.randint(1000, 9999)
        id_pedido = letras_aleatorias + str(numeros_aleatorios)

    return id_pedido

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

    executando_endereco = 1
    while executando_endereco:
        partes_endereco = endereco.split("-")

        if len(partes_endereco) == 3 and partes_endereco[0].strip() and partes_endereco[1].strip() and partes_endereco[2].strip():
            break

        limpar_tela()
        print(AMARELO + "Use o padrão de traços. Exemplo: Centro - Rua Flores - 123\n")
        endereco = input(BRANCO + "Digite novamente (X para cancelar): ").strip()

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
    return descricao.upper()

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
    valor_valido = False
    while not valor_valido:
        valor_texto = input(BRANCO + "Insira o valor do produto (X para cancelar): ")
        if valor_texto.lower() == 'x':
            return None
        valor = float(valor_texto)
        if valor < 0:
            print(AMARELO + "Valor não pode ser negativo")
        elif valor > 1000000:
            print(AMARELO + "Valor não pode ser maior que 1.000.000")
        else:
            valor_valido = True
    return valor


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
        print(AMARELO + "\nNenhum entregador cadastrado, pedido ficará como Pendente.\nApós cadastrar um entregador atualize esse pedido.")
        input(BRANCO + "\nPressione Enter para continuar...")
        return "0000"

    entregador_encontrado = None
    for entregador in lista_entregadores:
        if entregador["id_entregador"] == id_entregador:
            entregador_encontrado = entregador
            break

    if entregador_encontrado is None:
        print(VERMELHO + "Entregador não encontrado no sistema.")
        print(AMARELO + "Pedido ficará como Pendente e sem nenhum entregador associado")
        confirmacao()
        return "0000"

    contagem = 0
    pontos_em_uso = 0
    for pedido in lista_pedidos:
        if pedido["id_entregador"] == id_entregador and pedido["status_pedido"] in [1, 2]:
            contagem += 1
            pontos_em_uso += PONTOS_PORTE[pedido["porte_pedido"]]

    if contagem >= 5:
        print(AMARELO + "\nUm entregador só pode assume 5 entregas simultâneas")
        print(AMARELO + "Pedido ficará como Pendente e sem nenhum entregador associado")
        confirmacao()
        return "0000"

    nome_veiculo = MAPA_VEICULOS.get(entregador_encontrado["veiculo"], "VEÍCULO")
    limite_pontos = CAPACIDADE_PONTOS_VEICULO[entregador_encontrado["veiculo"]]
    pontos_pedido_atual = PONTOS_PORTE[porte_pedido]

    if pontos_em_uso + pontos_pedido_atual > limite_pontos:
        print(AMARELO + f"\nCapacidade de carga excedida para {nome_veiculo}!")
        print(AMARELO + f"Limite: {limite_pontos} ponto(s) | Em uso: {pontos_em_uso} | Este pedido: +{pontos_pedido_atual} ({MAPA_PORTES[porte_pedido]})")
        print(AMARELO + "Pedido ficará como Pendente e sem nenhum entregador associado")
        confirmacao()
        return "0000"

    if entregador_encontrado["estado"] != estado_sigla:
        print(AMARELO + "Este entregador não pertence a esse estado!")
        print(AMARELO + "Pedido ficará como Pendente e sem nenhum entregador associado")
        confirmacao()
        return "0000"

    if entregador_encontrado["regiao"] != regiao:
        print(AMARELO + "Este entregador pertence ao estado, mas não a essa região!")
        print(AMARELO + "Pedido ficará como Pendente e sem nenhum entregador associado")
        confirmacao()
        return "0000"

    posicao_entregador = buscar_posicao_por_id(id_entregador, lista_entregadores, "id_entregador")

    total_pedidos_futuro = contagem + 1
    total_pontos_futuro = pontos_em_uso + pontos_pedido_atual

    if total_pontos_futuro >= limite_pontos or total_pedidos_futuro == 5:
        lista_entregadores[posicao_entregador]["disponibilidade"] = "INDISPONIVEL"
    else:
        lista_entregadores[posicao_entregador]["disponibilidade"] = "DISPONIVEL"

    print(VERDE + "Entregador verificado e confirmado para esta rota!")
    confirmacao()
    return id_entregador

def atualizar_disponibilidade_entregador(id_entregador, lista_pedidos, lista_entregadores):
    if id_entregador == "0000":
        return

    posicao_entregador = buscar_posicao_por_id(id_entregador, lista_entregadores, "id_entregador")
    if posicao_entregador == -1:
        return

    id_veiculo = lista_entregadores[posicao_entregador]["veiculo"]
    limite_pontos = CAPACIDADE_PONTOS_VEICULO[id_veiculo]

    contagem = 0
    pontos_em_uso = 0
    for pedido in lista_pedidos:
        if pedido["id_entregador"] == id_entregador and pedido["status_pedido"] in [1, 2]:
            contagem += 1
            pontos_em_uso += PONTOS_PORTE[pedido["porte_pedido"]]

    if pontos_em_uso >= limite_pontos or contagem >= 5:
        lista_entregadores[posicao_entregador]["disponibilidade"] = "INDISPONIVEL"
    else:
        lista_entregadores[posicao_entregador]["disponibilidade"] = "DISPONIVEL"

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
              "porte_pedido", "valor_pedido", "status_pago", "saldo_devedor", "id_entregador", "status_pedido"]
    pedido = dict.fromkeys(campos)

    pedido["id_pedido"] = gerar_id_pedido(lista_pedidos)

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

    if pedido["status_pago"] == 1:
        pedido["saldo_devedor"] = 0.0
    else:
        pedido["saldo_devedor"] = pedido["valor_pedido"]

    id_entregador_resultado = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao,
                                                             pedido["porte_pedido"])

    if id_entregador_resultado is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    pedido["id_entregador"] = id_entregador_resultado

    if pedido["id_entregador"] == "0000":
        pedido["status_pedido"] = 1
    else:
        status_pedido = cadastrar_status(lista_entregadores)
        if status_pedido is None:
            print(AMARELO + "\nCadastro cancelado.")
            confirmacao()
            return False

        pedido["status_pedido"] = status_pedido

    lista_pedidos.append(pedido)

    porte_texto = MAPA_PORTES.get(pedido["porte_pedido"], "DESCONHECIDO")
    estado_texto = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
    prioridade_texto = MAPA_PRIORIDADES.get(pedido["prioridade"], "DESCONHECIDO")
    status_texto = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")
    status_pago_texto = MAPA_STATUS_PAGO.get(pedido["status_pago"], "DESCONHECIDO")

    limpar_tela()
    print("\n" + BRANCO + "----- PEDIDO CADASTRADO -----")
    print(BRANCO + f"ID -> {pedido['id_pedido']}")
    print(BRANCO + f"CLIENTE -> {pedido['nome_cliente']}")
    print(BRANCO + f"ESTADO -> {estado_texto}")
    print(BRANCO + f"ENDEREÇO -> {pedido['endereco']}")
    print(BRANCO + f"REGIÃO -> {MAPA_REGIOES.get(pedido['regiao'], 'DESCONHECIDA')}")
    print(BRANCO + f"PRIORIDADE -> {prioridade_texto}")
    print(BRANCO + f"DESCRIÇÃO -> {pedido['descricao_pedido']}")
    print(BRANCO + f"PORTE -> {porte_texto}")
    print(BRANCO + f"VALOR TOTAL -> R$ {pedido['valor_pedido']:.2f}")
    print(BRANCO + f"SALDO DEVEDOR -> R$ {pedido['saldo_devedor']:.2f}")
    print(BRANCO + f"STATUS PAGAMENTO -> {status_pago_texto}")
    print(BRANCO + f"STATUS -> {status_texto}")
    print(BRANCO + f"ID ENTREGADOR -> {pedido['id_entregador']}")

    confirmacao()
    return True

def buscar_posicao_por_id(id_procurado, lista, chave="id_pedido"):
    for i, item in enumerate(lista):
        if item[chave] == id_procurado:
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
    escolha = gerenciar_entrada_numerica(1, 4, BRANCO + "\nEscolha uma opção (X para cancelar): ")

    match escolha:
        case 1:
            limpar_tela()
            if lista_pedidos[posicao]["status_pedido"] == 4:
                print(AMARELO + "Pedido cancelado, necessário reativá-lo...")
                confirmacao()
                return False
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

            entregador_afetado = lista_pedidos[posicao]["id_entregador"]

            limpar_tela()
            lista_pedidos[posicao]["status_pedido"] = escolha_status

            if escolha_status in [3, 4]:
                lista_pedidos[posicao]["id_entregador"] = "0000"
                atualizar_disponibilidade_entregador(entregador_afetado, lista_pedidos, lista_entregadores)

            print(VERDE + f"Status do pedido atualizado com sucesso para: {MAPA_STATUS_PEDIDO[escolha_status]}")
            confirmacao()
            return True

        case 2:
            limpar_tela()
            status_pedido_texto = MAPA_STATUS_PEDIDO.get(lista_pedidos[posicao]["status_pedido"], "DESCONHECIDO")
            if lista_pedidos[posicao]["status_pedido"] in [4, 5]:
                print(
                    AMARELO + f"Pedido com status {status_pedido_texto}, entregadores não podem ser associados a ele...")
                confirmacao()
                return False
            estado = lista_pedidos[posicao]["estado"]
            regiao = lista_pedidos[posicao]["regiao"]

            if not lista_entregadores:
                limpar_tela()
                print(AMARELO + "Nenhum entregador cadastrado no sistema.")
                confirmacao()
                return False

            id_novo_entregador = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao,
                                                                lista_pedidos[posicao]["porte_pedido"])

            if not id_novo_entregador:
                return False

            if lista_pedidos[posicao]["id_entregador"] == id_novo_entregador and lista_pedidos[posicao][
                "id_entregador"] != "0000":
                limpar_tela()
                print(AMARELO + "Este entregador já é o responsável por este pedido. Nenhuma alteração feita.")
                confirmacao()
                return False

            entregador_antigo = lista_pedidos[posicao]["id_entregador"]

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = id_novo_entregador

            atualizar_disponibilidade_entregador(entregador_antigo, lista_pedidos, lista_entregadores)
            atualizar_disponibilidade_entregador(id_novo_entregador, lista_pedidos, lista_entregadores)

            print(VERDE + "Entregador atualizado com sucesso!")
            confirmacao()
            return True

        case 3:
            if lista_pedidos[posicao]["id_entregador"] == "0000":
                limpar_tela()
                print(AMARELO + "O pedido já está sem nenhum entregador associado.")
                confirmacao()
                return False

            entregador_removido = lista_pedidos[posicao]["id_entregador"]

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = "0000"

            atualizar_disponibilidade_entregador(entregador_removido, lista_pedidos, lista_entregadores)

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
                    lista_pedidos[posicao]["saldo_devedor"] = 0.0
                    print(VERDE + "Pedido pago com sucesso! Saldo devedor zerado.")
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
                    lista_pedidos[posicao]["saldo_devedor"] = lista_pedidos[posicao]["valor_pedido"]
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

    id_entregador = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao,
                                                   lista_pedidos[posicao]['porte_pedido'])

    if not id_entregador:
        limpar_tela()
        print(AMARELO + 'Não foi possível reativar o pedido devido a problemas com o entregador.')
        confirmacao()
        return False

    valor_original = lista_pedidos[posicao]['valor_pedido']
    valor_reativado = float(f"{valor_original * 1.10:.2f}")
    valor_diferenca = float(f"{valor_reativado - valor_original:.2f}")

    limpar_tela()
    print(BRANCO + '--- CONFIRMAÇÃO DE REATIVAÇÃO ---')
    print(BRANCO + f"ID:             {lista_pedidos[posicao]['id_pedido']}")
    print(BRANCO + f"Cliente:        {lista_pedidos[posicao]['nome_cliente']}")
    print(BRANCO + f"Valor original: R$ {valor_original:.2f}")
    print(BRANCO + f"Valor com +10%: R$ {valor_reativado:.2f}")

    ja_estava_pago = lista_pedidos[posicao]['status_pago'] == 1

    if ja_estava_pago:
        print(AMARELO + f"Diferença da taxa a cobrar: R$ {valor_diferenca:.2f}")

    print("\n")
    sub_menu_confirmar("DESEJA REATIVAR ESTE PEDIDO?")
    confirmar = gerenciar_entrada_numerica(1, 2, BRANCO + '\nDigite uma opção: ')
    while confirmar is False:
        sub_menu_confirmar("DESEJA REATIVAR ESTE PEDIDO?")
        confirmar = gerenciar_entrada_numerica(1, 2, BRANCO + '\nDigite uma opção novamente: ')

    if confirmar != 1:
        limpar_tela()
        print(AMARELO + 'Reativação cancelada.')
        confirmacao()
        return False

    if ja_estava_pago:
        lista_pedidos[posicao]['saldo_devedor'] = valor_diferenca
    else:
        lista_pedidos[posicao]['saldo_devedor'] = valor_reativado

    lista_pedidos[posicao]['status_pago'] = 2
    lista_pedidos[posicao]['status_pedido'] = 1
    lista_pedidos[posicao]['valor_pedido'] = valor_reativado
    lista_pedidos[posicao]['id_entregador'] = id_entregador

    limpar_tela()
    print(VERDE + 'Pedido reativado com sucesso!')
    print(BRANCO + f'Novo status: PENDENTE | Novo valor total: R$ {valor_reativado:.2f}')
    print(AMARELO + f'Saldo pendente a pagar: R$ {lista_pedidos[posicao]["saldo_devedor"]:.2f}')
    confirmacao()
    return True


def solicitar_reembolso(lista_pedidos, lista_entregadores):  # Adicionado lista_entregadores como parâmetro
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
    while confirmacao_reembolso is False:
        sub_menu_confirmar("CONFIRMAR REEMBOLSO?")
        confirmacao_reembolso = gerenciar_entrada_numerica(1, 2, BRANCO + "\nDigite uma opção novamente: ")

    if confirmacao_reembolso == 1:
        entregador_afetado = lista_pedidos[posicao]["id_entregador"]

        lista_pedidos[posicao]["status_pedido"] = 5
        lista_pedidos[posicao]["status_pago"] = 3
        lista_pedidos[posicao]["saldo_devedor"] = 0.0
        lista_pedidos[posicao]["id_entregador"] = "0000"

        atualizar_disponibilidade_entregador(entregador_afetado, lista_pedidos, lista_entregadores)

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

def gerar_id_entregador(lista_entregadores):
    id_entregador = str(random.randint(1000, 9999))

    while buscar_posicao_por_id(id_entregador, lista_entregadores, "id_entregador") != -1:
        id_entregador = str(random.randint(1000, 9999))

    return id_entregador

def cadastrar_nome_entregador():
    limpar_tela()
    nome = input(BRANCO + "Insira o nome do entregador (X para cancelar): ")
    if nome.lower() == 'x':
        return None
    while not validar_nome(nome):
        limpar_tela()
        nome = input("Insira o nome do entregador novamente (X para cancelar): ")
        if nome.lower() == 'x':
            return None
    limpar_tela()
    return nome.upper()

def cadastrar_veiculo():
    limpar_tela()
    sub_menu_veiculo()
    veiculo = gerenciar_entrada_numerica(1, 3, "\nDigite uma opção: ")
    while veiculo is False:
        limpar_tela()
        sub_menu_veiculo()
        veiculo = gerenciar_entrada_numerica(1, 3, "\nDigite uma opção novamente: ")
    return veiculo

def cadastrar_estado_entregador():
    limpar_tela()
    sub_menu_estados()
    estado = gerenciar_entrada_numerica(1, 7, "Digite uma opção: ")
    while estado is False:
        limpar_tela()
        sub_menu_estados()
        estado = gerenciar_entrada_numerica(1, 7, "Digite uma opção novamente: ")
    if estado is None:
        return None
    return MAPA_ESTADOS.get(estado, "DESCONHECIDO")

def cadastrar_regiao_entregador():
    limpar_tela()
    sub_menu_regiao()
    regiao = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
    while regiao is False:
        limpar_tela()
        sub_menu_regiao()
        regiao = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")
    return regiao

def cadastrar_turno_entregador():
    limpar_tela()
    sub_menus_turno()
    turno = gerenciar_entrada_numerica(1, 3, "\nDigite uma opção: ")
    while turno is False:
        limpar_tela()
        sub_menus_turno()
        turno = gerenciar_entrada_numerica(1, 3, "\nDigite uma opção novamente: ")
    return turno

def cadastrar_entregador(lista_entregadores):
    campos = ["id_entregador", "nome_entregador", "veiculo", "estado", "regiao", "turno", "disponibilidade"]
    entregador = dict.fromkeys(campos)

    entregador["id_entregador"] = gerar_id_entregador(lista_entregadores)

    entregador["nome_entregador"] = cadastrar_nome_entregador()
    if entregador["nome_entregador"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    entregador["veiculo"] = cadastrar_veiculo()
    if entregador["veiculo"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    entregador["estado"] = cadastrar_estado_entregador()
    if entregador["estado"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    entregador["regiao"] = cadastrar_regiao_entregador()
    if entregador["regiao"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    entregador["turno"] = cadastrar_turno_entregador()
    if entregador["turno"] is None:
        print(AMARELO + "\nCadastro cancelado.")
        confirmacao()
        return False

    entregador["disponibilidade"] = "DISPONIVEL"

    lista_entregadores.append(entregador)

    veiculo_texto = MAPA_VEICULOS.get(entregador["veiculo"], "DESCONHECIDO")
    regiao_texto = MAPA_REGIOES.get(entregador["regiao"], "DESCONHECIDA")
    turno_texto = MAPA_TURNOS.get(entregador["turno"], "DESCONHECIDO")

    limpar_tela()
    print(BRANCO + "----- ENTREGADOR CADASTRADO -----")
    print(f"ID -> {entregador['id_entregador']}")
    print(f"NOME -> {entregador['nome_entregador']}")
    print(f"VEÍCULO -> {veiculo_texto}")
    print(f"ESTADO -> {entregador['estado']}")
    print(f"REGIÃO -> {regiao_texto}")
    print(f"TURNO -> {turno_texto}")
    print(f"DISPONIBILIDADE -> {entregador['disponibilidade']}")
    confirmacao()

def imprimir_ficha_pedido(pedido):
    estado_txt = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
    regiao_txt = MAPA_REGIOES.get(pedido["regiao"], "DESCONHECIDA")
    prioridade_txt = MAPA_PRIORIDADES.get(pedido["prioridade"], "DESCONHECIDO")
    porte_txt = MAPA_PORTES.get(pedido["porte_pedido"], "DESCONHECIDO")
    status_pago_txt = MAPA_STATUS_PAGO.get(pedido["status_pago"], "DESCONHECIDO")
    status_pedido_txt = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")

    saldo = pedido.get("saldo_devedor", pedido["valor_pedido"])

    print(f'\nID:               {pedido["id_pedido"]}'
          f'\nCLIENTE:          {pedido["nome_cliente"]}'
          f'\nESTADO:           {estado_txt}'
          f'\nENDEREÇO:         {pedido["endereco"]}'
          f'\nREGIÃO:           {regiao_txt}'
          f'\nPRIORIDADE:       {prioridade_txt}'
          f'\nDESCRIÇÃO:        {pedido["descricao_pedido"]}'
          f'\nPORTE:            {porte_txt}'
          f'\nVALOR TOTAL:      R$ {pedido["valor_pedido"]:.2f}'
          f'\nSALDO DEVEDOR:    R$ {saldo:.2f}'
          f'\nSTATUS PAGAMENTO: {status_pago_txt}'
          f'\nSTATUS PEDIDO:    {status_pedido_txt}'
          f'\nID ENTREGADOR:    {pedido["id_entregador"]}')
    print("-" * 40)

def pedidos_pendentes(lista_pedidos):
    limpar_tela()
    print(BRANCO + '--- PEDIDOS PENDENTES ---')

    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado.')
        confirmacao()
        return False

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 1 and pedido["prioridade"] == 1:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 1 and pedido["prioridade"] == 2:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    if encontrou == 0:
        print(AMARELO + '\nNenhum pedido pendente no momento.')

    confirmacao()

def pedidos_em_rota(lista_pedidos):
    limpar_tela()
    print(BRANCO + '--- PEDIDOS EM ROTA ---')

    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado.')
        confirmacao()
        return False

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 2 and pedido["prioridade"] == 1:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 2 and pedido["prioridade"] == 2:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    if encontrou == 0:
        print(AMARELO + '\nNenhum pedido em rota no momento.')

    confirmacao()

def pedidos_entregues(lista_pedidos):
    limpar_tela()
    print(BRANCO + '--- PEDIDOS ENTREGUES ---')

    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado no sistema.')
        confirmacao()
        return False

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 3:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    if encontrou == 0:
        print(AMARELO + '\nNenhum pedido entregue encontrado.')

    confirmacao()

def pedidos_cancelados(lista_pedidos):
    limpar_tela()
    print(BRANCO + '--- PEDIDOS CANCELADOS ---')

    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado no sistema.')
        confirmacao()
        return False

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 4:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    if encontrou == 0:
        print(AMARELO + '\nNenhum pedido cancelado encontrado.')

    confirmacao()

def pedidos_reembolsados(lista_pedidos):
    limpar_tela()
    print(BRANCO + '--- PEDIDOS REEMBOLSADOS ---')

    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado no sistema.')
        confirmacao()
        return False

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 5:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    if encontrou == 0:
        print(AMARELO + '\nNenhum pedido reembolsado encontrado.')

    confirmacao()

def buscar_pedido(lista_pedidos):
    limpar_tela()
    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado no sistema.')
        confirmacao()
        return False

    id_busca = input('\nDigite o ID do pedido (X para cancelar): ').upper()
    if id_busca == 'X':
        return False
    while not validar_id_pedido(id_busca):
        limpar_tela()
        id_busca = input('\nID inválido, digite novamente (X para cancelar): ').upper()
        if id_busca == 'X':
            return False

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["id_pedido"] == id_busca:
            limpar_tela()
            print(BRANCO + '--- PEDIDO ENCONTRADO ---')
            imprimir_ficha_pedido(pedido)
            encontrou = 1
            break

    if encontrou == 0:
        print(AMARELO + '\nPedido não encontrado no sistema.')

    confirmacao()

def entregas_entregador(lista_pedidos, lista_entregadores):
    if not lista_entregadores:
        print(AMARELO + "Nenhum Entregador cadastrado no sistema...")
        confirmacao()
        return False

    limpar_tela()
    id_busca = input('Digite o ID do entregador (X para cancelar): ').strip()
    if id_busca.lower() == 'x':
        return False
    while not validar_id_entregador(id_busca):
        limpar_tela()
        id_busca = input('ID inválido, digite novamente (X para cancelar): ').strip()
        if id_busca.lower() == 'x':
            return False

    for entregador in lista_entregadores:
        if entregador["id_entregador"] == id_busca:
            limpar_tela()
            print(BRANCO + f'--- HISTÓRICO DE ENTREGAS DE: {entregador["nome_entregador"].upper()} ---')

            encontrou_pedido = 0

            for pedido in lista_pedidos:
                if pedido["id_entregador"] == id_busca:
                    imprimir_ficha_pedido(pedido)
                    encontrou_pedido = 1

            if encontrou_pedido == 0:
                print(AMARELO + '\nEste entregador não possui nenhuma entrega vinculada.')

            confirmacao()
            return True

    print(AMARELO + '\nEntregador não encontrado no sistema.')
    confirmacao()
    return False

def consultar_entregadores_disponiveis(lista_entregadores):
    limpar_tela()

    if not lista_entregadores:
        print(AMARELO + "Nenhum entregador cadastrado no sistema.")
        confirmacao()
        return False

    print("=== ENTREGADORES DISPONÍVEIS ===\n")
    encontrou = 0

    for entregador in lista_entregadores:
        if entregador["disponibilidade"] == "DISPONIVEL":
            encontrou = 1

            veiculo_texto = MAPA_VEICULOS.get(entregador["veiculo"], "VAN")
            regiao_texto = MAPA_REGIOES.get(entregador["regiao"], "DESCONHECIDA")
            turno_texto = MAPA_TURNOS.get(entregador["turno"], "DESCONHECIDO")

            print(f"ID              -> {entregador['id_entregador']}")
            print(f"NOME            -> {entregador['nome_entregador']}")
            print(f"VEÍCULO         -> {veiculo_texto}")
            print(f"ESTADO          -> {entregador['estado']}")
            print(f"REGIÃO          -> {regiao_texto}")
            print(f"TURNO           -> {turno_texto}")
            print(f"STATUS          -> {entregador['disponibilidade']}")
            print("-" * 35)

    if encontrou == 0:
        limpar_tela()
        print("Não há nenhum entregador disponível no momento.")
        confirmacao()
        return False

    confirmacao()
    return True

def imprimir_ficha_relatorio(pedido):
    estado_txt = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
    regiao_txt = MAPA_REGIOES.get(pedido["regiao"], "DESCONHECIDA")
    status_txt = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")

    saldo = pedido.get("saldo_devedor", pedido["valor_pedido"])

    print(f"ID              : {pedido['id_pedido']}")
    print(f"Cliente         : {pedido['nome_cliente']}")
    print(f"Estado          : {estado_txt}")
    print(f"Região          : {regiao_txt}")
    print(f"Endereço        : {pedido['endereco']}")
    print(f"Valor Total     : R$ {pedido['valor_pedido']:.2f}")
    print(f"Saldo Devedor   : R$ {saldo:.2f}")
    print(f"Status Entrega  : {status_txt}")
    print("-" * 35)

def relatorio_total_pedidos(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- TOTAL DE PEDIDOS ----")

    total = len(lista_pedidos)

    print(f"\nTotal de pedidos cadastrados: {total}")

    if total == 0:
        print(AMARELO + "\nNenhum pedido encontrado na base de dados.")

    confirmacao()

def relatorio_pedidos_por_status(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- PEDIDOS POR STATUS ----")

    pendente = 0
    em_rota = 0
    entregue = 0
    cancelado = 0
    reembolsado = 0

    for pedido in lista_pedidos:
        status = pedido["status_pedido"]

        if status == 1:
            pendente += 1
        elif status == 2:
            em_rota += 1
        elif status == 3:
            entregue += 1
        elif status == 4:
            cancelado += 1
        elif status == 5:
            reembolsado += 1

    print(f"Pendente   : {pendente}")
    print(f"Em Rota    : {em_rota}")
    print(f"Entregue   : {entregue}")
    print(f"Cancelado  : {cancelado}")
    print(f"Reembolsado: {reembolsado}")

    confirmacao()

def relatorio_alta_prioridade_todos(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- PEDIDOS COM ALTA PRIORIDADE ----\n")

    encontrados = 0

    for pedido in lista_pedidos:
        if pedido["prioridade"] == 1:
            encontrados += 1
            imprimir_ficha_relatorio(pedido)

    if encontrados == 0:
        print(AMARELO + "Nenhum pedido com Alta Prioridade encontrado.")
    else:
        print(VERDE + f"\nTotal de pedidos com Alta Prioridade: {encontrados}")

    confirmacao()

def relatorio_alta_prioridade_pendente(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- PEDIDOS COM ALTA PRIORIDADE (PENDENTE) ----\n")

    encontrados = 0

    for pedido in lista_pedidos:
        if pedido["prioridade"] == 1 and pedido["status_pedido"] == 1:
            encontrados += 1
            imprimir_ficha_relatorio(pedido)

    if encontrados == 0:
        print(AMARELO + "Nenhum pedido Pendente com Alta Prioridade encontrado.")
    else:
        print(VERDE + f"\nTotal de pedidos (Pendentes) com Alta Prioridade: {encontrados}")

    confirmacao()

def relatorio_alta_prioridade_em_rota(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- PEDIDOS COM ALTA PRIORIDADE (EM ROTA) ----\n")

    encontrados = 0

    for pedido in lista_pedidos:
        if pedido["prioridade"] == 1 and pedido["status_pedido"] == 2:
            encontrados += 1
            imprimir_ficha_relatorio(pedido)

    if encontrados == 0:
        print(AMARELO + "Nenhum pedido Em Rota com Alta Prioridade encontrado.")
    else:
        print(VERDE + f"\nTotal de pedidos (Em Rota) com Alta Prioridade: {encontrados}")

    confirmacao()

def relatorio_top_entregador(lista_entregadores, lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- ENTREGADOR COM MAIS ENTREGAS ----")

    if not lista_entregadores:
        print(AMARELO + "\nNenhum entregador cadastrado no sistema.")
        confirmacao()
        return

    maior_numero = 0
    nome_lider = ""
    id_lider = ""

    for entregador in lista_entregadores:
        id_atual = entregador["id_entregador"]
        total_entregues = 0

        for pedido in lista_pedidos:
            if pedido["id_entregador"] == id_atual and pedido["status_pedido"] == 3:
                total_entregues += 1

        if total_entregues > maior_numero:
            maior_numero = total_entregues
            nome_lider = entregador["nome_entregador"]
            id_lider = id_atual

    if maior_numero == 0:
        print(AMARELO + "\nNenhum entregador possui entregas concluídas até o momento.")
    else:
        print(VERDE + "\nLÍDER DE ENTREGAS ENCONTRADO:")
        print(BRANCO + f"ID    : {id_lider}")
        print(BRANCO + f"Nome  : {nome_lider}")
        print(VERDE + f"Total : {maior_numero} entrega(s) concluída(s)")

    confirmacao()

def menu_principal():
    lista_pedidos = []
    lista_entregadores = []
    executando_menu_principal = 1

    while executando_menu_principal:
        limpar_tela()
        sub_menu_principal()

        escolha_menu_principal = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
        while not escolha_menu_principal:
            limpar_tela()
            sub_menu_principal()
            escolha_menu_principal = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")

        if escolha_menu_principal == 1:
            executando_menu_pedidos = 1
            while executando_menu_pedidos:
                limpar_tela()
                sub_menu_pedidos()

                escolha_menu_pedidos = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
                while not escolha_menu_pedidos:
                    limpar_tela()
                    sub_menu_pedidos()
                    escolha_menu_pedidos = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")

                match escolha_menu_pedidos:
                    case 1:
                        limpar_tela()
                        cadastrar_pedido(lista_pedidos, lista_entregadores)
                    case 2:
                        limpar_tela()
                        atualizar_pedido(lista_pedidos, lista_entregadores)
                    case 3:
                        limpar_tela()
                        reativar_pedido(lista_pedidos, lista_entregadores)
                    case 4:
                        limpar_tela()
                        solicitar_reembolso(lista_pedidos)
                    case 5:
                        executando_menu_pedidos = 0

        elif escolha_menu_principal == 2:
            executando_menu_entregadores = 1
            while executando_menu_entregadores:
                limpar_tela()
                sub_menu_entregadores()

                escolha_menu_entregadores = gerenciar_entrada_numerica(1, 2, "\nDigite uma opção: ")
                while not escolha_menu_entregadores:
                    limpar_tela()
                    sub_menu_entregadores()
                    escolha_menu_entregadores = gerenciar_entrada_numerica(1, 2, "\nDigite uma opção novamente: ")

                match escolha_menu_entregadores:
                    case 1:
                        limpar_tela()
                        cadastrar_entregador(lista_entregadores)
                    case 2:
                        executando_menu_entregadores = 0

        elif escolha_menu_principal == 3:
            executando_menu_consulta = 1
            while executando_menu_consulta:
                limpar_tela()
                sub_menu_consultas()

                escolha_menu_consulta = gerenciar_entrada_numerica(1, 9, "\nDigite uma opção: ")
                while not escolha_menu_consulta:
                    limpar_tela()
                    sub_menu_consultas()
                    escolha_menu_consulta = gerenciar_entrada_numerica(1, 9, "\nDigite uma opção novamente: ")

                match escolha_menu_consulta:
                    case 1:
                        limpar_tela()
                        pedidos_pendentes(lista_pedidos)
                    case 2:
                        limpar_tela()
                        pedidos_em_rota(lista_pedidos)
                    case 3:
                        limpar_tela()
                        pedidos_entregues(lista_pedidos)
                    case 4:
                        limpar_tela()
                        pedidos_cancelados(lista_pedidos)
                    case 5:
                        limpar_tela()
                        pedidos_reembolsados(lista_pedidos)
                    case 6:
                        buscar_pedido(lista_pedidos)
                    case 7:
                        limpar_tela()
                        consultar_entregadores_disponiveis(lista_entregadores)
                    case 8:
                        limpar_tela()
                        entregas_entregador(lista_pedidos, lista_entregadores)
                    case 9:
                        executando_menu_consulta = 0

        elif escolha_menu_principal == 4:
            executando_menu_relatorios = 1
            while executando_menu_relatorios:
                limpar_tela()
                sub_menu_relatorios()

                escolha_menu_relatorios = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
                while not escolha_menu_relatorios:
                    limpar_tela()
                    sub_menu_relatorios()
                    escolha_menu_relatorios = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")

                match escolha_menu_relatorios:
                    case 1:
                        limpar_tela()
                        relatorio_total_pedidos(lista_pedidos)
                    case 2:
                        limpar_tela()
                        relatorio_pedidos_por_status(lista_pedidos)
                    case 3:
                        executando_alta_prioridade = 1
                        while executando_alta_prioridade:
                            limpar_tela()
                            sub_menu_alta_prioridade()

                            escolha_alta_prioridade = gerenciar_entrada_numerica(1, 4, "\nDigite uma opção: ")
                            while not escolha_alta_prioridade:
                                limpar_tela()
                                sub_menu_alta_prioridade()
                                escolha_alta_prioridade = gerenciar_entrada_numerica(1, 4, "\nDigite uma opção novamente: ")

                            match escolha_alta_prioridade:
                                case 1:
                                    limpar_tela()
                                    relatorio_alta_prioridade_todos(lista_pedidos)
                                case 2:
                                    limpar_tela()
                                    relatorio_alta_prioridade_pendente(lista_pedidos)
                                case 3:
                                    limpar_tela()
                                    relatorio_alta_prioridade_em_rota(lista_pedidos)
                                case 4:
                                    executando_alta_prioridade = 0
                    case 4:
                        limpar_tela()
                        relatorio_top_entregador(lista_entregadores, lista_pedidos)
                    case 5:
                        executando_menu_relatorios = 0

        else:
            limpar_tela()
            print(VERDE + "Sistema Finalizado com Sucesso.")
            executando_menu_principal = 0

if __name__ == "__main__":
    init(autoreset=True)
    menu_principal()