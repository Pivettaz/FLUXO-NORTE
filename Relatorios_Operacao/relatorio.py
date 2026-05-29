from utils import limpar_tela, confirmacao
from cores import BRANCO, VERDE, VERMELHO, AMARELO

MAPA_ESTADOS = {1: "AC", 2: "AP", 3: "AM", 4: "PA", 5: "RO", 6: "RR", 7: "TO"}
MAPA_REGIOES = {1: "ZONA NORTE", 2: "ZONA SUL", 3: "ZONA LEST", 4: "ZONA OEST", 5: "CENTRO"}
MAPA_STATUS_PEDIDO = {1: "PENDENTE", 2: "EM ROTA", 3: "ENTREGUE", 4: "CANCELADO", 5: "REEMBOLSADO"}
MAPA_STATUS_PAGO = {1: "PAGO", 2: "NAO PAGO", 3: "REEMBOLSADO"}


def relatorio_total_pedidos(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- TOTAL DE PEDIDOS ----")

    total = len(lista_pedidos)

    print(f"Total de pedidos cadastrados: {total}")

    if total == 0:
        print(AMARELO + "Nenhum pedido encontrado na base de dados.")

    confirmacao()


def relatorio_pedidos_por_status(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- PEDIDOS POR STATUS ----")

    pendente = 0
    em_rota = 0
    entregue = 0
    cancelado = 0
    reembolsado = 0

    for pedido in lista_pedidos:
        status = pedido["status_pedido"]

        if status == 1:
            pendente += 1
        elif status == 2:
            em_rota += 1
        elif status == 3:
            entregue += 1
        elif status == 4:
            cancelado += 1
        elif status == 5:
            reembolsado += 1

    print(f"Pendente   : {pendente}")
    print(f"Em Rota    : {em_rota}")
    print(f"Entregue   : {entregue}")
    print(f"Cancelado  : {cancelado}")
    print(f"Reembolsado: {reembolsado}")

    confirmacao()


def relatorio_alta_prioridade_todos(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- PEDIDOS COM ALTA PRIORIDADE ----")

    encontrados = 0

    for pedido in lista_pedidos:
        if pedido["prioridade"] == 1:
            encontrados += 1

            estado_txt = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
            regiao_txt = MAPA_REGIOES.get(pedido["regiao"], "DESCONHECIDA")
            status_txt = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")

            print(f"ID      : {pedido['id_pedido']}")
            print(f"Cliente : {pedido['nome_cliente']}")
            print(f"Estado  : {estado_txt}")
            print(f"Região  : {regiao_txt}")
            print(f"Endereço: {pedido['endereco']}")
            print(f"Status  : {status_txt}")
            print("-" * 30)

    if encontrados == 0:
        print(AMARELO + "Nenhum pedido com Alta Prioridade encontrado.")
    else:
        print(VERDE + f"Total de pedidos com Alta Prioridade: {encontrados}")

    confirmacao()

def relatorio_alta_prioridade_pendente(lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- PEDIDOS COM ALTA PRIORIDADE (PENDENTE) ----")

    encontrados = 0

    for pedido in lista_pedidos:
        if pedido["prioridade"] == 1 and pedido["status_pedido"] == 1:
            encontrados += 1

            estado_txt = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
            regiao_txt = MAPA_REGIOES.get(pedido["regiao"], "DESCONHECIDA")
            status_txt = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")

            print(f"ID      : {pedido['id_pedido']}")
            print(f"Cliente : {pedido['nome_cliente']}")
            print(f"Estado  : {estado_txt}")
            print(f"Região  : {regiao_txt}")
            print(f"Endereço: {pedido['endereco']}")
            print(f"Status  : {status_txt}")
            print("-" * 30)

    if encontrados == 0:
        print(AMARELO + "Nenhum pedido Pendente com Alta Prioridade encontrado.")
    else:
        print(VERDE + f"Total de pedidos (Pendentes) com Alta Prioridade: {encontrados}")

    confirmacao()

def relatorio_alta_prioridade_em_rota(lista_pedidos):
        limpar_tela()
        print(BRANCO + "---- PEDIDOS COM ALTA PRIORIDADE (PENDENTE) ----")

        encontrados = 0

        for pedido in lista_pedidos:
            if pedido["prioridade"] == 1 and pedido["status_pedido"] == 2:
                encontrados += 1

                estado_txt = MAPA_ESTADOS.get(pedido["estado"], "DESCONHECIDO")
                regiao_txt = MAPA_REGIOES.get(pedido["regiao"], "DESCONHECIDA")
                status_txt = MAPA_STATUS_PEDIDO.get(pedido["status_pedido"], "DESCONHECIDO")

                print(f"ID      : {pedido['id_pedido']}")
                print(f"Cliente : {pedido['nome_cliente']}")
                print(f"Estado  : {estado_txt}")
                print(f"Região  : {regiao_txt}")
                print(f"Endereço: {pedido['endereco']}")
                print(f"Status  : {status_txt}")
                print("-" * 30)

        if encontrados == 0:
            print(AMARELO + "Nenhum pedido Em Rota com Alta Prioridade encontrado.")
        else:
            print(VERDE + f"Total de pedidos (Em Rota) com Alta Prioridade: {encontrados}")

        confirmacao()


def relatorio_top_entregador(lista_entregadores, lista_pedidos):
    limpar_tela()
    print(BRANCO + "---- ENTREGADOR COM MAIS ENTREGAS ----")

    if not lista_entregadores:
        print(AMARELO + "Nenhum entregador cadastrado no sistema.")
        confirmacao()
        return

    maior_numero = 0
    nome_lider = ""
    id_lider = ""

    for entregador in lista_entregadores:
        id_atual = entregador["id_entregador"]
        total_entregues = 0

        for pedido in lista_pedidos:
            if pedido["id_entregador"] == id_atual and pedido["status_pedido"] == 3:
                total_entregues += 1

        if total_entregues > maior_numero:
            maior_numero = total_entregues
            nome_lider = entregador["nome_entregador"]
            id_lider = id_atual

    if maior_numero == 0:
        print(AMARELO + "Nenhum entregador possui entregas concluídas até o momento.")
    else:
        print(VERDE + "LÍDER DE ENTREGAS ENCONTRADO:")
        print(BRANCO + f"ID    : {id_lider}")
        print(BRANCO + f"Nome  : {nome_lider}")
        print(VERDE + f"Total : {maior_numero} entrega(s) concluída(s)")

    confirmacao()