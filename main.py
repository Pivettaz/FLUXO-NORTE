from Menu.menu import menu_principal
from colorama import init,Fore,Style

AMARELO = Fore.YELLOW + Style.BRIGHT
BRANCO = Fore.WHITE + Style.BRIGHT
VERDE = Fore.GREEN + Style.BRIGHT
VERMELHO = Fore.RED + Style.BRIGHT


init(autoreset=True)
menu_principal()