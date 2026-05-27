from Validacao.validadores import gerenciar_entrada_numerica, validar_id_entregador, validar_id_pedido, validar_regiao
from utils import limpar_tela, confirmacao
from colorama import Style, Fore
from Menu.sub_menus import sub_menu_estados

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

def cadastrar_nome():
    nome = input(Fore.WHITE + Style.BRIGHT + "Insira o nome do cliente: ")
    while len(nome) < 3 or  not nome.isalpha():
        print("Nome inválido! -> Deve conter mais de 3 letras e não conter símbolos ou números")
        nome = input("Insira o nome do cliente: ")
    limpar_tela()
    return nome.upper()

def cadastrar_estado():
    sub_menu_estados()
    estado = gerenciar_entrada_numerica(1,7,"Digite uma opção: ")

    while not estado:
        estado = gerenciar_entrada_numerica(1,7,"Digite uma opção novamente: ")
    return estado

def cadastrar_endereco():
    endereco = input("Digite o endereço do pedido: ")
    # implementar barreiras
    limpar_tela()
    return endereco.upper()

def cadastrar_regiao():
    regiao_pedido = input(Fore.WHITE + Style.BRIGHT + "Insira a região do endereço: ")
    while not validar_regiao(regiao_pedido):
        limpar_tela()
        regiao_pedido = input(Fore.YELLOW + Style.BRIGHT + "Insira a região do endereço novamente: ")
    return regiao_pedido

def cadastrar_prioridade():
    prioridade = gerenciar_entrada_numerica(1, 2,
                                                    Fore.WHITE + Style.BRIGHT + "\nPRIORIDADE \n[1] ALTA \n[2] NORMAL "
                                                                                "\nDigite uma opção: ")
    while not prioridade:
        limpar_tela()
        prioridade = gerenciar_entrada_numerica(1, 2, Fore.YELLOW + Style.BRIGHT + "\nPRIORIDADE "
                                                                                           "\n[1] ALTA \n[2] NORMAL "
                                                                                           "\nDigite uma opção novamente: ")
        return prioridade

def cadastrar_descricao():
   descricao = input(Fore.WHITE + Style.BRIGHT + "Insira a descrição do produto: ")
   limpar_tela()
   return descricao

def cadastrar_porte():
    porte = gerenciar_entrada_numerica(1, 3, Fore.YELLOW + Style.BRIGHT + "\nPORTE "
                                                                                  "\n[1] BAIXO \n[2] MEDIO [3] GRANDE "
                                                                                  "\nDigite uma opção: ")

    while not porte:
        limpar_tela()
        porte = gerenciar_entrada_numerica(1, 3, Fore.YELLOW + Style.BRIGHT + "\nPORTE "
                                                                                      "\n[1] BAIXO \n[2] MEDIO [3] GRANDE "
                                                                                      "\nDigite uma opção novamente: ")
        limpar_tela()
        return porte

def cadastrar_valor():
    valor = input(Fore.WHITE + Style.BRIGHT + "Insira o valor do produto: ")
    while not valor.isdigit():
        valor = input(Fore.WHITE + Style.BRIGHT + "Valor deve conter apenas números \nInsira o valor do produto novamente")
    limpar_tela()
    return valor


def cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao):
    id_entregador = input(Fore.WHITE + Style.BRIGHT + "Insira o ID do entregador responsável: ")
    while not validar_id_entregador(id_entregador):
        limpar_tela()
        id_entregador = input(Fore.YELLOW + Style.BRIGHT + "Insira o ID do entregador responsável novamente: ")

    estados_norte = ["", "AC", "AP", "AM", "PA", "RO", "RR", "TO"]

    if 1 <= estado<= 7:
        estado_sigla = estados_norte[estado]
    else:
        print("Código de estado inválido.")
        confirmacao()
        return False

    if not lista_entregadores:
        print(
            Fore.WHITE + Style.BRIGHT + "\nNenhum entregador cadastrado, pedido ficará como Pendente.\nApós cadastrar um entregador atualize esse pedido.")
        confirmacao()
        return "0000"

    contagem = 0
    for pedidos in lista_pedidos:
        if pedidos["id_entregador"] == id_entregador:
            if pedidos["status_pedido"] in ["PENDENTE", "EM ROTA"]:
                contagem += 1

    if contagem >= 5:
        print(Fore.WHITE + Style.BRIGHT + "\nUm entregador só pode assumir 5 entregas simultâneas")
        confirmacao()
        return False

    for entregador in lista_entregadores:
        if entregador["id_entregador"] == id_entregador:

            if entregador["estado"] != estado_sigla:
                print("Este entregador não pertence a esse estado!")
                confirmacao()
                return False

            if entregador["regiao"] != regiao:
                print("Este entregador pertence ao estado, mas não a essa região!")
                confirmacao()
                return False

            print("Entregador verificado e confirmado para esta rota!")
            confirmacao()
            return id_entregador

    print("Entregador não encontrado no sistema.")
    confirmacao()
    return False

def cadastrar_status(lista_entregadores):
    if not lista_entregadores:
        return 1
    status = gerenciar_entrada_numerica(1, 3, Fore.WHITE + Style.BRIGHT + "\nSTATUS DO PEDIDO "
                                                                                  "\n[1] PENDENTE ""\n[2] EM ROTA \n[3] ENTREGUE"
                                                                                  "\nDigite uma opção: ")
    while not status:
        limpar_tela()
        status = gerenciar_entrada_numerica(1, 3, Fore.YELLOW + Style.BRIGHT + "\nSTATUS DO PEDIDO \n"
                                                                                       "[1] PENDENTE ""\n[2] EM ROTA \n[3] ENTREGUE"
                                                                                       "\nDigite uma opção novamente: ")
        limpar_tela()
        return status

def cadastrar_pedido(lista_pedidos, lista_entregadores):

    campos = ["id_pedido", "nome_cliente", "estado", "endereco", "regiao", "prioridade", "descricao_pedido", "porte_pedido", "valor_pedido", "id_entregador", "status_pedido"]

    pedido = dict.fromkeys(campos)

    pedido["id_pedido"] = gerar_id_pedido()

    pedido["nome_cliente"] = cadastrar_nome()

    estado = cadastrar_estado()

    pedido["estado"] = estado

    pedido["endereco"] = cadastrar_endereco()

    regiao = cadastrar_regiao()

    pedido["regiao"] = regiao

    pedido["prioridade"] = cadastrar_prioridade()

    pedido["descricao_pedido"] =  cadastrar_descricao()

    porte = cadastrar_porte()

    pedido["porte_pedido"] =  porte

    pedido["valor_pedido"] = cadastrar_valor()

    pedido["id_entregador"] = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao, porte)

    pedido["status_pedido"] = cadastrar_status(lista_entregadores)

    lista_pedidos.append(pedido)

    porte_texto = "PEQUENO" if pedido["porte_pedido"] == 1 else "MEDIO" if pedido["status_pedido"] == 2 else "GRANDE"

    estado_texto = "AC" if pedido["estado"] == 1 else "AP" if pedido["estado"] == 2 else "AM" if pedido["estado"] == 3 else "PA" if \
    pedido["estado"] == 4 else "RO" if pedido["estado"] == 5 else "RR" if pedido["estado"] == 6 else "TO" if pedido["estado"] == 7 else "Desconhecido"

    prioridade_texto = "ALTA" if pedido["prioridade"] == 1 else "NORMAL"

    status_texto = "PENDENTE" if pedido["status_pedido"] == 1 else "EM ROTA" if pedido["status_pedido"] == 2 \
        else "ENTREGUE" if pedido["status_pedido"] == 3 else "CANCELADO"

    print(Fore.WHITE + Style.BRIGHT + "-----PEDIDO CADASTRADO-----")
    print(f"ID -> {pedido["id_pedido"]}")
    print(f"CLIENTE -> {pedido["nome_cliente"]}")
    print(f"ESTADO -> {estado_texto}")
    print(f"ENDEREÇO -> {pedido["endereco"]}")
    print(f"REGIÃO -> {pedido["regiao"]}")
    print(f"PRIORIDADE -> {prioridade_texto}")
    print(f"DESCRIÇÃO-> {pedido["descricao_pedido"]}")
    print(f"PORTE -> {porte_texto}")
    print(f"VALOR -> {pedido["valor_pedido"]}")
    print(f"STATUS -> {status_texto}")
    print(f"ID ENTREGADOR -> {pedido["id_entregador"]}")

    confirmacao()
    return True

def buscar_posicao_por_id(id_procurado, lista_pedidos):
    for i, pedido in enumerate(lista_pedidos):
        if pedido['id_pedido'] == id_procurado:
            return i

    return -1

def buscar_id_pedido_atualizar():
    id_pedido = input(Fore.WHITE + Style.BRIGHT + "Digite o ID do pedido que deseja atualizar: ").upper()
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(Fore.YELLOW + Style.BRIGHT + "Digite o ID do pedido que deseja atualizar novamente: ").upper()
    return id_pedido

def atualizar_pedido(lista_pedidos, lista_entregadores):
    if not lista_pedidos:
        print(Fore.YELLOW+ Style.BRIGHT + "Sem pedidos para atualizar...")
        confirmacao()
        return False

    id_pedido = buscar_id_pedido_atualizar()

    posicao = buscar_posicao_por_id(id_pedido, lista_pedidos)

    if posicao == -1:
        print(Fore.YELLOW + Style.BRIGHT + "Pedido não encontrado na base de dados.")
        confirmacao()
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

            escolha_status = gerenciar_entrada_numerica(1, 4, Fore.YELLOW + Style.BRIGHT + "\nSTATUS DO PEDIDO \n"
                                                                                   "[1] PENDENTE ""\n[2] EM ROTA \n[3] ENTREGUE\n [4] CANCELADO"
                                                                                   "\nDigite uma opção: ")
            while not escolha_status:
                escolha_status = gerenciar_entrada_numerica(1, 4, Fore.YELLOW + Style.BRIGHT + "\nSTATUS DO PEDIDO \n"
                                                                                               "[1] PENDENTE ""\n[2] EM ROTA \n[3] ENTREGUE\n [4] CANCELADO"
                                                                                               "\nDigite uma opção novamente: ")


            status_opcoes = ["", "PENDENTE", "EM ROTA", "ENTREGUE", "CANCELADO"]
            status_texto = status_opcoes[escolha_status]

            if lista_pedidos[posicao]["status_pedido"] == status_texto:
                limpar_tela()
                print(Fore.YELLOW+ Style.BRIGHT + f"O pedido já está com o status '{status_texto}'. Nenhuma alteração foi feita.")
                confirmacao()
                return False

            if status_texto == "CANCELADO":
                lista_pedidos[posicao]["id_entregador"] = "0000"

            limpar_tela()
            lista_pedidos[posicao]["status_pedido"] = status_texto
            print(Fore.GREEN + Style.BRIGHT + f"Status do pedido atualizado com sucesso para: {status_texto}")
            confirmacao()
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
                confirmacao()
                return False

            contagem = 0
            for pedidos in lista_pedidos:
                if pedidos["id_entregador"] == id_entregador:
                    contagem += 1

            if contagem >= 5:
                limpar_tela()
                print(Fore.YELLOW+ Style.BRIGHT + "\nUm entregador só pode assumir 5 entregas simultâneas")
                confirmacao()
                return False

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = id_entregador
            print(Fore.GREEN + Style.BRIGHT + "Entregador atualizado com sucesso!")
            confirmacao()
            return True
        case 3:
            if lista_pedidos[posicao]["id_entregador"] == "0000":
                limpar_tela()
                print(Fore.YELLOW + Style.BRIGHT + "O pedido já está sem nenhum entregador associado.")
                confirmacao()
                return False

            limpar_tela()
            lista_pedidos[posicao]["id_entregador"] = "0000"
            print(Fore.GREEN + Style.BRIGHT + "Entregador desassociado do pedido com sucesso.")
            confirmacao()
            return True

        case _:
            limpar_tela()
            print(Fore.RED + Style.BRIGHT + "Opção inválida detectada pelo sistema.")
            confirmacao()
            return False


def reativar_pedido(lista_pedidos, lista_entregadores):
    id_pedido = input(Fore.WHITE + Style.BRIGHT + 'Digite o ID do pedido que deseja reativar: ').upper()
    while not validar_id_pedido(id_pedido):
        limpar_tela()
        id_pedido = input(Fore.YELLOW + Style.BRIGHT + 'Digite o ID do pedido novamente: ').upper()

    posicao = buscar_posicao_por_id(id_pedido, lista_pedidos)

    if posicao == -1:
        limpar_tela()
        print(Fore.YELLOW + Style.BRIGHT + 'Pedido não encontrado na base de dados.')
        confirmacao()
        return False

    if lista_pedidos[posicao]['status_pedido'] != 'CANCELADO':
        limpar_tela()
        print(Fore.YELLOW + Style.BRIGHT + 'Este pedido não está cancelado e não pode ser reativado.')
        confirmacao()
        return False

    estado = lista_pedidos[posicao]['estado']
    regiao = lista_pedidos[posicao]['regiao']

    id_entregador = cadastrar_id_entregador_pedido(lista_pedidos, lista_entregadores, estado, regiao)

    if id_entregador == False:
        limpar_tela()
        print(Fore.YELLOW + Style.BRIGHT + 'Não foi possível reativar o pedido devido a problemas com o entregador.')
        confirmacao()
        return False

    valor_original = lista_pedidos[posicao]['valor_pedido']
    valor_reativado = float(f"{valor_original * 1.10:.2f}")

    limpar_tela()
    print(Fore.WHITE + Style.BRIGHT + '--- CONFIRMAÇÃO DE REATIVAÇÃO ---')
    print(f"ID:             {lista_pedidos[posicao]['id_pedido']}")
    print(f"Cliente:        {lista_pedidos[posicao]['nome_cliente']}")
    print(f"Valor original: R$ {valor_original:.2f}")
    print(f"Valor com +10%: R$ {valor_reativado:.2f}")

    confirmar = gerenciar_entrada_numerica(1, 2,
                                           Fore.YELLOW + Style.BRIGHT + '\nDeseja reativar esse pedido? \n[1] SIM \n[2] NÃO \nDigite uma opção: ')

    if confirmar != 1:
        limpar_tela()
        print(Fore.YELLOW + Style.BRIGHT + 'Reativação cancelada.')
        confirmacao()
        return False

    lista_pedidos[posicao]['status_pedido'] = 'PENDENTE'
    lista_pedidos[posicao]['valor_pedido'] = valor_reativado
    lista_pedidos[posicao]['id_entregador'] = id_entregador

    limpar_tela()
    print(Fore.GREEN + Style.BRIGHT + 'Pedido reativado com sucesso!')
    print(f'Novo status: PENDENTE | Novo valor: R$ {valor_reativado:.2f}')
    confirmacao()
    return True