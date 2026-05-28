from cores import BRANCO, AMARELO, VERDE

def sub_menu_principal():
    print(BRANCO + "=== FLUXO NORTE - SISTEMA DE LOGÍSTICA ===")
    print("\n[1] PEDIDOS")
    print("[2] ENTREGADORES")
    print("[3] CONSULTAS")
    print("[4] RELATÓRIOS")
    print("[5] FINALIZAR SISTEMA")
    print(BRANCO + "=========================================")

def sub_menu_pedidos():
    print(BRANCO + "--- GERENCIAMENTO DE PEDIDOS ---")
    print("\n[1] CADASTRO")
    print("[2] ATUALIZAÇÕES")
    print("[3] REATIVAR PEDIDO")
    print("[4] REEMBOLSAR PEDIDO")
    print("[5] VOLTAR")
    print(BRANCO + "--------------------------------")

def sub_menu_entregadores():
    print(BRANCO + "--- GERENCIAMENTO DE ENTREGADORES ---")
    print("\n[1] CADASTRO")
    print("[2] VOLTAR")
    print(BRANCO + "------------------------------------")

def sub_menu_consultas():
    print(BRANCO + "--- PAINEL DE CONSULTAS ---")
    print("\n[1] PEDIDOS PENDENTES (POR PRIORIDADE)")
    print("[2] PEDIDOS ENTREGUES")
    print("[3] BUSCAR PEDIDO POR ID")
    print("[4] ENTREGADORES DISPONÍVEIS")
    print("[5] HISTÓRICO DE ENTREGAS POR ENTREGADOR")
    print("[6] VOLTAR")
    print(BRANCO + "---------------------------")

def sub_menu_relatorios():
    print(BRANCO + "--- RELATÓRIOS GERENCIAIS ---")
    print("\n[1] TOTAL DE PEDIDOS CADASTRADOS")
    print("[2] QUANTIDADE DE PEDIDOS POR STATUS")
    print("[3] PEDIDOS DE ALTA PRIORIDADE")
    print("[4] ENTREGADOR LÍDER DE ENTREGAS")
    print("[5] VOLTAR")
    print(BRANCO + "-----------------------------")

def sub_menu_estados():
    print(BRANCO + "--- SELECIONE O ESTADO ---")
    print("\n[1] Acre (AC)")
    print("[2] Amapá (AP)")
    print("[3] Amazonas (AM)")
    print("[4] Pará (PA)")
    print("[5] Rondônia (RO)")
    print("[6] Roraima (RR)")
    print("[7] Tocantins (TO)")

def sub_menu_veiculo():
    print(BRANCO + "--- SELECIONE O VEÍCULO ---")
    print("\n[1] MOTO")
    print("[2] CARRO")
    print("[3] VAN")

def sub_menu_regiao():
    print(BRANCO + "--- SELECIONE A REGIÃO ---")
    print("\n[1] ZONA NORTE")
    print("[2] ZONA SUL")
    print("[3] ZONA LESTE")
    print("[4] ZONA OESTE")
    print("[5] CENTRO")

def sub_menus_turno():
    print(BRANCO + "--- SELECIONE O TURNO ---")
    print("\n[1] MATUTINO   -> (07h às 16h)")
    print("[2] VESPERTINO -> (14h às 23h)")
    print("[3] NOTURNO    -> (23h às 07h)")