import requests
from termcolor import colored as cl
import os
from requests.exceptions import Timeout

os.system('clear')

path = input(cl("PATH To Your List >> ", color='blue'))
lista = open(path, 'r').read().split('\n')

for url in lista:
    try:
        url_2 = f"https://{url}"
        req = requests.get(url_2, timeout=2).status_code
        if req == 200:
            print(cl(f"200 ====> {url_2}", color='green'))
            valid = open('200.txt', 'a')
            valid.write(url_2+"\n")
        
        else:
            print(cl(f"{req} =====> {url_2}", color='red'))
            
    except Timeout:
        print(cl('Timeout has been raised.', color='yellow'))
        continue
    except:
        continue
