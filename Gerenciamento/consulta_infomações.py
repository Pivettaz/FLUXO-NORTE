from Validacao import validadores as val
from utils import confirmacao
from main import BRANCO,VERDE,VERMELHO,AMARELO


def pedidos_pendentes(lista_pedidos):
    print('\n--- PEDIDOS PENDENTES ---')
    encontrou = 0
    for id_pedido, pedido in lista_pedidos.items():
        if pedido[4] == 'PENDENTE':
            print(f'\nID: {id_pedido} \nCliente: {pedido[0]} \nEndereço: {pedido[1]} \nRegião: {pedido[2]} \nPrioridade: {pedido[3]} \nDescrição: {pedido[4]} \nStatus: {pedido[5]} \nID Entregador: {pedido[6]}')
            encontrou = 1
            confirmacao()
    if encontrou == 0:
        print('\nNenhum pedido pendente.')
        confirmacao()

def pedidos_entregues(lista_pedidos):
    print('\n--- PEDIDOS ENTREGUES ---')
    encontrou = 0
    for id_pedido, pedido in lista_pedidos.items():
        if pedido[4] == 'Entregue':
            print(f'\nID: {id_pedido} \nCliente: {pedido[0]} \nEndereço: {pedido[1]} \nRegião: {pedido[2]} \nPrioridade: {pedido[3]} \nDescrição: {pedido[4]} \nStatus: {pedido[5]} \nID Entregador: {pedido[6]}')
            encontrou = 1
            confirmacao()
    if encontrou == 0:
        confirmacao()
        print('\nNenhum pedido entregue.')

def buscar_pedido(lista_pedidos):
    id_busca = input('\nDigite o ID do pedido: ')
    while not val.validar_id_pedido(id_busca):
        id_busca = input('\n ID inválido, digite novamente: ')

    if id_busca in lista_pedidos:
        pedido = lista_pedidos[id_busca]
        print(f'\n--- PEDIDO ENCONTRADO --- \nID: {id_busca} \nCliente: {pedido[0]} \nEndereço: {pedido[1]} \nRegião: {pedido[2]} \nPrioridade: {pedido[3]} \nDescrição: {pedido[4]} \nStatus: {pedido[5]} \nID Entregador: {pedido[6]}')
        confirmacao()
    else:
        print('\nPedido não encontrado.')
        confirmacao()

def entregadores_disponiveis(lista_entregadores):
    print('\n--- ENTREGADORES DISPONÍVEIS ---')
    encontrou = 0
    for id_entregador, entregador in lista_entregadores.items():
        if entregador[3] == 1:
            print(f'\nID: {id_entregador} \nNome: {entregador[0]} \nVeículo: {entregador[1]}')
            encontrou = 1
            confirmacao()
    if encontrou == 0:
        print('\nNenhum entregador disponível.')
        confirmacao()

def entregas_entregador(lista_pedidos, lista_entregadores):
    id_busca = input('\nDigite o ID do entregador: ')
    while not val.validar_id_entregador(id_busca):
        id_busca = input('\nID inválido, digite novamente: ')

    if id_busca in lista_entregadores:
        print(f'\n--- ENTREGAS DE {lista_entregadores[id_busca][0].upper()} ---')
        encontrou = 0
        for id_pedido, pedido in lista_pedidos.items():
            if pedido[5] == id_busca:
                print(f'\nID: {id_pedido} \nCliente: {pedido[0]} \nStatus: {pedido[4]}')
                encontrou = 1
                confirmacao()

        if encontrou == 0:
            print('\nEste entregador não possui entregas.')
            confirmacao()
    else:
        confirmacao()
        print('\nEntregador não encontrado.')