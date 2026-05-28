import os
from cores import BRANCO

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def confirmacao():
    input(BRANCO + "\nPressione Enter para voltar ao menu...")