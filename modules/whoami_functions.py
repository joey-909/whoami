import socket
import platform
import os

RED = '\033[91m'
GREEN = '\33[32m'
END = '\033[0m'

try:
    import requests
    import pathlib

except:
    print(f"\n{RED}[!]{END} Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()

def check_updates(version):
    try:
        version_update_source = requests.get("https://raw.githubusercontent.com/whoami-99/whoami/main/version.txt")
        version_update_source = version_update_source.text
        
        if version_update_source != version:
            print(f"\n{RED}[!]{END} New Update Available {version_update_source}, You Can Type 'whoami' And You Will See Our Github Link To Download The Latest Version.")

        if version_update_source == version:
            print(f"\n{GREEN}[+]{END} Whoami Is Uptodate.")
    except:
        print(f"\n{RED}[!]{END} Failed To Check For Updates.")

def local_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip
        
    except:
        return(f"\n{RED}[!]{END} Error While Getting Your Local Ip.")


def machine_os():
    try:
        machine_os = platform.system()
        return machine_os

    except Exception as e:
        return(f"\n{RED}[!]{END} Failed To Get The Machine Os.")

def clear():
    if machine_os() == "Windows":
        clear = os.system("cls")
        
    else:
        clear = os.system("clear")

def payloads_number():
    payloads_number = (sum(1 for x in pathlib.Path("whoami_payloads/").glob('*.py') if x.is_file()))
    return payloads_number