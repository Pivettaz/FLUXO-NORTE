from Validacao.validadores import gerenciar_entrada_numerica, validar_nome, validar_id_entregador
from utils import limpar_tela, confirmacao
from Menu.sub_menus import sub_menu_estados, sub_menu_veiculo, sub_menu_regiao, sub_menus_turno
import random
from cores import BRANCO, VERDE, VERMELHO, AMARELO
from pedidos import buscar_posicao_por_id


def gerar_id_entregador():
    return str(random.randint(1000, 9999))

def cadastrar_nome_entregador():
    limpar_tela()
    nome = input(BRANCO + "Insira o nome do entregador: ")
    while not validar_nome(nome):
        limpar_tela()
        nome = input(AMARELO + "Insira o nome do entregador novamente: ")
    limpar_tela()
    return nome.upper()

def cadastrar_veiculo():
    limpar_tela()
    sub_menu_veiculo()
    veiculo = gerenciar_entrada_numerica(1, 3, "\nDigite uma opção: ")
    while not veiculo:
        limpar_tela()
        sub_menu_veiculo()
        veiculo = gerenciar_entrada_numerica(1, 3, "\nDigite uma opção novamente: ")
    return veiculo

def cadastrar_estado_entregador():
    limpar_tela()
    sub_menu_estados()
    estado = gerenciar_entrada_numerica(1, 7, "Digite uma opção: ")
    while not estado:
        limpar_tela()
        sub_menu_estados()
        estado = gerenciar_entrada_numerica(1, 7, "Digite uma opção novamente: ")
    estados_norte = ["", "AC", "AP", "AM", "PA", "RO", "RR", "TO"]
    return estados_norte[estado]

def cadastrar_regiao_entregador():
    limpar_tela()
    sub_menu_regiao()
    regiao = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
    while not regiao:
        limpar_tela()
        sub_menu_regiao()
        regiao = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")
    return str(regiao)

def cadastrar_turno_entregador():
    limpar_tela()
    sub_menus_turno()

    turno = gerenciar_entrada_numerica(1,3, "\nDigite uma opção: ")
    while not turno:
        turno = gerenciar_entrada_numerica(1, 3, "\nDigite uma opção novamente: ")

    return turno

def cadastrar_entregador(lista_entregadores):
    campos = ["id_entregador", "nome_entregador", "veiculo", "estado", "regiao", "turno", "disponibilidade"]
    entregador = dict.fromkeys(campos)

    entregador["id_entregador"] = gerar_id_entregador()
    entregador["nome_entregador"] = cadastrar_nome_entregador()
    entregador["veiculo"] = cadastrar_veiculo()
    entregador["estado"] = cadastrar_estado_entregador()
    entregador["regiao"] = cadastrar_regiao_entregador()
    entregador["turno"] = cadastrar_turno_entregador()
    entregador["disponibilidade"] = "DISPONÍVEL"

    lista_entregadores.append(entregador)

    if entregador["veiculo"] == 1:
        veiculo_texto = "MOTO"
    elif entregador["veiculo"] == 2:
        veiculo_texto = "CARRO"
    else:
        veiculo_texto = "VAN"

    limpar_tela()
    print(BRANCO + "-----ENTREGADOR CADASTRADO-----")
    print(f"ID -> {entregador['id_entregador']}")
    print(f"NOME -> {entregador['nome_entregador']}")
    print(f"VEÍCULO -> {veiculo_texto}")
    print(f"ESTADO -> {entregador['estado']}")
    print(f"REGIÃO -> {entregador['regiao']}")
    print(f"TURNO -> {entregador['turno']}")
    print(f"DISPONIBILIDADE -> {entregador['disponibilidade']}")
    confirmacao()


def listar_pedidos_entregador(lista_pedidos, lista_entregadores):
    limpar_tela()
    id_busca = input('Digite o ID do entregador: ').strip()
    while not validar_id_entregador(id_busca):
        limpar_tela()
        id_busca = input('ID inválido, digite novamente: ').strip()

    for entregador in lista_entregadores:
        if entregador["id_entregador"] == id_busca:
            limpar_tela()
            print(f'=== RELATÓRIO DE ENTREGAS: {entregador["nome_entregador"].upper()} ===\n')

            encontrou_pendente = 0

            print("----PEDIDOS PENDENTES----")
            for pedido in lista_pedidos:
                if pedido["id_entregador"] == id_busca and pedido["status_pedido"] == "PENDENTE":
                    encontrou_pendente = 1
                    print(f'\nID: {pedido["id_pedido"]}'
                          f'\nCLIENTE: {pedido["nome_cliente"]}'
                          f'\nESTADO: {pedido["estado"]}'
                          f'\nENDEREÇO: {pedido["endereco"]}'
                          f'\nREGIÃO: {pedido["regiao"]}'
                          f'\nPRIORIDADE: {pedido["prioridade"]}'
                          f'\nDESCRIÇÃO: {pedido["descricao_pedido"]}'
                          f'\nPORTE: {pedido["porte_pedido"]}'
                          f'\nVALOR: R$ {pedido["valor_pedido"]:.2f}'  
                          f'\nSTATUS PEDIDO: {pedido["status_pedido"]}'
                          f'\nID ENTREGADOR: {pedido["id_entregador"]}')

            if encontrou_pendente == 0:
                print(" Nenhum pedido pendente.")

            print("\n" + "-" * 50 + "\n")

            print("---PEDIDOS EM ROTA----")
            encontrou_em_rota = 0

            for pedido in lista_pedidos:
                if pedido["id_entregador"] == id_busca and pedido["status_pedido"] == "EM ROTA":
                    encontrou_em_rota = 1
                    print(f'\nID: {pedido["id_pedido"]}'
                          f'\nCLIENTE: {pedido["nome_cliente"]}'
                          f'\nESTADO: {pedido["estado"]}'
                          f'\nENDEREÇO: {pedido["endereco"]}'
                          f'\nREGIÃO: {pedido["regiao"]}'
                          f'\nPRIORIDADE: {pedido["prioridade"]}'
                          f'\nDESCRIÇÃO: {pedido["descricao_pedido"]}'
                          f'\nPORTE: {pedido["porte_pedido"]}'
                          f'\nVALOR: R$ {pedido["valor_pedido"]:.2f}'  
                          f'\nSTATUS PEDIDO: {pedido["status_pedido"]}'
                          f'\nID ENTREGADOR: {pedido["id_entregador"]}')

            if encontrou_em_rota == 0:
                print("Nenhum pedido em rota.")

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



