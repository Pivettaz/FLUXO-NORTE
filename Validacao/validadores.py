from time import sleep

def gerenciar_entrada_numerica(min_val, max_val, mensagem):
    escolha = input(mensagem)

    if not escolha.isdigit():
        print(f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        sleep(1.5)
        return False
    elif min_val <= int(escolha) <= max_val:
        return int(escolha)
    else:
        print(f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        sleep(1.5)
        return False

def validar_regiao(regiao):
    if not regiao.isdigit():
        print("\nRegião só pode ser númerica")
        sleep(1.5)
        return False
    return True

def validar_id_entregador(id_entregador):
    if not id_entregador.isdigit():
        print("\nID do entregador não deve conter letras")
        sleep(1.5)
        return False
    elif len(id_entregador) != 4:
        print("\nID do entregador deve conter apenas 4 dígitos")
        sleep(1.5)
        return False
    return True

def validar_id_pedido(id_pedido):
    if len(id_pedido) != 5:
        print("ID deve conter 5 dígitos")
        sleep(1.5)
        return False
    elif not id_pedido[0].isalpha():
        print("Primeiro dígito do ID deve ser uma letra")
        sleep(1.5)
        return False
    elif not id_pedido[1:].isdigit():
        print("\nQuatro últimos dígitos do ID devem ser um número")
        sleep(1.5)
        return False
    return id_pedido.upper()

