import time
import os
import subprocess
import colorama
from colorama import Fore, Style
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

# Данные о номере телефона 2

print(Fore.BLUE + " ")
time.sleep(0.3)
print("░█████╗░░██████╗██╗███╗░░██╗████████╗██╗░░██╗")
time.sleep(0.3)
print("██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝╚██╗██╔╝")
time.sleep(0.3)
print("██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░░╚███╔╝░")
time.sleep(0.3)
print("██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░░██╔██╗░")
time.sleep(0.3)
print("╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░██╔╝╚██╗")
time.sleep(0.3)
print("░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝")

time.sleep(1.0)

txt = Fore.YELLOW + '-----------------------------------------------------'
for i in txt:
    time.sleep(0.1)
    print(i, end='', flush=True)

print(" ")

txt1 = Fore.GREEN + 'OSINTX || Создатель - IArepetsky || Поддержка - Kero'
for i in txt1:
    time.sleep(0.1)
    print(i, end='', flush=True)

print("")

txt2 = Fore.GREEN + '[1] Пробив по номеру   [2] Пробив по IP   [3] Наш Дс'
for i in txt2:
    time.sleep(0.03)
    print(i, end='', flush=True)

print("")
print(" ")

txt3 = Fore.GREEN + '[*] Выберите Действие:'
for i in txt3:
    time.sleep(0.05)
    print(i, end='', flush=True)
   
a = input(" ") 



if a == "1":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


   clear_console()
   subprocess.run(["python", "phone.py"])

if a == "2":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


   clear_console()
   subprocess.run(["python", "ip.py"])

if a == "3":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


   clear_console()
   subprocess.run(["python", "Discord.py"])
