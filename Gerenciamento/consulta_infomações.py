from Validacao import validadores as val
from utils import confirmacao
from main import BRANCO,VERDE,VERMELHO,AMARELO


def pedidos_pendentes(lista_pedidos):
    print('\n--- PEDIDOS PENDENTES ---')
    encontrou = 0
    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 'PENDENTE' and pedido["prioridade"] == 'ALTA':
            print(f'\nID: {pedido["id_pedido"]}'
                  f'\nCliente: {pedido["nome_cliente"]}'
                  f'\nEstado: {pedido["estado"]}'
                  f'\nEndereço: {pedido["endereco"]}'
                  f'\nRegião: {pedido["regiao"]}'
                  f'\nPrioridade: {pedido["prioridade"]}'
                  f'\nDescrição: {pedido["descricao_pedido"]}'
                  f'\nPorte: {pedido["porte_pedido"]}'
                  f'\nValor: {pedido["valor_pedido"]}'
                  f'\nStatus: {pedido["status_pedido"]}'
                  f'\nID Entregador: {pedido["id_entregador"]}')
            encontrou = 1

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 'PENDENTE' and pedido["prioridade"] == 'NORMAL':
            print(f'\nID: {pedido["id_pedido"]}'
                  f'\nCliente: {pedido["nome_cliente"]}'
                  f'\nEstado: {pedido["estado"]}'
                  f'\nEndereço: {pedido["endereco"]}'
                  f'\nRegião: {pedido["regiao"]}'
                  f'\nPrioridade: {pedido["prioridade"]}'
                  f'\nDescrição: {pedido["descricao_pedido"]}'
                  f'\nPorte: {pedido["porte_pedido"]}'
                  f'\nValor: {pedido["valor_pedido"]}'
                  f'\nStatus: {pedido["status_pedido"]}'
                  f'\nID Entregador: {pedido["id_entregador"]}')
            encontrou = 1
            
    if encontrou == 0:
        print('\nNenhum pedido pendente.')
        confirmacao()
        return False
    
    confirmacao()
    return True


def pedidos_entregues(lista_pedidos):
    print('\n--- PEDIDOS ENTREGUES ---')
    encontrou = 0
    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 'ENTREGUE':
            print(f'\nID: {pedido["id_pedido"]}'
                  f'\nCliente: {pedido["nome_cliente"]}'
                  f'\nEstado: {pedido["estado"]}'
                  f'\nEndereço: {pedido["endereco"]}'
                  f'\nRegião: {pedido["regiao"]}'
                  f'\nPrioridade: {pedido["prioridade"]}'
                  f'\nDescrição: {pedido["descricao_pedido"]}'
                  f'\nPorte: {pedido["porte_pedido"]}'
                  f'\nValor: {pedido["valor_pedido"]}'
                  f'\nStatus: {pedido["status_pedido"]}'
                  f'\nID Entregador: {pedido["id_entregador"]}')
            encontrou = 1
            confirmacao()
    if encontrou == 0:
        print('\nNenhum pedido entregue.')
        confirmacao()


def buscar_pedido(lista_pedidos):
    id_busca = input('\nDigite o ID do pedido: ').upper()
    while not val.validar_id_pedido(id_busca):
        id_busca = input('\nID inválido, digite novamente: ').upper()

    for pedido in lista_pedidos:
        if pedido["id_pedido"] == id_busca:
            print(f'\n--- PEDIDO ENCONTRADO ---'
                  f'\nID: {pedido["id_pedido"]}'
                  f'\nCliente: {pedido["nome_cliente"]}'
                  f'\nEstado: {pedido["estado"]}'
                  f'\nEndereço: {pedido["endereco"]}'
                  f'\nRegião: {pedido["regiao"]}'
                  f'\nPrioridade: {pedido["prioridade"]}'
                  f'\nDescrição: {pedido["descricao_pedido"]}'
                  f'\nPorte: {pedido["porte_pedido"]}'
                  f'\nValor: {pedido["valor_pedido"]}'
                  f'\nStatus: {pedido["status_pedido"]}'
                  f'\nID Entregador: {pedido["id_entregador"]}')
            confirmacao()
            return
    print('\nPedido não encontrado no sistema.')
    confirmacao()


def entregas_entregador(lista_pedidos, lista_entregadores):
    id_busca = input('\nDigite o ID do entregador: ')
    while not val.validar_id_entregador(id_busca):
        id_busca = input('\nID inválido, digite novamente: ')

    for entregador in lista_entregadores:
        if entregador["id_entregador"] == id_busca:
            print(f'\n--- ENTREGAS DE {entregador["nome_entregador"]} ---')
            encontrou = 0
            for pedido in lista_pedidos:
                if pedido["id_entregador"] == id_busca:
                    print(f'\nID: {pedido["id_pedido"]}'
                          f'\nCliente: {pedido["nome_cliente"]}'
                          f'\nStatus: {pedido["status_pedido"]}')
                    encontrou = 1
                    confirmacao()
            if encontrou == 0:
                print('\nEste entregador não possui entregas.')
                confirmacao()
            return
    print('\nEntregador não encontrado no sistema.')
    confirmacao()