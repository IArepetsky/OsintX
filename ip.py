import time
import subprocess
import os
import requests
from pyfiglet import Figlet
import folium
import colorama
from colorama import Fore, Style


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Страна]': response.get('country'),
            '[Имя региона]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
        
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('[!] Проверьте доступ к интернету!')
        
        
def main():
    preview_text = Figlet(font='slant')
    print(Fore.GREEN + preview_text.renderText('IP INFO'))
    ip = input('Введите айпи жертвы: ')
    
    get_info_by_ip(ip=ip)
    
    
if __name__ == '__main__':
    main()


time.sleep(1)

a = input("Назад - 0: ")
if a == "0":
   def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

   clear_console()
   subprocess.run(["python", "main.py"])
