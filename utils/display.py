import os
import sys
import datetime
from colorama import init, Fore, Back, Style

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass
init(autoreset=True)

LOGO = f"""
{Fore.RED}████████╗  ██████╗  ██████╗      ████████╗███████╗ █████╗ ███╗   ███╗
╚══██╔══╝ ██╔═══██╗ ██╔══██╗     ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
   ██║    ██║   ██║ ██████╔╝        ██║   █████╗  ███████║██╔████╔██║
   ██║    ██║   ██║ ██╔══██╗        ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
   ██║    ╚██████╔╝ ██║  ██║        ██║   ███████╗██║  ██║██║ ╚═╝ ██║
   ╚═╝     ╚═════╝  ╚═╝  ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
{Style.RESET_ALL}
"""

SEPARATOR = f"{Fore.RED}{'─'*60}{Style.RESET_ALL}"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(LOGO)
    print(f"{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE} Session: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{Fore.RED}[{Fore.WHITE}+{Fore.RED}]{Fore.WHITE} TOR TEAM OSINT")
    print(SEPARATOR)

def print_info(info, title="РЕЗУЛЬТАТ СКАНИРОВАНИЯ"):
    print()
    print(f"{Fore.RED}┌{'─'*56}┐")
    print(f"{Fore.RED}│ {Fore.WHITE}{title:<54}{Fore.RED} │")
    print(f"{Fore.RED}├{'─'*56}┤")
    for key, value in info.items():
        if value is not None and value != "":
            val = str(value)
            print(f"{Fore.RED}│ {Fore.YELLOW}{key:<24}{Fore.RED}│ {Fore.GREEN}{val:<28}{Fore.RED} │")
    print(f"{Fore.RED}└{'─'*56}┘{Style.RESET_ALL}")

def print_error(msg):
    print(f"\n{Fore.RED}[!] {msg}{Style.RESET_ALL}")

def print_success(msg):
    print(f"\n{Fore.GREEN}[+] {msg}{Style.RESET_ALL}")

def print_warning(msg):
    print(f"\n{Fore.YELLOW}[*] {msg}{Style.RESET_ALL}")

def print_links(links, title="ССЫЛКИ ДЛЯ ПРОВЕРКИ"):
    print()
    print(f"{Fore.RED}┌{'─'*56}┐")
    print(f"{Fore.RED}│ {Fore.WHITE}{title:<54}{Fore.RED} │")
    print(f"{Fore.RED}├{'─'*56}┤")
    for name, url in links.items():
        print(f"{Fore.RED}│ {Fore.YELLOW}{name:<16}{Fore.RED}│ {Fore.CYAN}{url:<36}{Fore.RED} │")
    print(f"{Fore.RED}└{'─'*56}┘{Style.RESET_ALL}")

def input_number():
    return input(f"\n{Fore.RED}[{Fore.WHITE}>{Fore.RED}]{Fore.WHITE} Номер (международный формат): {Style.RESET_ALL}").strip()

def input_choice():
    return input(f"{Fore.RED}[{Fore.WHITE}>{Fore.RED}]{Fore.WHITE} Выберите: {Style.RESET_ALL}").strip()
