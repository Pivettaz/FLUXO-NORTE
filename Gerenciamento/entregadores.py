from Validacao.validadores import gerenciar_entrada_numerica, validar_nome, validar_id_entregador
from utils import limpar_tela, confirmacao
from Menu.sub_menus import sub_menu_estados, sub_menu_veiculo, sub_menu_regiao, sub_menus_turno
import random
from cores import BRANCO, VERDE, VERMELHO, AMARELO

MAPA_ESTADOS = {1: "AC", 2: "AP", 3: "AM", 4: "PA", 5: "RO", 6: "RR", 7: "TO"}
MAPA_REGIOES = {1: "ZONA NORTE", 2: "ZONA SUL", 3: "ZONA LEST", 4: "ZONA OEST", 5: "CENTRO"}
MAPA_TURNOS = {1: "MANHÃ", 2: "TARDE", 3: "NOITE"}
MAPA_VEICULOS = {1: "MOTO", 2: "CARRO", 3: "VAN"}
MAPA_STATUS_PEDIDO = {1: "PENDENTE", 2: "EM ROTA", 3: "ENTREGUE", 4: "CANCELADO", 5: "REEMBOLSADO"}
MAPA_STATUS_PAGO = {1: "PAGO", 2: "NAO PAGO", 3: "REEMBOLSADO"}
MAPA_PRIORIDADES = {1: "ALTA", 2: "NORMAL"}
MAPA_PORTES = {1: "PEQUENO", 2: "MÉDIO", 3: "GRANDE"}


def gerar_id_entregador():
    return str(random.randint(1000, 9999))


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
        turno = gerenciar_entrada_numerica(1, 3, "\nDigite uma opção novamente: ")
    return turno


def cadastrar_entregador(lista_entregadores):
    campos = ["id_entregador", "nome_entregador", "veiculo", "estado", "regiao", "turno", "disponibilidade"]
    entregador = dict.fromkeys(campos)

    entregador["id_entregador"] = gerar_id_entregador()

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


def imprimir_ficha_pedido_entregador(pedido):
    estado_txt = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
    regiao_txt = MAPA_REGIOES.get(pedido["regiao"], "DESCONHECIDA")
    prioridade_txt = MAPA_PRIORIDADES.get(pedido["prioridade"], "DESCONHECIDO")
    porte_txt = MAPA_PORTES.get(pedido["porte_pedido"], "DESCONHECIDO")
    status_pedido_txt = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")

    print(f'\nID:               {pedido["id_pedido"]}'
          f'\nCLIENTE:          {pedido["nome_cliente"]}'
          f'\nESTADO:           {estado_txt}'
          f'\nENDEREÇO:         {pedido["endereco"]}'
          f'\nREGIÃO:           {regiao_txt}'
          f'\nPRIORIDADE:       {prioridade_txt}'
          f'\nDESCRIÇÃO:        {pedido["descricao_pedido"]}'
          f'\nPORTE:            {porte_txt}'
          f'\nVALOR:            R$ {pedido["valor_pedido"]:.2f}'
          f'\nSTATUS PEDIDO:    {status_pedido_txt}'
          f'\nID ENTREGADOR:    {pedido["id_entregador"]}')
    print("-" * 40)


def listar_pedidos_entregador(lista_pedidos, lista_entregadores):
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
            print(f'=== RELATÓRIO DE ENTREGAS: {entregador["nome_entregador"].upper()} ===\n')

            encontrou_pendente = 0

            print("---- PEDIDOS PENDENTES ----")
            for pedido in lista_pedidos:
                if pedido["id_entregador"] == id_busca and pedido["status_pedido"] == 1:
                    encontrou_pendente = 1
                    imprimir_ficha_pedido_entregador(pedido)

            if encontrou_pendente == 0:
                print("  Nenhum pedido pendente.")

            print("\n" + "-" * 50 + "\n")

            print("---- PEDIDOS EM ROTA ----")
            encontrou_em_rota = 0

            for pedido in lista_pedidos:
                if pedido["id_entregador"] == id_busca and pedido["status_pedido"] == 2:
                    encontrou_em_rota = 1
                    imprimir_ficha_pedido_entregador(pedido)

            if encontrou_em_rota == 0:
                print("  Nenhum pedido em rota.")

            print("\n==================================================")
            if encontrou_pendente == 0 and encontrou_em_rota == 0:
                limpar_tela()
                print('\nEste entregador não possui nenhuma entrega ativa no momento (Pendente/Em Rota).')

            confirmacao()
            return True

    limpar_tela()
    print('\nEntregador não encontrado no sistema.')
    confirmacao()
    return False