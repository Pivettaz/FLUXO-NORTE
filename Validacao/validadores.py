from time import sleep
from cores import BRANCO, VERDE, VERMELHO, AMARELO


def gerenciar_entrada_numerica(min_val, max_val, mensagem):
    escolha = input(mensagem)

    if not escolha.isdigit():
        print(AMARELO + f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        sleep(1.5)
        return False
    elif min_val <= int(escolha) <= max_val:
        return int(escolha)
    else:
        print(AMARELO + f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        sleep(1.5)
        return False


def validar_nome(nome):
    nome_limpo = nome.strip()

    if len(nome_limpo) < 3 or not nome_limpo.replace(" ", "").isalpha():
        print(AMARELO + "Nome deve conter pelo menos 3 letras e não conter símbolos ou números.")
        sleep(1.5)
        return False

    return True

def validar_id_entregador(id_entregador):
    if not id_entregador.isdigit():
        print(AMARELO + "\nID do entregador não deve conter letras")
        sleep(1.5)
        return False
    elif len(id_entregador) != 4:
        print(AMARELO + "\nID do entregador deve conter apenas 4 dígitos")
        sleep(1.5)
        return False
    return True

def validar_id_pedido(id_pedido):
    if len(id_pedido) != 5:
        print(AMARELO + "ID deve conter 5 dígitos")
        sleep(1.5)
        return False
    elif not id_pedido[0].isalpha():
        print(AMARELO + "Primeiro dígito do ID deve ser uma letra")
        sleep(1.5)
        return False
    elif not id_pedido[1:].isdigit():
        print(AMARELO + "\nQuatro últimos dígitos do ID devem ser um número")
        sleep(1.5)
        return False
    return id_pedido.upper()

