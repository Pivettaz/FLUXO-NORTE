def relatorio_total_pedidos(pedidos):
    print("")
    print("---- TOTAL DE PEDIDOS ----")

    total = 0
    for pid in pedidos:
        total = total + 1

    print("Total de pedidos cadastrados: " + str(total))

    if total == 0:
        print("Nenhum pedido encontrado.")

    print("")


def relatorio_pedidos_por_status(pedidos):
    print("")
    print("---- PEDIDOS POR STATUS ----")

    pendente = 0
    em_rota = 0
    entregue = 0
    cancelado = 0

    for pid in pedidos:
        status = pedidos[pid]["status_pedido"]

        if status == "PENDENTE":
            pendente = pendente + 1
        elif status == "EM ROTA":
            em_rota = em_rota + 1
        elif status == "ENTREGUE":
            entregue = entregue + 1
        elif status == "CANCELADO":
            cancelado = cancelado + 1

    print("Pendente : " + str(pendente))
    print("Em Rota  : " + str(em_rota))
    print("Entregue : " + str(entregue))
    print("Cancelado: " + str(cancelado))

    print("")


def relatorio_alta_prioridade(pedidos):
    print("")
    print("---- PEDIDOS COM ALTA PRIORIDADE ----")

    encontrados = 0

    for pid in pedidos:
        prioridade = pedidos[pid]["prioridade"]

        if prioridade == "ALTA":
            encontrados = encontrados + 1
            nome = pedidos[pid]["nome_cliente"]
            estado = pedidos[pid]["estado"]
            regiao = pedidos[pid]["regiao"]
            endereco = pedidos[pid]["endereco"]
            status = pedidos[pid]["status"]

            print("ID      : " + pid)
            print("Cliente : " + nome)
            print("Estado  : " + estado)
            print("Região  : " + regiao)
            print("Endereco: " + endereco)
            print("Status  : " + status)
            print("---")

    if encontrados == 0:
        print("Nenhum pedido com Alta Prioridade encontrado.")
    else:
        print("Total de pedidos com Alta Prioridade: " + str(encontrados))

    print("")


def relatorio_top_entregador(entregadores, pedidos):
    print("")
    print("---- ENTREGADOR COM MAIS ENTREGAS ----")

    if len(entregadores) == 0:
        print("Nenhum entregador cadastrado.")
        print("")
        return

    maior_numero = 0
    nome_lider = ""
    id_lider = ""

    for eid in entregadores:
        total_entregues = 0
        lista_pedidos = entregadores[eid]["pedidos"]

        for pid in lista_pedidos:
            if pid in pedidos:
                if pedidos[pid]["status_pedido"] == "ENTREGUE":
                    total_entregues = total_entregues + 1

        if total_entregues > maior_numero:
            maior_numero = total_entregues
            nome_lider = entregadores[eid]["nome"]
            id_lider = eid

    if maior_numero == 0:
        print("Nenhum entregador possui entregas concluidas.")
    else:
        print("ID    : " + id_lider)
        print("Nome  : " + nome_lider)
        print("Total : " + str(maior_numero) + " entrega(s) concluida(s)")
