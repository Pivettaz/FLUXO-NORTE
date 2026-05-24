from Validacao.validadores import gerenciar_entrada_numerica, validar_id_entregador, validar_id_pedido, validar_regiao
from utils import limpar_tela
from colorama import Style, Fore

# lista_pedidos = [] ESTÁ LISTA DEVE ESTAR FORA DA FUNÇÃO NO ARQUIVO PRINCIPAL PARA ADICIONAR OS PEDIDOS
lista_pedidos = []

def gerar_id_pedido():
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "1234567890"

    indice_letra_aleatoria = id(object()) % len(letras)
    semente = id(object())

    letra_aleatoria = letras[indice_letra_aleatoria]
    id_pedido = letra_aleatoria

    for i in range(4):
        semente = (semente * 1103515245 + 12345) % 2**31
        numero_aleatorio = semente % len(numeros)
        id_pedido += str(numero_aleatorio)

    return id_pedido

def cadastrar_pedido():

    campos = ["id_pedido", "nome_cliente", "endereco", "regiao", "prioridade", "descricao_pedido", "status_pedido", "id_entregador"]

    pedido = dict.fromkeys(campos)

    pedido["id_pedido"] = gerar_id_pedido()

    pedido["nome_cliente"] = input(Fore.WHITE + Style.BRIGHT + "Insira o nome do cliente: ")
    limpar_tela()

    pedido["endereco"] = input(Fore.WHITE + Style.BRIGHT + "Insira o endereço do pedido: ")
    limpar_tela()

    regiao_pedido = input(Fore.WHITE + Style.BRIGHT + "Insira a região do endereço: ")
    while not validar_regiao(regiao_pedido):
        limpar_tela()
        regiao_pedido = input(Fore.YELLOW + Style.BRIGHT + "Insira a região do endereço novamente: ")
    pedido["regiao"] = regiao_pedido
    limpar_tela()

    escolha_prioridade = gerenciar_entrada_numerica(1,2, Fore.WHITE+ Style.BRIGHT + "\nPRIORIDADE \n[1] ALTA \n[2] NORMAL "
                                                         "\nDigite uma opção:")
    while not escolha_prioridade:
        limpar_tela()
        escolha_prioridade = gerenciar_entrada_numerica(1,2, Fore.YELLOW + Style.BRIGHT + "\nPRIORIDADE "
                                                                                "\n[1] ALTA \n[2] NORMAL "
                                                                                "\nDigite uma opção novamente:")

    pedido["prioridade"] = escolha_prioridade
    limpar_tela()

    pedido["descricao_pedido"] = input(Fore.WHITE + Style.BRIGHT + "Insira a descrição do produto: ")
    limpar_tela()

    escolha_status = gerenciar_entrada_numerica(1, 4, Fore.WHITE + Style.BRIGHT + "\nSTATUS DO PEDIDO "
                                "\n[1] PENDENTE ""\n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO "
                                "\nDigite uma opção:")
    while not escolha_status:
        limpar_tela()
        escolha_status = gerenciar_entrada_numerica(1,4, Fore.YELLOW + Style.BRIGHT + "\nSTATUS DO PEDIDO \n"
                                                         "[1] PENDENTE ""\n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO "
                                                         "\nDigite uma opção novamente:")
    pedido["status_pedido"] = escolha_status
    limpar_tela()

    id_entregador = input(Fore.WHITE + Style.BRIGHT + "Insira o ID do entregador responsável: ")
    while not validar_id_entregador(id_entregador):
        limpar_tela()
        id_entregador = input(Fore.YELLOW + Style.BRIGHT + "Insira o ID do entregador responsável novamente: ")
    contagem = 0
    for pedidos in lista_pedidos:
        if pedidos["id_entregador"] == id_entregador:
            contagem += 1
    if contagem >= 5:
        print(Fore.WHITE + Style.BRIGHT + "\nUm entregador só pode assumir 5 entregas simultâneas")
        return False
    pedido["id_entregador"] = id_entregador
    limpar_tela()

    lista_pedidos.append(pedido)

    prioridade_texto = "ALTA" if pedido["prioridade"] == 1 else "NORMAL"
    status_texto = "PENDENTE" if pedido["status_pedido"] == 1 else "EM ROTA" if pedido["status_pedido"] == 2 \
        else "ENTREGUE" if pedido["status_pedido"] == 3 else "CANCELADO"

    print(Fore.WHITE + Style.BRIGHT + "-----PEDIDO CADASTRADO-----")
    print(f"ID -> {pedido["id_pedido"]}")
    print(f"CLIENTE -> {pedido["nome_cliente"]}")
    print(f"ENDEREÇO -> {pedido["endereco"]}")
    print(f"REGIÃO -> {pedido["regiao"]}")
    print(f"PRIORIDADE -> {prioridade_texto}")
    print(f"DESCRIÇÃO-> {pedido["descricao_pedido"]}")
    print(f"STATUS -> {status_texto}")
    print(f"ID ENTREGADOR -> {pedido["id_entregador"]}")
    return True

def buscar_posicao_por_id(id_procurado):
    for i, pedido in enumerate(lista_pedidos):
        if pedido['id_pedido'] == id_procurado:
            return i

    return -1


def atualizar_pedido():
    if not lista_pedidos:
        print(Fore.YELLOW+ Style.BRIGHT + "Sem pedidos para atualizar...")
        return False

    id_pedido = input(Fore.WHITE + Style.BRIGHT + "Digite o ID do pedido que deseja atualizar: ").upper()
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(Fore.YELLOW + Style.BRIGHT + "Digite o ID do pedido que deseja atualizar novamente: ").upper()

    posicao = buscar_posicao_por_id(id_pedido)

    if posicao == -1:
        print(Fore.YELLOW + Style.BRIGHT + "Pedido não encontrado na base de dados.")
        return False

    escolha = gerenciar_entrada_numerica(
        1, 3,
        Fore.WHITE + Style.BRIGHT + "\n--- MENU DE ATUALIZAÇÃO ---\n"
        "[1] Alterar Status do Pedido \n"
        "[2] Editar Entregador \n"
        "[3] Desassociar Entregador\n"
        "Escolha uma opção: "
    )

    match escolha:
        case 1:
            limpar_tela()
            escolha_status = gerenciar_entrada_numerica(
                1, 4,
                Fore.WHITE + Style.BRIGHT + "\nSTATUS DO PEDIDO \n"
                "[1] PENDENTE \n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO \n"
                "Digite uma opção: "
            )
            while not escolha_status:
                limpar_tela()
                escolha_status = gerenciar_entrada_numerica(
                    1, 4,
                    Fore.YELLOW + Style.BRIGHT + "\nSTATUS DO PEDIDO \n"
                    "[1] PENDENTE \n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO \n"
                    "Digite uma opção novamente: "
                )

            status_opcoes = ["", "PENDENTE", "EM ROTA", "ENTREGUE", "CANCELADO"]
            status_texto = status_opcoes[escolha_status]

            if lista_pedidos[posicao]["status_pedido"] == status_texto:
                limpar_tela()
                print(Fore.YELLOW+ Style.BRIGHT + f"O pedido já está com o status '{status_texto}'. Nenhuma alteração foi feita.")
                return False

            limpar_tela()
            lista_pedidos[posicao]["status_pedido"] = status_texto
            print(Fore.GREEN + Style.BRIGHT + f"Status do pedido atualizado com sucesso para: {status_texto}")
            return True

        case 2:
            limpar_tela()
            id_entregador = input(Fore.WHITE + Style.BRIGHT + "Insira o ID do entregador responsável: ")
            while not validar_id_entregador(id_entregador):
                limpar_tela()
                id_entregador = input(Fore.YELLOW + Style.BRIGHT + "Insira o ID do entregador responsável novamente: ")

            if lista_pedidos[posicao]["id_entregador"] == id_entregador:
                limpar_tela()
                print(Fore.YELLOW + Style.BRIGHT + "Este entregador já é o responsável por este pedido.")
                return False

            contagem = 0
            for pedidos in lista_pedidos:
                if pedidos["id_entregador"] == id_entregador:
                    contagem += 1

            if contagem >= 5:
                limpar_tela()
                print(Fore.YELLOW+ Style.BRIGHT + "\nUm entregador só pode assumir 5 entregas simultâneas")
                return False

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = id_entregador
            print(Fore.GREEN + Style.BRIGHT + "Entregador atualizado com sucesso!")
            return True
        case 3:
            if lista_pedidos[posicao]["id_entregador"] == "0000":
                limpar_tela()
                print(Fore.YELLOW + Style.BRIGHT + "O pedido já está sem nenhum entregador associado.")
                return False

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = "0000"
            print(Fore.GREEN + Style.BRIGHT + "Entregador desassociado do pedido com sucesso.")
            return True

        case _:
            limpar_tela()
            print(Fore.RED + Style.BRIGHT + "Opção inválida detectada pelo sistema.")
            return False