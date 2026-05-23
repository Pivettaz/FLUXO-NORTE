# lista_pedidos = [] ESTÁ LISTA DEVE ESTAR FORA DA FUNÇÃO NO ARQUIVO PRINCIPAL PARA ADICIONAR OS PEDIDOS

lista_pedidos = []

def cadastrar_pedido():

    campos = ["id_pedido", "nome_cliente", "prioridade", "descricao_pedido", "status_pedido", "id_entregador"]

    pedido = dict.fromkeys(campos)
    pedido["id_pedido"] = input("Digite o ID do pedido") # Implementar o ID automático
    pedido["nome_cliente"] = input("Insira o nome do cliente: ")
    pedido["prioridade"] = int(input("[1] ALTA \n[2] NORMAL \nEscolha a prioridade: ")) # Implementar barreiras
    pedido["descricao_pedido"] = input("Insira a descrição do produto: ")
    pedido["status_pedido"] = input("Insira o status do pedido: \n[1] PENDENTE "
                                    "\n[2] EM ROTA \n[3] ENTREGUE "
                                    "\n[4] CANCELADO")
    pedido["id_entregador"] = int(input("Insira o ID do entregador responsável: ")) # Implementar barreiras

    lista_pedidos.append(pedido)
    print("\nPedido cadastrado com sucesso!")

# Função base apenas para ver como listar o pedido após o cadastro
def listar_pedidos():
    if not lista_pedidos:
        print("\nNenhum pedido cadastrado ainda.")
        return

    print("\n=== LISTA DE PEDIDOS ===")
    for p in lista_pedidos:
        prioridade_texto = "ALTA" if p["prioridade"] == 1 else "NORMAL"

        print(f"ID: {p["id_pedido"]} | Cliente: {p["nome_cliente"]} | Prioridade: {prioridade_texto}")
        print(
            f"Descrição: {p["descricao_pedido"]} | Status: {p["status_pedido"]} | Entregador ID: {p["id_entregador"]}")
        print("-" * 30)
