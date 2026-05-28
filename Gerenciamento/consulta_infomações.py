from Validacao import validadores as val
from utils import confirmacao, limpar_tela
from cores import BRANCO, VERDE, VERMELHO, AMARELO

MAPA_ESTADOS = {1: "AC", 2: "AP", 3: "AM", 4: "PA", 5: "RO", 6: "RR", 7: "TO"}
MAPA_REGIOES = {1: "ZONA NORTE", 2: "ZONA SUL", 3: "ZONA LEST", 4: "ZONA OEST", 5: "CENTRO"}
MAPA_PRIORIDADES = {1: "ALTA", 2: "NORMAL"}
MAPA_PORTES = {1: "PEQUENO", 2: "MÉDIO", 3: "GRANDE"}
MAPA_STATUS_PEDIDO = {1: "PENDENTE", 2: "EM ROTA", 3: "ENTREGUE", 4: "CANCELADO", 5: "REEMBOLSADO"}
MAPA_STATUS_PAGO = {1: "PAGO", 2: "NAO PAGO", 3: "REEMBOLSADO"}


def imprimir_ficha_pedido(pedido):
    estado_txt = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
    regiao_txt = MAPA_REGIOES.get(pedido["regiao"], "DESCONHECIDA")
    prioridade_txt = MAPA_PRIORIDADES.get(pedido["prioridade"], "DESCONHECIDO")
    porte_txt = MAPA_PORTES.get(pedido["porte_pedido"], "DESCONHECIDO")
    status_pago_txt = MAPA_STATUS_PAGO.get(pedido["status_pago"], "DESCONHECIDO")
    status_pedido_txt = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")

    print(f'\nID:               {pedido["id_pedido"]}'
          f'\nCLIENTE:          {pedido["nome_cliente"]}'
          f'\nESTADO:           {estado_txt}'
          f'\nENDEREÇO:         {pedido["endereco"]}'
          f'\nREGIÃO:           {regiao_txt}'
          f'\nPRIORIDADE:       {prioridade_txt}'
          f'\nDESCRIÇÃO:        {pedido["descricao_pedido"]}'
          f'\nPORTE:            {porte_txt}'
          f'\nVALOR:            R$ {pedido["valor_pedido"]:.2f}'
          f'\nSTATUS PAGAMENTO: {status_pago_txt}'
          f'\nSTATUS PEDIDO:    {status_pedido_txt}'
          f'\nID ENTREGADOR:    {pedido["id_entregador"]}')
    print("-" * 40)


def pedidos_pendentes(lista_pedidos):
    limpar_tela()
    print(BRANCO + '--- PEDIDOS PENDENTES ---')

    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado.')
        confirmacao()
        return False

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 1 and pedido["prioridade"] == 1:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 1 and pedido["prioridade"] == 2:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    if encontrou == 0:
        print(AMARELO + '\nNenhum pedido pendente no momento.')

    confirmacao()


def pedidos_entregues(lista_pedidos):
    limpar_tela()
    print(BRANCO + '--- PEDIDOS ENTREGUES ---')

    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado no sistema.')
        confirmacao()
        return False

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["status_pedido"] == 3:
            imprimir_ficha_pedido(pedido)
            encontrou = 1

    if encontrou == 0:
        print(AMARELO + '\nNenhum pedido entregue encontrado.')

    confirmacao()


def buscar_pedido(lista_pedidos):
    limpar_tela()
    if len(lista_pedidos) == 0:
        print(AMARELO + '\nNenhum pedido cadastrado no sistema.')
        confirmacao()
        return False

    id_busca = input('\nDigite o ID do pedido: ').upper()
    while not val.validar_id_pedido(id_busca):
        limpar_tela()
        id_busca = input('\nID inválido, digite novamente: ').upper()

    encontrou = 0

    for pedido in lista_pedidos:
        if pedido["id_pedido"] == id_busca:
            limpar_tela()
            print(BRANCO + '--- PEDIDO ENCONTRADO ---')
            imprimir_ficha_pedido(pedido)
            encontrou = 1
            break

    if encontrou == 0:
        print(AMARELO + '\nPedido não encontrado no sistema.')

    confirmacao()


def entregas_entregador(lista_pedidos, lista_entregadores):
    if not lista_entregadores:
        print(AMARELO + "Nenhum Entregador cadastrado no sistema...")
        confirmacao()
        return False

    limpar_tela()
    id_busca = input('Digite o ID do entregador: ').strip()
    while not val.validar_id_entregador(id_busca):
        limpar_tela()
        id_busca = input('ID inválido, digite novamente: ').strip()

    for entregador in lista_entregadores:
        if entregador["id_entregador"] == id_busca:
            limpar_tela()
            print(BRANCO + f'--- HISTÓRICO DE ENTREGAS DE: {entregador["nome_entregador"].upper()} ---')

            encontrou_pedido = 0

            for pedido in lista_pedidos:
                if pedido["id_entregador"] == id_busca:
                    imprimir_ficha_pedido(pedido)
                    encontrou_pedido = 1

            if encontrou_pedido == 0:
                print(AMARELO + '\nEste entregador não possui nenhuma entrega vinculada.')

            confirmacao()
            return True

    print(AMARELO + '\nEntregador não encontrado no sistema.')
    confirmacao()
    return False


def consultar_entregadores_disponiveis(lista_entregadores):
    limpar_tela()

    if not lista_entregadores:
        print(AMARELO + "Nenhum entregador cadastrado no sistema.")
        confirmacao()
        return False

    print("=== ENTREGADORES DISPONÍVEIS ===\n")
    encontrou = 0

    opcoes_veiculos = {1: "MOTO", 2: "CARRO", 3: "VAN"}

    for entregador in lista_entregadores:
        if entregador["disponibilidade"] == "DISPONIVEL":
            encontrou = 1

            veiculo_texto = opcoes_veiculos.get(entregador["veiculo"], "VAN")

            print(f"ID              -> {entregador['id_entregador']}")
            print(f"NOME            -> {entregador['nome_entregador']}")
            print(f"VEÍCULO         -> {veiculo_texto}")
            print(f"ESTADO          -> {entregador['estado']}")
            print(f"REGIÃO          -> {entregador['regiao']}")
            print(f"TURNO           -> {entregador['turno']}")
            print(f"STATUS          -> {entregador['disponibilidade']}")
            print("-" * 35)

    if encontrou == 0:
        limpar_tela()
        print("Não há nenhum entregador disponível no momento.")
        confirmacao()
        return False

    confirmacao()
    return True