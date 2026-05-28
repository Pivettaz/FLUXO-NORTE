from Validacao.validadores import gerenciar_entrada_numerica, validar_nome
from utils import limpar_tela, confirmacao
from Menu.sub_menus import sub_menu_estados, sub_menu_veiculo, sub_menu_regiao, sub_menus_turno
import random
from cores import BRANCO, VERDE, VERMELHO, AMARELO


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
