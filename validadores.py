def gerenciar_entrada_numerica(min_val, max_val):
    escolha = input("Digite uma opção: ")

    if not escolha.isdigit():
        print(f"\nPor favor, insira uma opção entre {min_val} e {max_val}")
        return False
    elif min_val <= int(escolha) <= max_val:
        return escolha
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
