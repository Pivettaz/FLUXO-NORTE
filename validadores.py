def gerenciar_entrada_numerica(min_val, max_val, mensagem):
    escolha = input(mensagem)

    if not escolha.isdigit():
        print(f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        return False
    elif min_val <= int(escolha) <= max_val:
        return int(escolha)
    else:
        print(f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        return False

def validar_id_entregador(id_entregador):
    if not id_entregador.isdigit():
        print("\nID do entregador não deve conter letras")
        return False
    elif len(id_entregador) != 4:
        print("\nID do entregador deve conter apenas 4 dígitos")
        return False
    return True

def validar_id_pedido(id_pedido):
    if len(id_pedido) != 5:
        print("ID deve conter 5 dígitos")
        return False
    elif not id_pedido[0].isalpha():
        print("Primeiro dígito do ID deve ser uma letra")
        return False
    elif not id_pedido[1:].isdigit():
        print("Quatro últimos dígitos do ID devem ser um número")
        return False
    return True
