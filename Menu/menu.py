from utils import limpar_tela
import Menu.sub_menus as sm
from Validacao.validadores import gerenciar_entrada_numerica
from Gerenciamento.pedidos import cadastrar_pedido, atualizar_pedido, reativar_pedido, solicitar_reembolso
from Gerenciamento.entregadores import cadastrar_entregador
from Gerenciamento.consulta_infomações import pedidos_pendentes, pedidos_entregues, buscar_pedido, entregadores_disponiveis, entregas_entregador

def menu_principal():
    lista_pedidos = []
    lista_entregadores = []
    executando_menu_princpal = 1
    while executando_menu_princpal:
        limpar_tela()
        sm.sub_menu_principal()

        escolha_menu_principal = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
        while not escolha_menu_principal:
            limpar_tela()
            sm.sub_menu_principal()
            escolha_menu_principal = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")

        if escolha_menu_principal == 1:
            executando_menu_pedidos = 1
            while executando_menu_pedidos:
                limpar_tela()
                sm.sub_menu_pedidos()

                escolha_menu_pedidos = gerenciar_entrada_numerica(1,5, "\nDigite uma opção: ")
                while not escolha_menu_pedidos:
                    limpar_tela()
                    sm.sub_menu_pedidos()
                    escolha_menu_pedidos = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")

                match escolha_menu_pedidos:
                    case 1:
                        limpar_tela()
                        cadastrar_pedido(lista_pedidos, lista_entregadores)
                    case 2:
                        limpar_tela()
                        atualizar_pedido(lista_pedidos, lista_entregadores)
                    case 3:
                        limpar_tela()
                        reativar_pedido(lista_pedidos, lista_entregadores)
                    case 4:
                        limpar_tela()
                        solicitar_reembolso(lista_pedidos)
                    case 5:
                        executando_menu_pedidos = 0
        elif escolha_menu_principal == 2:
            executando_menu_entregadores = 1
            while executando_menu_entregadores:
                limpar_tela()
                sm.sub_menu_entregadores()

                escolha_menu_entregadores = gerenciar_entrada_numerica(1, 2, "\nDigite uma opção: ")
                while not escolha_menu_entregadores:
                    limpar_tela()
                    sm.sub_menu_entregadores()
                    escolha_menu_entregadores = gerenciar_entrada_numerica(1, 2, "\nDigite uma opção novamente:")

                match escolha_menu_entregadores:
                    case 1:
                        limpar_tela()
                        cadastrar_entregador(lista_entregadores)
                    case 2:
                        executando_menu_entregadores = 0
        elif escolha_menu_principal == 3:
            executando_menu_consulta = 1
            while executando_menu_consulta:
                limpar_tela()
                sm.sub_menu_consultas()

                escolha_menu_consulta = gerenciar_entrada_numerica(1, 6, "\nDigite uma opção: ")
                while not escolha_menu_consulta:
                    limpar_tela()
                    sm.sub_menu_consultas()
                    escolha_menu_consulta = gerenciar_entrada_numerica(1, 6, "\nDigite uma opção novamente: ")

                match escolha_menu_consulta:
                    case 1:
                        limpar_tela()
                        pedidos_pendentes(lista_pedidos)
                    case 2:
                        limpar_tela()
                        pedidos_entregues(lista_pedidos)
                    case 3:
                        limpar_tela()
                        buscar_pedido(lista_pedidos)
                    case 4:
                        limpar_tela()
                        entregadores_disponiveis(lista_entregadores)
                    case 5:
                        limpar_tela()
                        entregas_entregador(lista_pedidos, lista_entregadores)
                    case 6:
                        executando_menu_consulta = 0
        elif escolha_menu_principal == 4:
            executando_menu_relatorios = 1
            while executando_menu_relatorios:
                limpar_tela()
                sm.sub_menu_relatorios()

                escolha_menu_relatorios = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
                while not escolha_menu_relatorios:
                    limpar_tela()
                    escolha_menu_relatorios = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")

                match escolha_menu_relatorios:
                    case 1:
                        limpar_tela()
                        sm.sub_menu_relatorios()
                        print("Implementar relatório do total de pedidos")
                    case 2:
                        limpar_tela()
                        print("Implementar relatório da quantidade de pedidos por status")
                    case 3:
                        limpar_tela()
                        print("Implementar relatório de pedidos urgentes")
                    case 4:
                        limpar_tela()
                        print("Implementar relatório de entregador com maior número de entregas")
                    case 5:
                        executando_menu_relatorios = 0
        else:
            limpar_tela()
            print("Sistema Finalizado")
            executando_menu_princpal = 0


