import time
import os
import subprocess
import colorama
from colorama import Fore, Style
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Данные о номере телефона 2

print(Fore.GREEN + " ")
time.sleep(0.5)
print("░█████╗░░██████╗██╗███╗░░██╗████████╗██╗░░██╗")
time.sleep(0.5)
print("██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝╚██╗██╔╝")
time.sleep(0.5)
print("██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░░╚███╔╝░")
time.sleep(0.5)
print("██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░░██╔██╗░")
time.sleep(0.5)
print("╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░██╔╝╚██╗")
time.sleep(0.5)
print("░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝")
time.sleep(1.5)
print(Fore.YELLOW + "-----------------------------------------------------")
print(Fore.BLUE + "OSINTX || Создатель - IArepetsky || Поддержка - Kero")

print("1. Пробив по номеру                                      2. Наш дс")
print("3. Пробив по IP                                          4. ...")

a = input("Выберите действие: ")
if a == "1":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


   clear_console()
   subprocess.run(["python", "phone.py"])

if a == "3":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


   clear_console()
   subprocess.run(["python", "ip.py"])

if a == "2":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


   clear_console()
   subprocess.run(["python", "Discord.py"])
