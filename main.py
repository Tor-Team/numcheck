#!/usr/bin/env python3
import sys
from colorama import Fore, Style, init
init(autoreset=True)
from utils.display import print_header, print_info, print_error, print_success, print_warning, print_links, input_number, input_choice, SEPARATOR
from core.phone_info import get_phone_info
from core.social_check import check_social_networks, get_social_links
from core.breach_check import get_breach_links, get_breach_summary

def menu_basic_scan():
    number = input_number()
    if not number:
        print_error("Номер не введён")
        return
    info = get_phone_info(number)
    if "Ошибка" in info:
        print_error(info["Ошибка"])
        return
    print_info(info, "БАЗОВАЯ ИНФОРМАЦИЯ О НОМЕРЕ")

def menu_social_scan():
    number = input_number()
    if not number:
        print_error("Номер не введён")
        return
    print_warning("Выполняется проверка социальных сетей...")
    results = check_social_networks(number)
    print_info(results, "ПРОВЕРКА СОЦИАЛЬНЫХ СЕТЕЙ")
    links = get_social_links(number)
    print_links(links, "ССЫЛКИ ДЛЯ ПЕРЕХОДА")

def menu_breach_scan():
    number = input_number()
    if not number:
        print_error("Номер не введён")
        return
    summary = get_breach_summary(number)
    print_info(summary, "ПРОВЕРКА УТЕЧЕК ДАННЫХ")
    links = get_breach_links(number)
    print_links(links, "СЕРВИСЫ ДЛЯ ПРОВЕРКИ УТЕЧЕК")

def menu_full_scan():
    number = input_number()
    if not number:
        print_error("Номер не введён")
        return
    info = get_phone_info(number)
    if "Ошибка" in info:
        print_error(info["Ошибка"])
        return
    print_info(info, "ПОЛНАЯ ИНФОРМАЦИЯ О НОМЕРЕ")
    print_warning("Выполняется проверка социальных сетей...")
    social = check_social_networks(number)
    print_info(social, "СОЦИАЛЬНЫЕ СЕТИ")
    links = get_social_links(number)
    print_links(links, "ССЫЛКИ НА СОЦСЕТИ")
    breach = get_breach_summary(number)
    print_info(breach, "УТЕЧКИ ДАННЫХ")
    blinks = get_breach_links(number)
    print_links(blinks, "СЕРВИСЫ УТЕЧЕК")

def main():
    print_header()
    while True:
        print(f"\n{Fore.RED}ГЛАВНОЕ МЕНЮ:{Style.RESET_ALL}")
        print(f"  {Fore.RED}[{Fore.WHITE}1{Fore.RED}]{Fore.WHITE} Базовая информация о номере")
        print(f"  {Fore.RED}[{Fore.WHITE}2{Fore.RED}]{Fore.WHITE} Проверка социальных сетей")
        print(f"  {Fore.RED}[{Fore.WHITE}3{Fore.RED}]{Fore.WHITE} Проверка утечек данных")
        print(f"  {Fore.RED}[{Fore.WHITE}4{Fore.RED}]{Fore.WHITE} Полный анализ")
        print(f"  {Fore.RED}[{Fore.WHITE}5{Fore.RED}]{Fore.WHITE} Выход")
        print(SEPARATOR)
        choice = input_choice()
        if choice == "1":
            menu_basic_scan()
        elif choice == "2":
            menu_social_scan()
        elif choice == "3":
            menu_breach_scan()
        elif choice == "4":
            menu_full_scan()
        elif choice == "5":
            print(f"\n{Fore.RED}═══════════════════════════════════════════")
            print(f"{Fore.GREEN} TOR TEAM — завершение сессии")
            print(f"{Fore.RED}═══════════════════════════════════════════{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print_error("Неверный выбор")

if __name__ == "__main__":
    main()
