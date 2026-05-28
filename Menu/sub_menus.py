from main import BRANCO,VERDE,VERMELHO,AMARELO

def sub_menu_principal():
    print("-----Fluxo Norte-----")
    print("\n[1] PEDIDOS")
    print("[2] ENTREGADORES")
    print("[3] CONSULTA")
    print("[4] RELATÓRIOS")
    print("[5] FINALIZAR SISTEMA")

def sub_menu_pedidos():
    print("-----Pedidos-----")
    print("\n[1] CADASTRO")
    print("[2] ATUALIZAÇÕES")
    print("[3] REATIVAR PEDIDO")
    print("[4] REEMBOLSAR PEDIDO")
    print("[5] VOLTAR")

def sub_menu_entregadores():
    print("-----Entregadores-----")
    print("[1] CADASTRO")
    print("[2] VOLTAR")

def sub_menu_consultas():
    print("-----Consulta-----")
    print("\n[1] PEDIDOS PENDENTES") # POR PRIORIDADE
    print("\n[2] PEDIDOS ENTREGUES")
    print("\n[3] BUSCAR PEDIDO - ID")
    print("\n[4] ENTREGADORES DISPONÍVEIS")
    print("\n[5] TOTAL DE ENTREGAS - POR ENTREGADOR")
    print("[6] VOLTAR")

def sub_menu_relatorios():
    print("-----Relatórios-----")
    print("\n[1] TOTAL DE PEDIDOS")
    print("\n[2] QUANTIDADE DE PEDIDOS - STATUS")
    print("\n[3] PEDIDOS URGENTES")
    print("\n[4] ENTREGADOR COM MAIOR NÚMERO DE ENTREGA")
    print("[5] VOLTAR")

def sub_menu_estados():
    print("[1] Acre (AC)")
    print("[2] Amapá (AP)")
    print("[3] Amazonas (AM)")
    print("[4] Pará (PA)")
    print("[5] Rondônia (RO)")
    print("[6] Roraima (RR)")
    print("[7] Tocantins (TO)")

def sub_menu_veiculo():
    print("-----Veículo-----")
    print("[1] MOTO")
    print("[2] CARRO")
    print("[3] VAN")

def sub_menu_regiao():
    print("-----Região-----")
    print("[1] REGIÃO 1")
    print("[2] REGIÃO 2")
    print("[3] REGIÃO 3")
    print("[4] REGIÃO 4")
    print("[5] REGIÃO 5")

def sub_menus_turno():
    print("-----Turno-----")
    print("[1] MATUTINO -> (07-16)")
    print("[2] VESPERTINO -> (14-23)")
    print("[3] NOTURNO -> (23-07)")