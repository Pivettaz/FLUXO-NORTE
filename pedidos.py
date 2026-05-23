from validadores import gerenciar_entrada_numerica, validar_id_entregador

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

    campos = ["id_pedido", "nome_cliente", "prioridade", "descricao_pedido", "status_pedido", "id_entregador"]

    pedido = dict.fromkeys(campos)

    pedido["id_pedido"] = gerar_id_pedido()
    pedido["nome_cliente"] = input("Insira o nome do cliente: ")

    print("\nPRIORIDADE \n[1] ALTA \n[2] NORMAL")
    escolha_prioridade = gerenciar_entrada_numerica(1,2)
    while not escolha_prioridade:
        escolha_prioridade = gerenciar_entrada_numerica(1,2)
    pedido["prioridade"] = escolha_prioridade

    pedido["descricao_pedido"] = input("Insira a descrição do produto: ")

    print("\nSTATUS DO PEDIDO \n[1] PENDENTE \n[2] EM ROTA \n[3] ENTREGUE \n[4] CANCELADO")
    escolha_status = gerenciar_entrada_numerica(1, 4)
    while not escolha_status:
        escolha_status = gerenciar_entrada_numerica(1,4)
    pedido["status_pedido"] = escolha_status

    id_entregador = input("Insira o ID do entregador responsável: ")
    while not validar_id_entregador(id_entregador):
        id_entregador = input("Insira o ID do entregador responsável: ")
    pedido["id_entregador"] = id_entregador

    lista_pedidos.append(pedido)

    prioridade_texto = "ALTA" if pedido["prioridade"] == 1 else "NORMAL"
    status_texto = "PENDENTE" if pedido["status_pedido"] == 1 else "EM ROTA" if pedido["status_pedido"] == 2 \
        else "ENTREGUE" if pedido["status_pedido"] == 3 else "CANCELADO"

    print("-----PEDIDO CADASTRADO-----")
    print(f"ID -> {pedido["id_pedido"]}")
    print(f"CLIENTE -> {pedido["nome_cliente"]}")
    print(f"PRIORIDADE -> {prioridade_texto}")
    print(f"DESCRIÇÃO-> {pedido["descricao_pedido"]}")
    print(f"STATUS -> {status_texto}")
    print(f"ID ENTREGADOR -> {pedido["id_entregador"]}")

