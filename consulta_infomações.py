def pedidos_pendentes(lista_pedidos):
    print('\n--- PEDIDOS PENDENTES ---')
    encontrou = 0
    for id_pedido, pedido in lista_pedidos.items():
        if pedido[4] == 'Pendente':
            print(f'\nID: {id_pedido} \nCliente: {pedido[0]} \nEndereço: {pedido[1]} \nPrioridade: {pedido[2]} \nDescrição: {pedido[3]} \nStatus: {pedido[4]} \nID Entregador: {pedido[5]}')
            encontrou = 1
    if encontrou == 0:
        print('\nNenhum pedido pendente.')

def pedidos_entregues(lista_pedidos):
    print('\n--- PEDIDOS ENTREGUES ---')
    encontrou = 0
    for id_pedido, pedido in lista_pedidos.items():
        if pedido[4] == 'Entregue':
            print(f'\nID: {id_pedido} \nCliente: {pedido[0]} \nEndereço: {pedido[1]} \nPrioridade: {pedido[2]} \nDescrição: {pedido[3]} \nStatus: {pedido[4]} \nID Entregador: {pedido[5]}')
            encontrou = 1
    if encontrou == 0:
        print('\nNenhum pedido entregue.')

def buscar_pedido(lista_pedidos):
    id_busca = input('\n Digite o ID do pedido: ')

    while len(id_busca) != 5 or id_busca[0].isalpha() == False or id_busca[1:].isdigit() == False:
        print('\nID inválido! O ID deve iniciar com uma letra seguida de 4 números.')
        id_busca = input('\nDigite o ID do pedido novamente: ').upper()
    
    if id_busca in lista_pedidos:
        pedido = lista_pedidos[id_busca]
        print(f'\n--- PEDIDO ENCONTRADO --- \nID: {id_busca} \nCliente: {pedido[0]} \nEndereço: {pedido[1]} \nPrioridade: {pedido[2]} \nDescrição: {pedido[3]} \nStatus: {pedido[4]} \nID Entregador: {pedido[5]}')
    else:
        print('\nPedido não encontrado.')

def entregadores_disponiveis(lista_entregadores):
    print('\n--- ENTREGADORES DISPONÍVEIS ---')
    encontrou = 0
    for id_entregador, entregador in lista_entregadores.items():
        if entregador[3] == 1:
            print(f'\nID: {id_entregador} \nNome: {entregador[0]} \nVeículo: {entregador[1]}')
            encontrou = 1
    if encontrou == 0:
        print('\nNenhum entregador disponível.')

def entregas_entregador(lista_pedidos, lista_entregadores):
    id_busca = input('\nDigite o ID do entregador: ')
    if id_busca in lista_entregadores:
        print(f'\n--- ENTREGAS DE {lista_entregadores[id_busca][0].upper()} ---')
        encontrou = 0
        for id_pedido, pedido in lista_pedidos.items():
            if pedido[5] == id_busca:
                print(f'\nID: {id_pedido} \nCliente: {pedido[0]} \nStatus: {pedido[4]}')
                encontrou = 1
        if encontrou == 0:
            print('\nEste entregador não possui entregas.')
    else:
        print('\nEntregador não encontrado.')