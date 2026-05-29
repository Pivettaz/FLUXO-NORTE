import pyfiglet
from cores import BRANCO, AMARELO, VERMELHO, CIANO, PALETA

LARGURA = 44
NAVEGACAO = ("VOLTAR", "FINALIZAR SISTEMA")


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
        ["✅", "PEDIDOS ENTREGUES"],
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
