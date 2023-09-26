from pyfiglet import Figlet
import folium
import colorama
from colorama import Fore, Style
import subprocess
import os


preview_text = Figlet(font='slant')
print(Fore.BLUE + preview_text.renderText('OUR DISCORD'))
print("Дискорд поддерживающий OsintX - https://discord.gg/wm3RBZrHSn")

a = input("Назад - 0: ")
if a == "0":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

   clear_console()
   subprocess.run(["python", "main.py"])