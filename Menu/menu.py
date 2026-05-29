from utils import limpar_tela, confirmacao
import Menu.sub_menus as sm
from Validacao.validadores import gerenciar_entrada_numerica
from Gerenciamento.pedidos import cadastrar_pedido, atualizar_pedido, reativar_pedido, solicitar_reembolso
from Gerenciamento.entregadores import cadastrar_entregador
from Gerenciamento.consulta_infomações import pedidos_pendentes, pedidos_em_rota, pedidos_entregues, pedidos_cancelados, pedidos_reembolsados, buscar_pedido, consultar_entregadores_disponiveis, entregas_entregador
from  Relatorios_Operacao.relatorio import relatorio_total_pedidos, relatorio_pedidos_por_status, relatorio_alta_prioridade_todos, relatorio_alta_prioridade_pendente, relatorio_alta_prioridade_em_rota, relatorio_top_entregador
from cores import VERDE


def menu_principal():
    lista_pedidos = []
    lista_entregadores = []
    executando_menu_principal = 1

    while executando_menu_principal:
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

                escolha_menu_pedidos = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
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
                    escolha_menu_entregadores = gerenciar_entrada_numerica(1, 2, "\nDigite uma opção novamente: ")

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

                escolha_menu_consulta = gerenciar_entrada_numerica(1, 9, "\nDigite uma opção: ")
                while not escolha_menu_consulta:
                    limpar_tela()
                    sm.sub_menu_consultas()
                    escolha_menu_consulta = gerenciar_entrada_numerica(1, 9, "\nDigite uma opção novamente: ")

                match escolha_menu_consulta:
                    case 1:
                        limpar_tela()
                        pedidos_pendentes(lista_pedidos)
                    case 2:
                        limpar_tela()
                        pedidos_em_rota(lista_pedidos)
                    case 3:
                        limpar_tela()
                        pedidos_entregues(lista_pedidos)
                    case 4:
                        limpar_tela()
                        pedidos_cancelados(lista_pedidos)
                    case 5:
                        limpar_tela()
                        pedidos_reembolsados(lista_pedidos)
                    case 6:
                        buscar_pedido(lista_pedidos)
                    case 7:
                        limpar_tela()
                        consultar_entregadores_disponiveis(lista_entregadores)
                    case 8:
                        limpar_tela()
                        entregas_entregador(lista_pedidos, lista_entregadores)
                    case 9:
                        executando_menu_consulta = 0

        elif escolha_menu_principal == 4:
            executando_menu_relatorios = 1
            while executando_menu_relatorios:
                limpar_tela()
                sm.sub_menu_relatorios()

                escolha_menu_relatorios = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção: ")
                while not escolha_menu_relatorios:
                    limpar_tela()
                    sm.sub_menu_relatorios()
                    escolha_menu_relatorios = gerenciar_entrada_numerica(1, 5, "\nDigite uma opção novamente: ")

                match escolha_menu_relatorios:
                    case 1:
                        limpar_tela()
                        relatorio_total_pedidos(lista_pedidos)
                    case 2:
                        limpar_tela()
                        relatorio_pedidos_por_status(lista_pedidos)
                    case 3:
                        executando_alta_prioridade = 1
                        while executando_alta_prioridade:
                            limpar_tela()
                            sm.sub_menu_alta_prioridade()

                            escolha_alta_prioridade = gerenciar_entrada_numerica(1, 4, "\nDigite uma opção: ")
                            while not escolha_alta_prioridade:
                                limpar_tela()
                                sm.sub_menu_alta_prioridade()
                                escolha_alta_prioridade = gerenciar_entrada_numerica(1, 4, "\nDigite uma opção novamente: ")

                            match escolha_alta_prioridade:
                                case 1:
                                    limpar_tela()
                                    relatorio_alta_prioridade_todos(lista_pedidos)
                                case 2:
                                    limpar_tela()
                                    relatorio_alta_prioridade_pendente(lista_pedidos)
                                case 3:
                                    limpar_tela()
                                    relatorio_alta_prioridade_em_rota(lista_pedidos)
                                case 4:
                                    executando_alta_prioridade = 0
                    case 4:
                        limpar_tela()
                        relatorio_top_entregador(lista_entregadores, lista_pedidos)
                    case 5:
                        executando_menu_relatorios = 0

        else:
            limpar_tela()
            print(VERDE + "Sistema Finalizado com Sucesso.")
            executando_menu_principal = 0