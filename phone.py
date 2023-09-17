import time
import os
import subprocess
import colorama
from colorama import Fore, Style
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

time.sleep(0.5)
print(Fore.GREEN + " ")
time.sleep(0.5)
print("██████╗░██╗░░██╗░█████╗░███╗░░██╗███████╗")
time.sleep(0.5)
print("██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝")
time.sleep(0.5)
print("██████╔╝███████║██║░░██║██╔██╗██║█████╗░░")
time.sleep(0.5)
print("██╔═══╝░██╔══██║██║░░██║██║╚████║██╔══╝░░")
time.sleep(0.5)
print("██║░░░░░██║░░██║╚█████╔╝██║░╚███║███████╗")
time.sleep(0.5)
print("╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝╚══════╝")
time.sleep(1)
print(Fore.YELLOW + "-----------------------------------------------------")
print(Fore.BLUE + "Пробив по номеру телефона || Создатель - IArepetsky || Поддержка - Kero")
ph = phonenumbers.parse(input("Введите номер телефона:"))

time.sleep(1)
print("Страна: " + geocoder.country_name_for_number(ph, 'ru'))

time.sleep(1)
print("Оператор: " + carrier.name_for_number(ph, lang='en'))

time.sleep(1)
timeZone = timezone.time_zones_for_number(ph)
print(' ' .join(timeZone))

time.sleep(1)

a = input("Назад - 0: ")
if a == "0":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

   clear_console()
   subprocess.run(["python", "main.py"])