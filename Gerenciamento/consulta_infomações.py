from Validacao import validadores as val
from utils import confirmacao
from cores import BRANCO,VERDE,VERMELHO,AMARELO


def pedidos_pendentes(lista_pedidos):
    print('\n--- PEDIDOS PENDENTES ---')

    if len(lista_pedidos) == 0:        
        print('\nNenhum pedido cadastrado.')
        confirmacao()
        return False

    encontrou = 0
    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 'PENDENTE' and pedido["prioridade"] == 'ALTA':
            print(f'\nID: {pedido["id_pedido"]}'
                  f'\nCLIENTE: {pedido["nome_cliente"]}'
                  f'\nESTADO: {pedido["estado"]}'
                  f'\nENDEREÇO: {pedido["endereco"]}'
                  f'\nREGIÃO: {pedido["regiao"]}'
                  f'\nPRIORIDADE: {pedido["prioridade"]}'
                  f'\nDESCRIÇÃO: {pedido["descricao_pedido"]}'
                  f'\nPORTE: {pedido["porte_pedido"]}'
                  f'\nVALOR: {pedido["valor_pedido"]}'
                  f'\nSTATUS PEDIDO: {pedido["status_pedido"]}'
                  f'\nID ENTREGADOR: {pedido["id_entregador"]}')
            encontrou = 1

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 'PENDENTE' and pedido["prioridade"] == 'NORMAL':
            print(f'\nID: {pedido["id_pedido"]}'
                  f'\nCLIENTE: {pedido["nome_cliente"]}'
                  f'\nESTADO: {pedido["estado"]}'
                  f'\nENDEREÇO: {pedido["endereco"]}'
                  f'\nREGIÃO: {pedido["regiao"]}'
                  f'\nPRIORIDADE: {pedido["prioridade"]}'
                  f'\nDESCRIÇÃO: {pedido["descricao_pedido"]}'
                  f'\nPORTE: {pedido["porte_pedido"]}'
                  f'\nVALOR: {pedido["valor_pedido"]}'
                  f'\nSTATUS PEDIDO: {pedido["status_pedido"]}'
                  f'\nID ENTREGADOR: {pedido["id_entregador"]}')
            encontrou = 1

    if encontrou == 0:
        print('Nenhum pedido pendente.')    

    confirmacao()

def pedidos_entregues(lista_pedidos):
    print('\n--- PEDIDOS ENTREGUES ---')

    if len(lista_pedidos) == 0:
            print('\nNenhum pedido entregue.')
            confirmacao()
            return False
    
    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 'ENTREGUE':
            print(f'\nID: {pedido["id_pedido"]}'
                  f'\nCLIENTE: {pedido["nome_cliente"]}'
                  f'\nESTADO: {pedido["estado"]}'
                  f'\nENDEREÇO: {pedido["endereco"]}'
                  f'\nREGIÃO: {pedido["regiao"]}'
                  f'\nPRIORIDADE: {pedido["prioridade"]}'
                  f'\nDESCRIÇÃO: {pedido["descricao_pedido"]}'
                  f'\nPORTE: {pedido["porte_pedido"]}'
                  f'\nVALOR: {pedido["valor_pedido"]}'
                  f'\nSTATUS PAGAMENTO: {pedido["status_pago"]}'
                  f'\nSTATUS PEDIDO: {pedido["status_pedido"]}'
                  f'\nID ENTREGADOR: {pedido["id_entregador"]}')
            encontrou = 1
            
        if encontrou == 0:
            print('Nenhum pedido entregue.')

        confirmacao()


def buscar_pedido(lista_pedidos):

    if len(lista_pedidos) == 0:        
        print('\nNenhum pedido cadastrado.')
        confirmacao()
        return False
    
    id_busca = input('\nDigite o ID do pedido: ').upper()
    while not val.validar_id_pedido(id_busca):
        id_busca = input('\nID inválido, digite novamente: ').upper()

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["id_pedido"] == id_busca:
            print(f'\n--- PEDIDO ENCONTRADO ---'
                  f'\nID: {pedido["id_pedido"]}'
                  f'\nCLIENTE: {pedido["nome_cliente"]}'
                  f'\nESTADO: {pedido["estado"]}'
                  f'\nENDEREÇO: {pedido["endereco"]}'
                  f'\nREGIÃO: {pedido["regiao"]}'
                  f'\nPRIORIDADE: {pedido["prioridade"]}'
                  f'\nDESCRIÇÃO: {pedido["descricao_pedido"]}'
                  f'\nPORTE: {pedido["porte_pedido"]}'
                  f'\nVALOR: {pedido["valor_pedido"]}'
                  f'\nSTATUS PAGAMENTO: {pedido["status_pago"]}'
                  f'\nSTATUS PEDIDO: {pedido["status_pedido"]}'
                  f'\nID ENTREGADOR: {pedido["id_entregador"]}')
            encontrou = 1
            
    if encontrou == 0:    
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
                        f'\nCLIENTE: {pedido["nome_cliente"]}'
                        f'\nESTADO: {pedido["estado"]}'
                        f'\nENDEREÇO: {pedido["endereco"]}'
                        f'\nREGIÃO: {pedido["regiao"]}'
                        f'\nPRIORIDADE: {pedido["prioridade"]}'
                        f'\nPORTE: {pedido["porte_pedido"]}'
                        f'\nSTATUS PAGAMENTO: {pedido["status_pago"]}'
                        f'\nSTATUS PEDIDO: {pedido["status_pedido"]}')
    
                    confirmacao()
            if encontrou == 0:
                print('\nEste entregador não possui entregas.')
                confirmacao()
            return False
        
    print('\nEntregador não encontrado no sistema.')
    confirmacao()